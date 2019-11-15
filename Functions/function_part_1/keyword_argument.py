# firstname="om" and lastname="khunt" is called the default parameter

def fullname(firstname="om",lastname="khunt"):
    print(f"your full name is {firstname} {lastname}")

fullname();
fullname(lastname="Sidapara",firstname="Hiten"); #it's  called the keyword argument
fullname(firstname="Aarvee",lastname="Khunt");