user_age = int(input("Enter your age:  "))

max_heart_rate = 220 - user_age
target_heart_rate1 = (50/100) * max_heart_rate
target_heart_rate2 = (80/100) * max_heart_rate

print("Your maximum heart rate is", max_heart_rate)
print("Your target heart rate ranges between", target_heart_rate1, "-", target_heart_rate2 )


