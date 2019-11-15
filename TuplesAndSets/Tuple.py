#Tuple is the ordered collection of the data like the list but the syntax dofference.
# Tuple is the immutable so the we are not change the value of the tuples data


# Create the Tuple


# months = ("january","fabuary","march","april","may");
# print(months);
#
#     # in tuple there are not any insert delete or update method available
#
#
# for month in months:
#     print(month);



# Create the tuple as the dictionary key.


# locations = {
#     (11.09,11.12):"Ahemdabad",
#     (15.17,17.02):"Delhi",
#     (12.09,13.45):"Mumbai"
# };
#
# print(locations);
#
#
# for key,value in locations.items():
#     print(f"{key} {value}");



# Note : The List Is Not Used Any Time For The Dictionary Key


# inforamtion = dict(name="Hiten Sidapara",age=19,study="Computer Engineering");
# print(inforamtion.items());

        # Answer

# dict_items([('name', 'Hiten Sidapara'), ('age', 19), ('study', 'Computer Engineering')])
                #1st Tuple                 # 2nd Tuple    #3rd Tuple





# Print The data using the loop



# months = ("january","fabuary","march","april","may");

# for month in months:
#     print(month);


# i=0;
# while i<len(months):
#     print(months[i]);
#     i+=1;






# Tuple Method :

# 1. Count  Method :

# numbers = (1,2,3,4,5,5,5,4,3,3,2,1,1,1,1);
# print(numbers.count(1));
# print(len(numbers));
# print(numbers.count(5));




# 2 index Method :

# numbers = (1,2,3,4,5,6,7,1,2,3,4,5,6);
#
# print(numbers.index(1));
# print(numbers.index(5));
# print(numbers.index(5,5));



# 3. Slice Method :

# numbers = (1,2,3,4,5,6,7,8,9,10);
#
# print(numbers[1:6]);
#
# numbers_slice = numbers[1:8:2];
# print(numbers_slice);



# set comprehension

# {print(nums*2) for nums in range(1,11)};

# String = "aeiou"
#
# {print(char) for char in String if String =='aeiou'}

# Even Odd Number :

number = {nums**2 if nums%2==0 else nums/2 for nums in range(1,11)}
print(number);