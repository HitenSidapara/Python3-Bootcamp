# Function args in another function



# def sum(n,func):
#     total = 0
#     for num in range(n):
#         total += func(num)
#     return total
# def square(x):
#     return (x*x)
# def cube(x):
#     return (x*x*x)
#
#
# print(sum(5,square))
# print(sum(3,cube))





# nested function

from random import choice

# def greet(person):
#     def mood():
#         current_mod = choice(["Hello There","go where","I Love you"])
#         return current_mod
#
#     result = f"{person}  {mood()}"
#     return result
#
# print(greet("Hiten"))


def greet(person):
    def mood():
        current_mod = choice(["Hello There","go where","I Love you"])
        result = f"{person}  {current_mod}"
        return result

    return mood()

print(greet("Hiten"))