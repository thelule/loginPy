class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Nombre: ", self.nombre, ", y tiene ", self.edad, " años de edad.")

    def hablar(self, palabras="Nada que decir"):
        print(self.nombre, ':', palabras)

    def decir(self, *palabras):
        for frase in palabras:
            print(self.nombre, ':', frase)

    def platicar(self, **palabras):
        for frase in palabras:
            print(self.nombre, ':', palabras[frase])

class Trabajador(Persona):
    def __init__(self, nombre, edad, adscripcion='"Sin adscripción"'):
        self.nombre = nombre
        self.edad = edad
        self.__adscripcion = adscripcion
        print("Nombre: ", self.nombre, ", y tiene ", self.edad, " años de edad. Y trabaja en", self.__adscripcion)

    def trabajar(self):
        print(self.nombre, "está trabajando")

    def verAdscripcion(self):
        return self.__adscripcion

david = Persona("David", 33)

ana = Persona("Ana", 31)

david.hablar("Hola Ana, cómo te va?")
ana.hablar("Bien, y tú q'ongo?")
david.decir("Todo bien, gracias", "Cuéntame cómo te fue ayer")
ana.platicar(respuesta="Comí atún y me hizo daño", pregunta="tú q'comistes?")

maria = Trabajador("María", 25)
maria.trabajar()

pedro = Trabajador("Pedro", 42, "Políticas")
pedro.edad = 43
print(pedro.edad)
pedro.verAdscripcion()