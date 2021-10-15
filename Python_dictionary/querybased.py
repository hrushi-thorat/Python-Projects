import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

word = input("Enter the word: ")
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result)
else:
    print("Enter the valid string")
