password = input("Enter your password:  ")
length = len(password)

if length < 6:
	print(" Your password is too short, try again")
	
if length > 20:
	print(" Your password is too long, try again")

if (length >=6) & (length <= 20):
	print('*' * length)
