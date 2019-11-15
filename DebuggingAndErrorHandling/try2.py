# try
# except
# else
# finally


# while True:
#     try:
#         number = int(input("Enter Number : "))
#     except ValueError as err:
#         print(err)
#     else:
#         print("yeah, you are enter the number");
#         break;
#     finally:
#         print("Finally Block Always Execute");


# Example :

def devide(a, b):
    try:
        result = a / b;
    except ZeroDivisionError:
        print("Don't Devided By Zero");
    except TypeError:
        print("a and b must be ints or floats")
    else:
        print(f"{a}/{b} result is {result}")


devide(1, 2)
devide(1, 0)
devide(1, 'a')
