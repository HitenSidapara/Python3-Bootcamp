
def be_polite(func):
    def wrapper():
        print("Hello, Welcome to the decorators")
        func()
        print("Bye, To the Decorators")
    return wrapper()

@be_polite
def greet():
    print("My name Is Colt")

@be_polite
def rage():
    print("No One Hate")


try:
    greet()
    rage()
except TypeError:
    pass

# greet = be_polite(greet)
# rage  = be_polite(rage)
