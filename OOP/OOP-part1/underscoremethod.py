# _name    = pure convension in python for the private method
#  __name  = this method is used to when the inheritance _classname__name
# __init__ = when we are override method that time used

class User:
    def __init__(self,fname,lname,age):
        self._fname = fname
        self.__lname = lname
        self.age =age


user1 = User("Hiten","Sidapara",20)

print(f"{user1._fname} {user1._User__lname} {user1.age}")
print(User("Hiten","Sidapara",19)._fname)