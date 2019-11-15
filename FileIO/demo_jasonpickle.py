import jsonpickle

class Man:
    def __init__(self,name,age,city):
        self.name = name
        self.age  = age
        self.city = city

    def __repr__(self):
        return f"{self.name} age is {self.age} and lives in {self.city}"


# hiten = Man("Hiten Sidapara",19,"Junagadh")
# print(hiten)


# with open("MAN.jason","w") as file:
#     data_encode = jsonpickle.encode(hiten)
#     file.write(data_encode)


# with open("MAN.jason","r") as file:
#     data = file.read()
#     data_decode = jsonpickle.decode(data)
#     print(data_decode)