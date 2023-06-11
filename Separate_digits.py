number = int(input("Enter a five digit number: "))

first_digit = (int(number / 10000)) % 10
second_digit = (int(number / 1000)) % 10
third_digit = (int(number / 100)) % 10
fourth_digit = (int(number / 10)) % 10
fifth_digit = (int(number % 10))

print(first_digit,"\t",second_digit, "\t", third_digit, "\t", fourth_digit, "\t", fifth_digit)
