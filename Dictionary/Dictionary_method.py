# Dictionary Method :

# clear method : remove all the key and value pair

# inforamation = dict(name="Hiten",hobby="Learning Language in computer",fav_number = 27,honest=True);
# print(inforamation);

# inforamation.clear();
# print(inforamation);



# Copy Method :


# a = {"name":"Om","age":2,"hobby":"playing cricket"};
# print(a);
# b= a.copy();
# print(b);
# print(a==b);
# print(a is b);


# a = [1,2,3,4];
# b=a.copy();
# print(a);
# print(b);
# print(a==b);
# print(a is b);




# From Keys Method : used for the default value

# new_dict = {}.fromkeys([]);
# print(new_dict);
# new_dict=new_dict.fromkeys(["name","email","phone_number","password"],"unknown");
# print(new_dict);


# Iterate the String

# another_dict = dict.fromkeys("Hiten","unknown");
# print(another_dict);

# Iterate The String

# numbers  =  dict.fromkeys(range(1,5),"Unknown");
# print(numbers);


# result = 1 in numbers;
# print(result);



# Get Method :


# inforamation = dict(name="Hiten",hobby="Learning Language in computer",fav_number = 27,honest=True);
# print(inforamation);


# result = inforamation.get("name");
# print(result);

    # If The Value Not Present In The Dictionary Then return The None Value.

# result = inforamation.get("study");
# print(result);



# POP Method :
# This Method Takes One Argument pass As The Key


# inforamation = dict(name="Hiten",hobby="Learning Language in computer",fav_number = 27,honest=True);
# print(inforamation);
#
#
# var =  inforamation.pop("name");
# print(var);
# print(inforamation);
#     #Gives the error if the key is not avaibale in the dictionary
# var =  inforamation.pop("abc");
# print(var);
# print(inforamation);




# Popitem Method : last data of dictionary is remove.

# inforamation = dict(name="Hiten",hobby="Learning Language in computer",fav_number = 27,honest=True);
# print(inforamation);
#
#
# var  = inforamation.popitem();
# print(var);
# print(inforamation);




# Update Method :  This method is used to the update the list from the another list
# This method not remove the list data


# first = dict(name = "Hiten",email="@gmail.com",phoneNumber = "333333333");
# second = {};
# print(first);
# print(second);
#
# second.update(first);
#
# print(first);
# print(second);
#
# second["name"]="Om";
#
# print(second);
#
# second.update(first);
#
# print(first);
# print(second);
#
#         #Does't Remove Any Item In The List
#
# second.update({});
# print(second);