class User:

    active_user = 0

    @classmethod
    def active_users(cls):
        return f"Active User Is {cls.active_user}"

    def __init__(self,fname,lname,age):
        self.name=lname
        self.lname=lname
        self.age=age
        User.active_user+=1

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def logout(self):
        User.active_user -=1



class Moderators(User):

    active_mod = 0

    @classmethod
    def active_mods(cls):
        return f"Active Moderators is {cls.active_mod}"

    def __init__(self,fname,lname,age,community):
        super().__init__(fname,lname,age)
        self.community = community
        Moderators.active_mod+=1

    def logout(self):
        Moderators.active_mod -=1
        super().logout()



Hiten = Moderators("Hiten","Sidapara","20","Computer")
Akshay = User("Akshay","Padashala","19")
Raj = Moderators("Raj","Chovatiya","23","Web Development")
print(User.active_users())
print(Moderators.active_mods())
Raj.logout()
print(Moderators.active_mods())
print(User.active_users())
Akshay.logout()
print(Moderators.active_mods())
print(User.active_users())