# set is the combination of the list and the dictionary because the it has not the key value
# pair or not access by the order

# set is the lighter than the list and the dictionary

# set has not allow the duplicate the value so the set contains the unique value


# Remove the duplicate value :


# s = {1,2,3,4,5,5,5,5,5,5};
# print(s)

# s = set({1,2,3,4,5,6,7,8,1,2,3,4,3,4,3});
# print(s);






# Where the set use
# set is used when the list item check and remove the duplicate value in the list


# combo = [1,2,3,'a',4,'b','c',13.0003,1,2,3,4,1,2,3,'a','b','b'];

# print(len(combo));

# remove the duplicate value :

# print(list(set(combo)));

# calculate the length after the duplicate value remove

# print(len(list(set(combo))));






# Set Method :

# 1.Add

numbers = {1,2,3,4,5,6};
# print(numbers);
# numbers.add(7);
# print(numbers);

# 2.Remove the data

# print(numbers);
# numbers.remove(6)
# print(numbers);

# 3. Copy Method :

# print(numbers);
#
# another_list = numbers.copy();
# print(another_list);
#
# print(numbers == another_list);
# print(numbers is another_list);


# 4. Clear List :

# print(numbers);
# numbers.clear();
# print(numbers);

# 5. set math :

# first_set = {"Hiten","jay","Akshay","Prashant","Raj","Bhavin","Mayank","Akshay"};
# second_list = {"Jitesh","Rushil","Raj","Hiten","Akshay","Rashik","Ashvin"};

# # union using the set math

# print(first_set | second_list);
# print(len(first_set | second_list));

# # intersection using the set math

# print(first_set & second_list);
# print(len(first_set & second_list));