import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


# Store the object state blue



# blue = Cat("Blue","Scottish Fold","String")
#
#
# with open("pets.pickle", "wb") as file:
# 	pickle.dump(blue, file)




# read the data from the pikle file



# with open("pets.pickle", "rb") as file:
# 	blue = pickle.load(file)
# 	print(blue)
# 	print(blue.play())