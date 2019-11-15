from copy import copy
class Human:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return f"{self.fname} {self.lname} age is {self.age}"

    def __add__(self, other):
        if isinstance(other,Human):
            return Human(fname="New Born",lname=self.lname,age=0)
        return "Not Adding Those Things"
    def __mul__(self, other):
        if isinstance(other,int):
            return [copy(self) for i in range(other)]
        return "Not Multiply!"


j = Human("Jon","snow",33)
e = Human("Emila","Clark",29)
print(j+e)
print(j+2)

triples=j*3
triples[1].fname="Jokhlisi"
print(triples)
print(j*e)

# Exercise

all = (j+e)*3
print(all)
all[1].fname = "Targerian"
print(all)