# create the python 1st class

class User:

    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def initial(self):
        return f"{self.fname[0]} {self.lname[0]}"

    def seniore(self):
        return self.age >=65

    def birthday(self):
        self.age+=1
        return self.age


user1 = User("Hiten","Sidapara",19)
print(f"is senior : {user1.seniore()}")
print(user1.initial())
print(user1.full_name())
print(f"{user1.fname} {user1.lname} : {user1.age}")

print("*********************************************")

user2 = User("Om","Khunt",1.2)
print(f"{user2.fname} {user2.lname} : {user2.age}")

print("*********************************************")

user3 = User("Narendra","Modi",67);
print(f"is senoir : {user3.seniore()}")
print(user3.initial())
print(user3.full_name())
print(f"{user3.fname} {user3.lname} : {user3.age}")
print(user3.age)
print(f"bitrhday {user3.birthday()}th , {user3.full_name()}")
print(user3.age)
