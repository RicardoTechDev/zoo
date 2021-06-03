class Animals:
    def __init__(self, nombre, edad, salud, felicidad):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

    def display_info(self):
        print(f"Nombre: {self.nombre}\nSalud: {self.salud}\nFelicidad: {self.felicidad}")
        return self

    def alimentacion(self, kg_alimento):
        self.salud += kg_alimento * 10
        self.felicidad += kg_alimento * 10
        return self

    def return_nombre(self):
        return self.nombre


class Lion(Animals):
    def __init__(self,nombre, edad, peso, salud = 300, felicidad = 150):
        super().__init__(nombre, edad, salud, felicidad)
        self.peso = peso

    def alimentacion(self, kg_alimento):
        self.increase_weight(kg_alimento)
        super().alimentacion(kg_alimento)
        return self

    def increase_weight(self,kg_alimento):
        self.peso += kg_alimento * 0.010
    
    def display_info(self):
        print(f"Nombre: {self.nombre}\n Salud: {self.salud}\n Felicidad: {self.felicidad} \n Peso: {self.peso}")
        return self


class Tiger(Animals):
    def __init__(self, nombre, edad, salud = 250, felicidad = 200):
        super().__init__(nombre, edad, salud, felicidad)

class Bear(Animals):
    def __init__(self, nombre, edad, salud = 350, felicidad = 400):
        super().__init__(nombre, edad, salud, felicidad)   
