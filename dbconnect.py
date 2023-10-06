import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Yash@123", database="practice")

mycursor = mydb.cursor()

mycursor.execute("select name from student WHERE roll_no=54")

print(mycursor.fetchall())
