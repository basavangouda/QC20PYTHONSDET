#Step 1: Connect to the SQl Server
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user='root'
#     ,password="Password")
# print(mydb)

#Step 2 Create Databse
#mycursor=mydb.cursor()
# mycursor.execute("create database qc20python")

#Step 3 : Create Table
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user='root'
#     ,password="Password",
#     database='qc20python'
# )
#
# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE TRAINING(name VARCHAR(255), Address VARCHAR(255))")

#step4 Check whether table is created or Not
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user='root'
#     ,password="Password",
#     database='qc20python'
# )
#
# mycursor=mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)

#Step 5 Create Primary key (If table exists we can alter the table)
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root'
    , password="Password",
    database='qc20python'
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE CUSTOMER (id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255), ADDRESS VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(type(i))
    print(i)

#Alter the table
mycursor.execute("ALTER TABLE TRAINING ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
