height = input("Enter your height in meters: ")
weight = input("Enter your height in weight: ")
bmi = float(weight) / float(height) ** 2

print(f"Your bmi is {bmi}")
if bmi < 18.50:
    print("You're underweight")
elif bmi > 25:
    print("You're overweight")
else:
    print("You're in a normal level")