#!/usr/bin/env python3
import os
import torch
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model


# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
DATA_FILE = "004-preentrenamiento relleno.jsonl"   # <- tu fichero JSONL
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"            # <- Qwen 2.5 3B Instruct
OUTPUT_DIR = "./qwen25-3b-jvc-lora"

MAX_LENGTH = 512 # Longitud máxima del bloque de entrenamiento
NUM_EPOCHS = 3 # Cantidad de pasadas que se hace sobre el entrenamiento
LR = 2e-4 # Cuando el error de entrenamiento sea menor, el entrenamiento acaba
BATCH_SIZE = 1
GRAD_ACCUM = 4


def main():
    start_dt = datetime.now() # Momento actual

    print("🚀 Starting Qwen2.5 training (Q/A JSONL)")
    print(f"📄 Dataset: {DATA_FILE}")
    print(f"🧠 Base model: {MODEL_NAME}")
    print("-" * 60)

    # ------------------------------------------------------------
    # Check data file exists
    # ------------------------------------------------------------
    #  Comprueba si existe, y si no, da error
    if not os.path.isfile(DATA_FILE):
        raise FileNotFoundError(f"Training file not found: {DATA_FILE}")

    # ------------------------------------------------------------
    # Device
    # ------------------------------------------------------------
    # Comprueba si tienes CPU o GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        print("💻 CUDA GPU detected. Training in fp16 with LoRA (no 4-bit).")
    else:
        print("💻 No CUDA GPU. Training on CPU (this will be slower).")

    # ------------------------------------------------------------
    # Load dataset
    # ------------------------------------------------------------
    # Carga los dos
    print("📥 Loading dataset with datasets.load_dataset(...)")
    raw_dataset = load_dataset(
        "json",
        data_files=DATA_FILE,
        split="train",
    )
    print(f"✅ Dataset loaded with {len(raw_dataset)} Q/A examples.")

    # ------------------------------------------------------------
    # Tokenizer and model (Qwen)
    # ------------------------------------------------------------
    print("✅ Loading tokenizer (Qwen)...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        use_fast=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("✅ Loading base model (Qwen)...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto" if device == "cuda" else None,
    )
    if device == "cpu":
        model.to(device)

    # ------------------------------------------------------------
    # LoRA (full precision, no bitsandbytes)
    # ------------------------------------------------------------
    print("✅ Wrapping model with LoRA (full precision)...")
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Convert question/answer → chat text
    # ------------------------------------------------------------
    print("🧱 Converting (question/answer) pairs into chat-style text...")

    SYSTEM_PROMPT = (
        "Eres un asistente educativo en español que responde de forma clara, "
        "precisa y concisa a preguntas técnicas."
    )

    def qa_to_text(example):
        q = example.get("question", "")
        a = example.get("answer", "")
        if not isinstance(q, str):
            q = str(q)
        if not isinstance(a, str):
            a = str(a)

        conv = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

        # Qwen Instruct normalmente soporta chat template
        try:
            text = tokenizer.apply_chat_template(
                conv,
                tokenize=False,
                add_generation_prompt=False,
            )
        except Exception:
            # Fallback simple
            text = (
                f"SYSTEM: {SYSTEM_PROMPT}\n"
                f"USER: {q}\n"
                f"ASSISTANT: {a}\n"
            )

        return {"text": text}

    text_dataset = raw_dataset.map(qa_to_text)

    # ------------------------------------------------------------
    # Tokenization
    # ------------------------------------------------------------
    print("✅ Tokenizing dataset...")

    def tokenize_fn(batch):
        out = tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding="max_length",
        )
        out["labels"] = out["input_ids"].copy()
        return out

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    # ------------------------------------------------------------
    # TrainingArguments
    # NOTE: NO overwrite_output_dir (tu versión de transformers no lo soporta)
    # ------------------------------------------------------------
    print("✅ Configuring TrainingArguments...")

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        warmup_ratio=0.03,
        logging_steps=10,
        save_steps=200,
        save_total_limit=1,
        fp16=(device == "cuda"),
        bf16=False,
        dataloader_pin_memory=False,
        report_to="none",
    )

    # ------------------------------------------------------------
    # Trainer
    # ------------------------------------------------------------
    print("✅ Creating Trainer...")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # ------------------------------------------------------------
    # Train
    # ------------------------------------------------------------
    print("🚂 Starting training...")
    train_output = trainer.train()
    print("🏁 Training finished.")

    # ------------------------------------------------------------
    # Save
    # ------------------------------------------------------------
    print("💾 Saving model and tokenizer to", OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("✅ Done.")

    # ------------------------------------------------------------
    # Basic run summary
    # ------------------------------------------------------------
    end_dt = datetime.now()
    print(f"⏱️ Duration: {end_dt - start_dt}")
    metrics = getattr(train_output, "metrics", None)
    if metrics:
        print("📊 Metrics:", metrics)


if __name__ == "__main__":
    main()

