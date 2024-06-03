# Create a program to calculate the BMI (Body Mass Index)
# BMI = weight(kg) / (height(m) * height(m))

weight = float(input("Enter your weight(kg) here: "))
height = float(input("Enter your height(m)  here: "))

bmi = weight / (height ** 2)

print(f"Your body mass index is: {bmi:.2f}")
if bmi < 18.5:
    print("- Underwwight!")
elif 18.5 <= bmi < 25:
    print("- Normal weight!")
elif 25 <= bmi < 30:
    print("- Overweight!")
else:
    print("- Obese!")