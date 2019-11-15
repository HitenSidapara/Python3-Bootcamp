# 1st Way To Create The Dictionary

information = {
    "name":"Hiten Sidapara",
    "age":20,
    "study":"Computer Engineering.",
    "honest":True
};

# print(information);


# 2nd Way To Create The Dictionary


# information1 = dict(name="Om",age=1.2,study=False,honest=True);

# print(information1);
# print(information1["name"]);
# print(information1["age"]);
# print(information1["study"]);
# print(information1["key"]); throw error if the key is not avaiable in the dictionary




# Data Fetch Using The ForLoop

# for values in information.values():
#     print(values);
#
# for keys  in information.keys():
#     print(keys);

# for keys in information.keys():
#     print(f"{keys} : {information[keys]}");


# Access both the value

# for key,value in information.items():
#     print(f"{key} : {value}");







# Find the Key or value Exist in the dictionary
# by default it search for the key not value.

is_exist = "name" in information;
print(is_exist);

is_exist = "name" in information.keys();
print(is_exist);

is_exist = "Hiten Sidapara" in information.values();
print(is_exist);

is_exist = "Jay Sidapara" in information.values();
print(is_exist);

is_exist =  "hobby" in information.keys();
print(is_exist);

is_exist = "hobby" in information;
print(is_exist);