import mysql.connector


conn = mysql.connector.connect(
    user='root', 
    password='', 
    host='localhost', 
    database='db_handwashing'
    )
cursor = conn.cursor()



