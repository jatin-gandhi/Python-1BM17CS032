import sqlite3 


connection = sqlite3.connect("myTable.db") 


crsr = connection.cursor() 

#Inserting the data  

sql_command = """CREATE TABLE emp (  
staff_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""


crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1983-10-28");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (2, "Gill", "Gates", "M", "1984-10-28");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (3, "Mill", "Gates", "M", "1985-10-28");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO emp VALUES (4, "Sill", "Gates", "M", "1986-10-28");"""
crsr.execute(sql_command) 

connection.commit() 

#Fetching and displaying the data


crsr.execute("SELECT * FROM emp")    
data= crsr.fetchall()   
for tupl in data: 
	print(tupl) 


#Displaying the data of a specific employee

id = int(input("Enter the id"))  
sql_command = ("""SELECT * FROM EMP WHERE STAFF_NUMBER ={};""".format(id))
crsr.execute(sql_command) 
data= crsr.fetchall() 
print(data)  


# Update data

sql_command = ("""UPDATE EMP SET FNAME= 'SAM' WHERE STAFF_NUMBER = {} ;""".format(3))
crsr.execute(sql_command) 
print("Updated")


#Delete data

connection.execute("""DELETE from EMP where fname ='Bill';""") 
connection.commit() 
print ("Total number of rows deleted :", connection.total_changes) 

cursor = connection.execute("SELECT * FROM EMP") 
for row in cursor: 
	print (row) 




connection.close() 
