#it represent with the """ """ in the function in python world
# if we are access with the __doc__.

def exponent(number,power=2):
    """exponent(number,power) raise power of the number(default value of the power is 2)"""
    return number ** power

print(exponent(2,3));
print(exponent(3,2));
print(exponent(4));
print(exponent.__doc__);