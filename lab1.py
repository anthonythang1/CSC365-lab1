import sys
import pandas as pd

try:
			## read txt file and give column names for organization
	df = pd.read_csv('students.txt', header=None, names = ['StLastName', 'StFirstName', 'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])

	print(df)

	if df.shape[1] != 8:
		print("Error: File has incorrect format")

except FileNotFoundError:
	print("Error: file couldn't be found")



while True:
	try:
		command = input("Enter Command: ")
## S Case - R4 & R5
		if command == "S":
	## R2
			val1 = input("Enter Student Last Name: ")
			opt = input("Enter 'B' to receive bus info or press enter to disregard: ")
				## [df[x] == val] checks if val and the data are the same, returns T/F
				## df[df[x] == val] returns the True expressions
			matches = df[df['StLastName'] == val1] 	
			if opt == "B":
				print(matches[['StLastName', 'StFirstName', 'Bus']])
			else:
				## prints the matched data corresponding to correct input
				print(matches[['StFirstName', 'StLastName', 'Grade', 'Classroom', 'TLastName', 'TFirstName']])


## T Case - R6
		elif command == "T":
			val1 = input("Enter Teacher Last Name: ")
			matches = df[df['TLastName'] == val1]
			print(matches[['StLastName', 'StFirstName']])


## G Case - R7 & R9
		elif command == "G":
			val1 = int(input("Enter your grade: "))
			opt = input("Enter option: 'H' for highest or 'L' for lowest")
			
			matches = df[df['Grade'] == val1]

			if opt == "H":
				high = matches[matches['GPA'] == matches['GPA'].max()]
				print(high[['StFirstName', 'StLastName', 'GPA', 'TLastName', 'Bus']])
			elif opt == "L":
				low = matches[matches['GPA'] == matches['GPA'].min()] 
				print(low[['StFirstName', 'StLastName', 'GPA', 'TLastName', 'Bus']])
			else:
				print(matches[['StLastName', 'StFirstName']])

## B Case - R8
		elif command == "B":
			val1 = int(input("Enter Bus Number: "))
			matches = df[df['Bus'] == val1]
			print(matches[['StLastName', 'StFirstName']])


## A Case - R10
		elif command == "A":
			val1 = int(input("Enter your  Grade: "))
			matches = df[df['Grade'] == val1]
			average = matches['GPA'].mean()
	
			print(f"Average GPA of Grade {val1} is {average:.2f}")


## I Case - R11
		elif command == "I":
    			grade_counts = df['Grade'].value_counts().sort_index()  # Get counts of each grade, sorted by grade
    			for grade, count in grade_counts.items():  # Iterate over the grades and counts
        			print(f"{grade}: {count}")



## Q Case - R12
		elif command == "Q":
			print("K. Thanks.")
			sys.exit()

	except Exception as e:
		print(f"Unexpected Error: {e}")




## CSC 365
## Lab 1-a test suite
## TC - 1
## Test requirements: R6
## Command T:
## input: HAMER
## expected output: StFirst & Last

## TC - 2
## R6
## Command T:
## input: HUNGER
## Expected output: error

## TC - 3:
## R7 & R9
## Command G:
## input: Valid Grade, option H
## Expected output: Student detail of highest GPA

## TC - 4:
## R7 & R9
## Command G:
## input: Valid Grade, no H/L
## Expected output: List of students in that grade

## TC - 6:
## R8
## Command B:
## input: Invalid bus number
## Expected output: Empty/error

## TC - 9:
## R10
## Command A:
## input: Invalid grade
## Expected output: error

## TC - 10:
## R11
## Command I:
## Expected output: List of grades and student count

## TC - 11:
## R12
## Command Q:
## Expected output: terminate
