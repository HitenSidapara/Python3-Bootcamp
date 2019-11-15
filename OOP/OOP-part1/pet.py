class pet:
    allowed = ('cat','dog','fish','rat')
    def __init__(self,name,species):
        if species not in pet.allowed:
            raise ValueError(f"you cant not have {species} pet!")
        self.name = name
        self.species = species
        print(f"{self.name} = {self.species}")

    def set_attribute(self,species):
        if species not in pet.allowed:
            raise ValueError(f"you cant not have {species} pet!")
        self.species=species


c = pet("blue","cat")
c.set_attribute("dog")
print(c.name,c.species)
d = pet("rusty","dog")
d.set_attribute("cat")
print(d.name,d.species)

#############################################################
print(pet.allowed)
# refer all the inatsance to the same class
print(c.allowed)
print(d.allowed)

c.allowed = ("Tiger","Pig")
# not reference to the pet class but the dog class still allowed to the pet class
print(c.allowed)