import csv

# Simple Way TO read csv File

# with open("junagadh.csv") as file:
#     print(file.read())


# Example 2 ; Using The reader : it return the list


# with open("junagadh.csv") as file:
#     data = csv.reader(file)
#     # print(data)
#     print(file.__next__())
#     for dataset in data:
#         # if dataset[3] == "VADASIMDI":
#           if dataset[2] == "JUNAGADH":
#             print(dataset)




#Example 3 : dictreader : it return th rdict representation


# with open("junagadh.csv") as file:
#     data = csv.DictReader(file)
#     # print(data)
#     for dataset in data:
#         if dataset["BlockName"] == "JUNAGADH" and dataset["GramPanchayatName"] == "VADASIMDI":
#              print(dataset)