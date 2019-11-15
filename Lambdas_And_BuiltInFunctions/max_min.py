# max Built in method

print(max([1,2,3,4,5,6,7,8,9,99]));
print(min([1,2,3,4,5,6,7,8,9,99]));

print(max('a','b','c','e','z'));
print(min('a','b','c','e','z'));

print(max("helloworld!"));
print(min("helloworld!"));

print(max((1,2,3,99,88,65,2)));
print(min((1,2,3,99,88,65,2)));

names = ["hiten","raj","akshay","kaushik","jay","om","prashant"];

print(max(names,key=lambda name : len(name)));
print(min(names,key=lambda name : len(name)));



# Example :

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# min playcount song name

print(min(songs,key= lambda song: song["playcount"]));
print(min(songs,key= lambda song: song["playcount"])["title"]);

# max playcont song name

print(max(songs,key= lambda song: song["playcount"]));

print(max(songs,key= lambda song: song["playcount"])["title"]);
