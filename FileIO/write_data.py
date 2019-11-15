# Passing the "w" as the Write parameter

# with open("story.txt","w") as f:
#     f.write("This is the story about the python language")


#passing The  "a" Append Mode

# with open("new.txt","a") as f:
#     f.write("Hey I am Hear")


# Passing the r+mode read And Write

with open("story.txt","r+") as f:
    print(f.read())
    print(f.write("This is the somethig new story"))
    f.seek(0)
    print(f.write(":)"))
    print(f.write("\n :("))