print(""" Welcome 
This application is a simple mathematics application
It ask you to enter your name
Then also ask for year of Birth.
It then calculate your age.
And give you the questions
""")
name_entered = input("Enter your name: ")
print("Your name is ", name_entered)
print(" ")
if ("A" in name_entered):
	print("There is a letter A in your name")
else:
	print("There is no letter A in", name_entered)
print(" ")

print("The type of this data is: ", type (name_entered))
print(" ")

year_entered = int(input("Enter your year of birth:  "))
year = 2023
age = year - year_entered
print("You are : ", age,  "years old")
print(" ")
print("The type of this data is: ", type (age))
print(" ")

location = input("Enter your address:")
print("The address you entered is: ", location)
print(" ")
print("The type of this data is: ", type (location))
print(" ")

x = 1
while (x  <= 8):
	import random
	random_number = random.randrange(50, 100)
	random1_number = random.randrange(0, 30)

	print("Checkpoint: ", random_number, "-", random1_number)
	user_answer = int (input("What is the answer of the above: "))
	real_answer = random_number - random1_number
	print(" ")

	if (user_answer == real_answer): 
		print("Your answer is correct")
	else: 
		print("Your answer is not correct")
	
	x = x + 1
print(" ")
	

	








