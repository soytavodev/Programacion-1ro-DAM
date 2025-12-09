class Profesor():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos

class Alumno():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos
		
alumno1 = Alumno("Gustavo Enrique","Delnardo,gustavo1@gmail.com")
print(alumno1)

profesor1 = Profesor("Juan","Garcia","juan1@gmail.com")
print(profesor1)
		
