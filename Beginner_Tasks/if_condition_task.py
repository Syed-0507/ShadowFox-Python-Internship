# Beginner Task - If Condition

# -----------------------------------
# 1. BMI Category Calculator
# -----------------------------------

print("----- BMI Calculator -----")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# -----------------------------------
# 2. Find the Country of a City
# -----------------------------------

print("\n----- Find Country -----")

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ").strip().title()

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found in the given lists.")


# -----------------------------------
# 3. Check if Two Cities are
#    in the Same Country
# -----------------------------------

print("\n----- Compare Two Cities -----")

city1 = input("Enter the first city: ").strip().title()
city2 = input("Enter the second city: ").strip().title()

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")

elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")

elif city1 in india and city2 in india:
    print("Both cities are in India")

elif (
    city1 not in australia
    and city1 not in uae
    and city1 not in india
) or (
    city2 not in australia
    and city2 not in uae
    and city2 not in india
):
    print("One or both cities are not present in the given lists.")

else:
    print("They don't belong to the same country")