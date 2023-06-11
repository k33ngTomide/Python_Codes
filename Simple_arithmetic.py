first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

sum = first_number + second_number + third_number
average = sum / 3
product = first_number * second_number * third_number

smallest = first_number
if second_number < first_number: 
	smallest = second_number
if third_number < second_number:
	smallest = third_number

largest = first_number
if second_number > first_number: 
	largest = second_number
if third_number > second_number:
	largest = third_number

print(" ")
print("sum is: ", sum)
print("Average is: ", average)
print("Product is: ", product)
print("The smallest number is : ", smallest)
print("The largest number is : ", largest)
