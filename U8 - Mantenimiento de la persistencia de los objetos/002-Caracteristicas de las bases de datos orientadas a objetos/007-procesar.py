#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from lxml import html


INPUT_HTML = Path("guardado.html")
OUT_JSON = Path("housing_ads.json")
OUT_CSV = Path("housing_ads.csv")


def _find_balanced_object(text: str, any_pos_inside: int) -> Optional[Tuple[int, int]]:
    """
    Given a position that is inside a JSON object in `text`,
    return (start_index, end_index_exclusive) of the balanced {...} object.
    Uses brace counting while respecting JSON strings.
    """
    # Find nearest '{' to the left
    start = text.rfind("{", 0, any_pos_inside)
    if start == -1:
        return None

    i = start
    depth = 0
    in_str = False
    esc = False

    while i < len(text):
        ch = text[i]

        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return (start, i + 1)

        i += 1

    return None


def extract_candidate_json_objects(page_text: str) -> List[Dict[str, Any]]:
    """
    Extract JSON objects that look like 'housing ads' by locating markers like "propertyId"
    and then brace-matching to parse the containing object.
    """
    markers = [
        '"propertyId":',        # common in list cards
        '"detailUrl":',         # link to ad detail
        '"realEstateAdId":',    # uuid id
        '"rawPrice":',          # appears in other embedded blobs
    ]

    # collect all marker occurrences
    positions = []
    for m in markers:
        positions.extend([m.start() for m in re.finditer(re.escape(m), page_text)])
    positions = sorted(set(positions))

    objs: List[Dict[str, Any]] = []
    seen_fingerprints = set()

    for pos in positions:
        span = _find_balanced_object(page_text, pos)
        if not span:
            continue
        s, e = span
        blob = page_text[s:e].strip()

        # quick filter to avoid parsing tons of unrelated JSON objects
        if '"propertyId"' not in blob and '"detailUrl"' not in blob and '"rawPrice"' not in blob:
            continue

        try:
            data = json.loads(blob)
        except Exception:
            continue

        # Heuristic: keep objects that look like an ad
        looks_like_ad = (
            isinstance(data, dict)
            and (
                ("propertyId" in data)
                or ("detailUrl" in data)
                or ("realEstateAdId" in data)
                or ("rawPrice" in data and ("address" in data or "coordinates" in data))
            )
        )
        if not looks_like_ad:
            continue

        # Dedup: propertyId if present; else realEstateAdId; else full blob hash
        fp = (
            f"propertyId:{data.get('propertyId')}"
            if data.get("propertyId") is not None
            else f"realEstateAdId:{data.get('realEstateAdId')}"
            if data.get("realEstateAdId")
            else f"hash:{hash(blob)}"
        )
        if fp in seen_fingerprints:
            continue
        seen_fingerprints.add(fp)

        objs.append(data)

    return objs


def flatten_for_csv(ad: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a practical flattened row for CSV while keeping the full JSON separately.
    """
    price = ad.get("price") if isinstance(ad.get("price"), dict) else {}
    features = ad.get("features") if isinstance(ad.get("features"), dict) else {}
    publisher = ad.get("publisher") if isinstance(ad.get("publisher"), dict) else {}
    location = ad.get("location") if isinstance(ad.get("location"), dict) else {}
    coords = ad.get("coordinates") if isinstance(ad.get("coordinates"), dict) else {}

    # Some blobs use different keys (e.g. address/coordinates/rawPrice)
    address = ad.get("address") if isinstance(ad.get("address"), dict) else {}

    return {
        "propertyId": ad.get("propertyId") or ad.get("id"),
        "realEstateAdId": ad.get("realEstateAdId"),
        "detailUrl": ad.get("detailUrl") or (ad.get("detail") or {}).get("es-ES"),
        "transactionType": ad.get("transactionType") or ad.get("transactionTypeId"),
        "propertyType": ad.get("propertyType") or ad.get("typeId"),
        "propertySubtype": ad.get("propertySubtype") or ad.get("subtypeId") or ad.get("buildingSubtype"),
        "price_amount": price.get("amount") if isinstance(price, dict) else ad.get("rawPrice"),
        "price_drop": price.get("amountDrop") if isinstance(price, dict) else ad.get("reducedPrice"),
        "rooms": features.get("rooms") if isinstance(features, dict) else None,
        "bathrooms": features.get("bathrooms") if isinstance(features, dict) else None,
        "surface": features.get("surface") if isinstance(features, dict) else None,
        "floor": features.get("floor") if isinstance(features, dict) else None,
        "antiquity": features.get("antiquity") if isinstance(features, dict) else None,
        "publisher_name": publisher.get("name"),
        "publisher_alias": publisher.get("alias"),
        "publisher_phone": ad.get("phone"),
        "location_address": location.get("address") or address.get("upperLevel"),
        "location_zone": location.get("zone") or address.get("county"),
        "location_municipality": location.get("municipality") or address.get("district"),
        "location_locality": location.get("locality") or address.get("city"),
        "latitude": coords.get("latitude"),
        "longitude": coords.get("longitude"),
        "multimedia_count": len(ad.get("multimedias", [])) if isinstance(ad.get("multimedias"), list) else 0,
    }


def main() -> None:
    raw = INPUT_HTML.read_text(encoding="utf-8", errors="ignore")
    doc = html.fromstring(raw)

    # 1) Pull all script text (many sites embed JSON here)
    scripts = doc.xpath("//script/text()")
    script_text = "\n".join(scripts)

    # 2) Also search the full raw HTML (sometimes JSON is outside <script> text extraction)
    combined = raw + "\n" + script_text

    ads = extract_candidate_json_objects(combined)

    # Save full JSON
    OUT_JSON.write_text(json.dumps(ads, ensure_ascii=False, indent=2), encoding="utf-8")

    # Save a flattened CSV
    rows = [flatten_for_csv(a) for a in ads]

    # Minimal CSV without extra deps
    import csv
    fieldnames = sorted({k for r in rows for k in r.keys()})
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Extracted ads: {len(ads)}")
    print(f"Wrote: {OUT_JSON.resolve()}")
    print(f"Wrote: {OUT_CSV.resolve()}")


if __name__ == "__main__":
    main()

