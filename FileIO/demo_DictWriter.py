from csv import DictReader, DictWriter

# with open("physical_data.csv","w") as file:
#     hearder = ["Name","Age","Country","Height"]
#     csv_write = DictWriter(file,fieldnames=hearder)
#     csv_write.writeheader()
#     csv_write.writerow({
#         "Name":"Hiten",
#         "Age":19,
#         "Country":"India",
#         "Height":165
#     })
#     csv_write.writerow({
#         "Name": "Om",
#         "Age": 1.2,
#         "Country": "India",
#         "Height": 65
#     })
#     csv_write.writerow(
#     {
#     "Name": "Akshay",
#     "Age": 20,
#     "Country": "India",
#     "Height": 140
#     })
#     csv_write.writerow(
#     {
#         "Name": "Raj",
#         "Age": 18,
#         "Country": "India",
#         "Height": 175
#     }
#     )




# Exercise 1 : data conver into the inch

# read file is changed so not work

def cm_to_inch(cm):
    return float(cm)*0.393701;


with open("physical_data.csv") as file:
    csv_reader = DictReader(file)
    info =list(csv_reader)
    with open("physical_data.csv","w") as file:
      hearder = ["Name","Age","Country","Height(in)"]
      csv_writer = DictWriter(file,fieldnames=hearder)
      csv_writer.writeheader()
      for row in info:
          csv_writer.writerow({
              "Name": row["Name"],
              "Age": row["Age"],
              "Country": row["Country"],
              "Height(in)": cm_to_inch(row["Height(in)"])
          })