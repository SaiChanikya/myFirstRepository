import sqlite3
DATABASE_NAME = "Framework.db"
MENU_FILE = "MenuOfSQLiteOperations.cfg"
tableName = "FRAMEWORK_TABLE"

def printMenu():
	print(open(MENU_FILE).read())

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
cursor.execute("pragma table_info(FRAMEWORK_TABLE)")
listOfFieldNames = cursor.fetchall()
columnNamesList = [columnName[1] for columnName in listOfFieldNames]
fetchColumns = [columnNamesList[counter] for counter in range(1, len(columnNamesList) - 1)]

def patternForUnderline(string):
	for i in string:
		if i == '|':
			print("+", end = "")
		else:
			print("-", end = "" )
	print()

def printAndUnderline(string):
	print(string)
	patternForUnderline(string)

def printTableHeader(string):
	patternForUnderline(string)
	printAndUnderline(string)

def printUpdateMenu():
	print("*******MENU FOR UPDATE********")
	for counter in range(len(fetchColumns)):
		print(str(counter + 1) + ". " + fetchColumns[counter])
	print("******************************")


def insert():
	columnValues = [input("Enter " + columnNamesList[counter] + ": ") for counter in range(len(columnNamesList))]
	placeHolders = ""
	for counter in range(len(columnNamesList)):
		if counter != len(columnNamesList) - 1:
			placeHolders += "?,"
		else:
			placeHolders += "?"	
	try:	
		result = cursor.execute("INSERT INTO " + tableName + " VALUES(" + placeHolders + ")", columnValues).fetchone()
		connection.commit()
		result = cursor.rowcount
		if result == 0:
			print("Record doesn't exist!")
		else:
			print("Record inserted successfully.")
	except Exception as E:
		print("Error!", E)
		connection.rollback()
		print("Insert operation failed!")

def read():
	query = "SELECT * FROM " + tableName + " where " + columnNamesList[-1] + " = 1" 
	records = connection.execute(query)
	try:
		allRecords = cursor.execute(query).fetchall()
		print("Total records are: ", len(allRecords))
		header = "| "
		for columnName in columnNamesList:
			header += columnName.rjust(20, ' ')
			if columnName is columnNamesList[-1]:
				header += " |"
			else:
				header += " | "
		printTableHeader(header)
		for record in allRecords:
			data = "| "
			for counter in range(len(record)):
				data += str(record[counter]).rjust(20, ' ')
				if counter == (len(record) - 1):
					data += " |"
				else:					
					data += " | "		
			printAndUnderline(data)
	except Exception as E:
		print("Error!", E)
		print("Read operation failed!")

def update():
	try:
		primaryKey = input("Enter " + columnNamesList[0] + " to update the record: ")
		printUpdateMenu()
		option = int(input("Enter your option: ")) - 1
		if option > 0 and option <= len(fetchColumns):
			columnValue = input("Enter " + fetchColumns[option] + " to be updated: ")
			cursor.execute("UPDATE " + tableName + " SET " + fetchColumns[option] + " = ? WHERE " + columnNamesList[0] + " = ?", (columnValue, primaryKey))
			connection.commit()	
			result = cursor.rowcount
			if result == 0:
				print("Record doesn't exist!")
			else:
				print("Record updated successfully.")
		else:
			print("You have entered invalid option!")
	except Exception as E: 	
		print("Error!", E)
		connection.rollback()
		print("Update operation failed!")	

def delete():
	try:		
		primaryKey = input("Enter " + columnNamesList[0] + " to delete the record: ")
		cursor.execute("UPDATE " + tableName + " SET " + columnNamesList[-1] + " = ? WHERE " + columnNamesList[0] + " = ?", (0, primaryKey))
		connection.commit()
		result = cursor.rowcount
		if result == 0:
			print("Record doesn't exist!")
		else:
			print("Record deleted successfully.")
	except Exception as E:
		print("Error!", E)
		connection.rollback()
		print("Delete operation failed!")

def exitFromMenu():
	print("Thank you.")
	connection.close()
	exit()

def showMenu():
	try:
		while True:
			printMenu()
			option = int(input("Enter your option: "))
			if option == 1:
				insert()
			elif option == 2:
				read()
			elif option == 3:
				update()
			elif(option == 4):
				delete()
			elif option == 5:
				exitFromMenu()
			else:
				print("Please, Enter valid option!")				
	except Exception as E:
		print("Error!", E)
		print("Show operation failed!")

showMenu()	



		



	