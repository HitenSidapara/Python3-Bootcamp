from csv import reader, writer

with open("info.csv","w") as file:
    write_data = writer(file)
    write_data.writerow(["name","age","city"])
    write_data.writerow(["Hiten","19","valasimdi"])
    write_data.writerow(["Raj","18","vadal"])
    write_data.writerow(["Akshay","20","Privad"])