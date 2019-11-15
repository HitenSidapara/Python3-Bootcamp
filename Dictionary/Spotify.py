playlist = {
    "title":"2018 Best Songs Collecion",
    "author":"Hiten Sidapara",
    "songs":[
        {"title":"Aankh Marey",
         "artist":["Neha Kakkar"," Mika Singh And Kumar Sanu"],
         "duration":2.10},

        {"title": "Apna Time Aayega",
         "artist": ["Ranveer Singh", "Alia Bhatt"],
         "duration": 3.90},

        {"title": "Tere Bin",
         "artist": ["Rahat Fateh Ali Khan"," Asees Kaur","Tanishk Bagchi"],
         "duration": 2.80}
    ]
};


# for songs in playlist["songs"]:
#     print(songs);

# Exercise 1 :

# total_duration = 0;
# for songs in playlist["songs"]:
#     total_duration+=songs["duration"];
# print(f"Total Duration Is : {total_duration}");



# Fetch all The data of teh palylist


print(playlist);

print(playlist["title"]);
print(playlist["author"])
for songs in playlist["songs"]:
    print(f"name : {songs['title']} \n Author Name : {songs['artist']} \n Duration : {songs['duration']} \n");
print();
