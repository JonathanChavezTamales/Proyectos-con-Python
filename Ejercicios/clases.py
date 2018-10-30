class Alumno:
	def __init__(self, nombre, edad, is_a_lizard):
		self.nombre = nombre
		self.edad = edad
		self.is_a_lizard = is_a_lizard

	def presentarse(self):
		print(f"Hola, me llamo {self.nombre} y tengo {self.edad}.")
		if self.is_a_lizard == True:
			print("Adios amigo, nos vemos en el otro mundo")

juanito = Alumno("Juan", 17, False)

juanito.presentarse()
