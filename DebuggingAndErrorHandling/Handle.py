# Handle the error


# name

# Gives us the name error

# now handle this error
#
# try:
#     name
# except NameError as err:
#     print(err);




# Another Example :


def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name":"Hiten"}

print(get(d,"name"));
print(get(d,"city"));
