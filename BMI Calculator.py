def bmi_calculator(height, weight):
    return round((weight / height ** 2), 2)


print("Calculate your BMI!!")

hei = float(input("Height in meters: "))
wei = float(input("Weight in kg: "))

bmi = bmi_calculator(hei, wei)
print("Your BMI is: ", bmi)

if bmi <= 18.5:
    print("Your underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your normal.")
elif 25 < bmi <= 29.29:
    print("Your overweight.")
else:
    print("Your obese.")
