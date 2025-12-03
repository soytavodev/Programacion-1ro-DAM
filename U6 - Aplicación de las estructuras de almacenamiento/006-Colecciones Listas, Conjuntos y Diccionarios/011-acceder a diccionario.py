persona = {
	"nombre":"Gustavo Enrique",
  "apellidos":"Delnardo Vallejo",
  "correo":"gustavo1@gmail.com",
  "edad":35,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])
