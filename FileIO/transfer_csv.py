from csv import reader,writer

# Oney Way

# with open("info.csv") as file:
#     data = reader(file)
#     data_upper = [ [row.upper() for row in dataset] for dataset in data]
#     for row in data_upper:
#         print(row)
#
# with open("copy_info.csv","w") as file:
#     data = writer(file)
#     for row in data_upper:
#         data.writerow(row)




# Second way

with open("info.csv") as file:
    data = reader(file)
    data_upper = [ [row.upper() for row in dataset] for dataset in data]
    with open("copy_info.csv","w") as file:
        write_data = writer(file)
        for row in data_upper:
            write_data.writerow(row)