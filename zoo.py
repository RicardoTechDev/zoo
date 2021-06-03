from animals import Animals, Bear, Lion, Tiger
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,especie,nombre, edad, *args):
        if especie == 'Lion':
            peso = 0
            for i in args:
                peso = i 
            lion = Lion(nombre, edad, peso)
            self.animals.append(lion)
            #print(lion.nombre)
        elif especie == 'Tiger':
            tiger = Tiger(nombre, edad)
            self.animals.append(tiger)
        elif especie == 'Bear':
            bear = Bear(nombre, edad)
            self.animals.append(bear)
    
    def alimentar_animal(self,nombre_animal, kg_alimento):
        for animal in self.animals: #Recorremos la lista animals 
            #para luego comparar el nombre con el nombre del animal que deseamos alimentar
            if animal.return_nombre() == nombre_animal:
                animal.alimentacion(kg_alimento)#Una vez encontrado lo alimentamos con el metodo alimentación de Animals
        return self
        

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

    



zoo1 = Zoo("John's Zoo")
zoo1.add_animal("Lion","Nala",11,150)
zoo1.add_animal("Lion","Simba",10,160)
zoo1.add_animal("Tiger","Richard",8)
#zoo1.print_all_info()
for animales in zoo1.animals:
    animales.display_info()

zoo1.alimentar_animal("Simba",12)
for animales in zoo1.animals:
    animales.display_info()
