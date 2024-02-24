
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '8606369881'

	)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE crmDB")

print("All Done!")

