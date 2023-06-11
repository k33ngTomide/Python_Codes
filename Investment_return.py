amount_invested = int(input("Enter the original amount invested: $"))
rate = int(input("Enter ther annual rate of return: "))

number_of_years = 10
amount_of_deposit = amount_invested*((1 + (rate/100))**number_of_years)

number_of_years = 20
amount_of_deposit1 = amount_invested*((1 + (rate/100))**number_of_years)

number_of_years = 30
amount_of_deposit2 = amount_invested*((1 + (rate/100))**number_of_years)

print("The amount of deposit at the end of 10 years: $",  amount_of_deposit, "\n")
print("The amount of deposit at the end of 20 years: $",  amount_of_deposit1, "\n")
print("The amount of deposit at the end of 30 years: $",  amount_of_deposit2, "\n")
