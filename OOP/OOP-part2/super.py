class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is {self.species}"


class Cat(Animal):
    def __init__(self,name,age,toy):
        super().__init__(name,species="Cat")
        # Animal.__init__(self,name,species)
        # self.name=name
        # self.species=species
        self.age=age
        self.toy=toy


blue = Cat("Blue","3","String")
print(blue.age,blue.toy)
print(blue)

print(isinstance(blue,Cat))
print(isinstance(blue,Animal))
print(isinstance(blue,object))