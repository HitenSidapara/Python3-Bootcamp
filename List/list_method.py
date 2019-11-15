#  Append Method :
# this method is used to the append the data last of the list.
# in this method we can add the one item at a time


# numbers = [1,2,3,4];
#
# numbers.append(5);
# print(numbers);
# numbers.append([4,5])  # consider as the single item
# print(numbers);




# Extend Method:
# this method is used to the data add to the last of the index in list
# in extend method we can add the number of the data at the last of the list



# numbers = [1,2,3,4,5];
# numbers.extend([6]);
# print(numbers)
# numbers.extend([7,8,9,10]);
# print(numbers);




# insert method:
# This method is used for the number add at the any position of the list


# numbers = [1,2,5,6,7,8,9,10];
#
# print(numbers);
# numbers.insert(2,3);
# print(numbers);
# numbers.insert(3,4);
# print(numbers);
#
#
# # not work
# numbers.insert(-1,11);
# print(numbers);
#
# # is work
#
# numbers.insert(len(numbers),11);
# print(numbers);






# clear method :
# this method is used to clear all the list


# numbers = list(range(1,10));
# print(numbers);
# numbers.clear();
# print(numbers);




# pop mthod:
# this method is used to the remove the particular element in list using the index
# by default it remove the last element of the list




# numbers = list(range(1,5));
# print(numbers);
# numbers.pop();
# print(numbers);
# numbers.pop(0);
# print(numbers);







# remove method :
# this method used to the remove the data in list using the list data value
# if the value is correct then delete this value else throws exception



# shop_items = ["shoes","cloths","mobile","laptop"];
# print(shop_items);
# shop_items.remove("shoes");
# print(shop_items);
# shop_items.remove("mobile");
# print(shop_items);





# index method :

# friends = ["Raj","Akshay","jay","Parshant","Amit","Kaushik","Raj","Akshay",
#            "Raj","Jay","Akshay","Prashant","Raj","Hiten"];


# print(friends);
# print(friends.index("Amit"));
# print(friends.index("Raj"));
# print(friends.index("Raj",2));




# Count Method

# print(friends);
# print(friends.count("Raj"));
# print(friends.count("Ravi"));
# print(friends.count("Akshay"));




# reverse method :


# numbers = list(range(1,6));
# print(numbers);
#
# numbers.reverse();
#
# print(numbers);
#
#
#
#
# print(friends);
# friends.reverse();
# print(friends);




# sort method :


# numbers = [9,8,7,6,5,4,3,2,1,0];
# print(numbers);
# numbers.sort();
# print(numbers);






# Join method:
# this method is used to the join the list to the string.

# friends = ["Hiten","Akshay","Raj","Jay","Prashant"];

# print(friends);

# friends_string = " is my friend \n".join(friends);

# print(friends_string);