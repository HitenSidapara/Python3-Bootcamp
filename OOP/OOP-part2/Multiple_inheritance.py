class Aqualtic:
    print("Aqualtic Init")
    def __init__(self,name):
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return  f"I am {self.name} of the sea!"

class Ambulatory:
    print("Ambulatory Init")
    def __init__(self,name):
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land!"

class Palnguin(Aqualtic,Ambulatory):
    def __init__(self,name):
        print("Palnguin Init")
        Ambulatory.__init__(self,name)
        Aqualtic.__init__(self,name)
        # super().__init__(name)


panguin = Palnguin("panguin")

# aquatic =Aqualtic("fish")
# print(aquatic.swim())
# print(aquatic.greet())
#
# ambulatory=Ambulatory("dog")
# print(ambulatory.walk())
# print(ambulatory.greet())
#
# palnguin = Palnguin("palnguin")
# print(palnguin.swim())
# print(palnguin.walk())
# print(palnguin.greet())