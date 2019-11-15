# Lambda is used when the function not use more than one time
# Lambda function has no name so its called the anonymous function
# No Return Keyword use because it is automatically return value


# Example 1 :

# def square(num):
#     print(num ** 2)
#
# square(4);
#
# # Using The Lambda
#
# square_lambda = lambda num : num ** 2;
# print(square_lambda(27))




# Example 2 :

def fullname(fname,lname):
    print(f"{fname} {lname}");

fullname("Hiten","Sidapara")

# Using Lambda

fullname_lambda = lambda fname,lname: f"{fname} {lname}"

print(fullname("Om","Khunt"))



# Find The Name oOf The Functions

print(fullname.__name__);
print(fullname_lambda.__name__);  #lambda has no name so its called the anonymous function
