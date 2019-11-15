f = open("demo.txt")

# print(f)
# print(f.name)
# help(f)

# print("First Time Read The File")
# print(f.read())
# print("Second Time Read File")
# f.seek(0)
# print(f.read())


# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())


# Gives The List Of the lines where it break
# print(f.readlines())


print(f.closed)
f.close()
print(f.closed)