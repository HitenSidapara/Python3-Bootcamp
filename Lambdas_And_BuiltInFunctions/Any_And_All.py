# All : it return true or false value if all the value are true then return true else retuen
# false

# numbers = [0,1,2,3,4];
# #  because the 0 is false
# print(all(numbers))
#
#
# numbers = [1,2,3,4,5,6];
# print(all(numbers))



# Find All The Number Is Even

# numbers = list(range(2,11,2));
# # print(numbers) even number list
#
#
# print(all([num%2 == 0 for num in numbers]))
#
#
# # create the odd number list
#
# odd_number = list(range(1,11,2))
# print(all([num%2 == 0 for num in odd_number]))




#####################################################################################

# Any is return true if any one return true

# numbers = [0,1,2,3,4,5];
# # 0 is flase but other value is true so it return true
# print(any(numbers));



number_list = list(range(1,11));

print(any([num%2==0 for num in number_list]));

another_number_list = list(range(1,11,2));
print(any([num%2==0 for num in another_number_list]));