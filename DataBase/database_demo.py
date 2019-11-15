import pymysql;

db = pymysql.connect("localhost","root","","python")

cursor = db.cursor();


# Select data into the database


# sql = "select * from user";
#
# cursor.execute(sql)
#
#
# result = cursor.fetchall()
#
# print(result)
#
# for data in result:
#     for item in data:
#         print(item)


# Insert data into database

name = input("Enter The User Name : ")
email = input("Enter The User Email : ")
password = input("Enter The User Password : ")



# sql = "insert into user(name,email,password) values('jay','jay@gmail.com','1911999')"

try:
    cursor.execute(sql);
    db.commit();
except:
    db.rollback()


db.close()