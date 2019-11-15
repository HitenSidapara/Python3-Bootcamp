# create the python 1st class

class User:

    activeuser = 0

    @classmethod
    def display_active_user(cls):
        return f"There are currently {User.activeuser} active user"

    @classmethod
    def data_string(cls, data_str):
        fname,lname,age = data_str.split(",");
        return cls(fname,lname,int(age))

    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        User.activeuser +=1

    def __repr__(self):
        return f"{self.full_name()} age is  {self.age}"

    def logout(self):
        User.activeuser -= 1
        return f"{self.fname} has log out"

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def initial(self):
        return f"{self.fname[0]} {self.lname[0]}"

    def seniore(self):
        return self.age >=65

    def birthday(self):
        self.age+=1
        return self.age


hiten=User.data_string("hiten,sidapara,19")
print(hiten)
print(hiten.display_active_user())


raj = User.data_string("Raj,Chovatiya,22")
print(raj)
print(raj.display_active_user())

akshay = User.data_string("Akshay,Padahala,20")
print(akshay)
print(akshay.display_active_user())