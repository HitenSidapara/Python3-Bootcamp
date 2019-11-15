class Human:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        if age >= 0:
            self._age =age
        else:
            self._age=0

    # Using For The Getter

    @property
    def age(self):
        return self._age

    # Using For The Setter

    @age.setter
    def age(self,age):
        if age >= 0:
            self._age =age
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"

    @full_name.setter
    def full_name(self,name):
        self.fname,self.lname = name.split(" ")


    # def get_age(self):
    #     return self.age
    #
    # def set_age(self,age):
    #     self.age=age


    def __repr__(self):
        return f"{self.fname} {self.lname} : {self._age}"


hiten = Human("Hiten","Sidapara",19)
print(hiten)
print(hiten.age)

Akshay = Human("Akshay","Padashala",20)
print(Akshay)
print(Akshay.age)
Akshay.age = 150
print(Akshay.age)

print(Akshay.full_name)
Akshay.full_name = "Nayan Padashala"
print(Akshay.full_name)