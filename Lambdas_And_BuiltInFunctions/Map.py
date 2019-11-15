# Map is The Built in function that accepts the two argument and iterate the (list,dictionary etc)


number = list(range(1,6));

# Exercise :
# Double Value Of The Each Number

double_value = map(lambda num:num*2,number)

# Gives the map object
#
# print(double_value);
# <map object at 0x7ff6397bca58>


print(list(double_value));


# Another Way :

def double(number):
    return number*2;

double_value1 = list(map(double,number));
print(double_value1);


# another way : List Comprehension

[print(num*2) for num in number];





# Another Eample

name = [
    {"fname":"hiten","lname":"Sidapara"},
    {"fname":"om","lname":"Khunt"},
    {"fname": "aarvee", "lname": "Khunt"},
]

upperCase = list(map(lambda name:name["fname"].upper(),name))
print(upperCase);