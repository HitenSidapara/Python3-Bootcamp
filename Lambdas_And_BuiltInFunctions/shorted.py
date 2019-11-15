# Sorted method sort the numbers

# numbers = [1,4,3,6,9,7,5,3,4,9,62,45,22,56];
# print(numbers);
# print(sorted(numbers));
# print(sorted(numbers,reverse=True));



# Example 1 :

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# Sorted data according to the username

print(sorted(users,key=lambda users : users["username"]))

# sorted data according to the tweet length

print(sorted(users,key=lambda users : len(users["tweets"])));

# sorted most tweets

print(sorted(users,key=lambda users : len(users["tweets"]),reverse=True));



# ANOTHER EXAMPLE DATA SET==================================

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]


print(sorted(songs,key=lambda songs : songs["playcount"],reverse=True));