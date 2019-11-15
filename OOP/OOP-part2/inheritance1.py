class Animal:
    cool = True

    def make_sound(self,sound):
        print(f"Sound Is {sound}")

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound("Meow")
a = Animal()
a.make_sound("Woof Woof")

print(isinstance(blue,Cat))
print(isinstance(blue,Animal))
print(isinstance(blue,object))