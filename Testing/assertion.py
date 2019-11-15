# Example 1 :

# def positive_number(x,y):
#     assert x>0 and y>0 ,"Not A positive Number"
#     return x+y
#
# print(positive_number(10,2))
# print(positive_number(-10,-2))



# Example 2 :

def junk_food(food):
    assert food in ["pizza","ice-cream","candy","butter"],"Only Allowed The Junk Food"
    return f"Eating Food is {food}"

food = input("Enter The Food Name")
print(junk_food(food))


# if the d=file suould be run in the optimized mod then the assert are not work
# python3 -O assertion.py  use the -O flage so optimize the code