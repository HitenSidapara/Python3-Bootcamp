# Filter Is Used To The shortout some value

# numbers = list(range(1,11));
#
# even_number = list(filter(lambda num:num%2==0,numbers));
#
# print(even_number);





# Exercise 1 :

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]


# Find The Data Which User Have not any tweet

inactive_user = list(filter(lambda userlist:len(userlist["tweets"]) == 0,users))

print(inactive_user);

# Find The Active User
# [],"",0 return the false so the tweet list is not empty the return true so the print this value.


active_user = list(filter(lambda userlist:userlist["tweets"],users))
print(active_user);


# in active user find another way

inactive_user_another = list(filter(lambda userlist:not userlist["tweets"],users))

print(inactive_user_another);




# Combine the list and map

# find the inactive user an convert into the uppercase

username_inactive = list(map(lambda name : name["username"].upper(),
                         filter(lambda user:not user["tweets"],users)));

print(username_inactive);


# Find The Active User in Uppercase

username_active = list(map(lambda name : name["username"].upper(),
                         filter(lambda user: user["tweets"],users)));

print(username_active);