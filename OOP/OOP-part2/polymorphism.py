class Animal:
    def speak(self):
        raise NotImplementedError("Not Implemented By Sub Class")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("woof")

class Fish(Animal):
    pass

c =Cat()
c.speak()
d = Dog()
d.speak()
f = Fish()
f.speak()