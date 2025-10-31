# ============================================================
# ShadowFox Python Development Internship - Task 1 (Beginner)
# Topics Covered: Variables | Numbers | Lists | If Conditions | For Loops
# Author: [shreyas srivastava]
# ============================================================


# 1️⃣ VARIABLES

print("\n----- Task 1: VARIABLES -----")

# 1. Value of π and its data type
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# 2. Testing reserved keyword usage
print("\n--- Attempting to use 'for' as variable name ---")
print("Code: for = 4")
print("Result: SyntaxError - 'for' is a reserved keyword in Python")
print("Reason: Reserved keywords like 'for', 'if', 'while', etc. cannot be used as variable names")
print("They are part of Python's syntax and have special meanings.")

# 3. Simple Interest Calculation
print("\n--- Simple Interest Calculator ---")
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in years: "))
simple_interest = (P * R * T) / 100
print(f"Simple Interest for {T} years is: {simple_interest}")




# 2️⃣ NUMBERS


print("\n----- Task 2: NUMBERS -----")

# 1. Using format function
def format_number(num, format_type):
    return format(num, format_type)

result = format_number(145, 'o')
print(f"Number: 145")
print(f"Format type: 'o' (octal)")
print(f"Formatted result: {result}")
print("Representation: Octal (base-8) number system")

# 2. Pond area and total water
print("\n--- Circular Pond Water Calculation ---")
radius = 84  # meters
pi_value = 3.14
area = pi_value * radius * radius
print(f"Radius of pond: {radius} meters")
print(f"Area of pond: {area} square meters")

# Bonus: Total water calculation
water_per_sqm = 1.4  # liters
total_water = area * water_per_sqm
print(f"Total water in pond: {int(total_water)} liters")

# 3. Speed in m/s
print("\n--- Speed Calculator ---")
distance = 490  # meters
time_minutes = 7  # minutes
time_seconds = time_minutes * 60  # convert to seconds
speed = distance / time_seconds
print(f"Distance: {distance} meters")
print(f"Time: {time_minutes} minutes ({time_seconds} seconds)")
print(f"Speed: {int(speed)} meters/second")




# 3️⃣ LISTS


print("\n----- Task 3: LISTS -----")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("1. Original Justice League:", justice_league)
print(f"   Number of members: {len(justice_league)}")

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("\n2. After Batman recruited Batgirl & Nightwing:", justice_league)

# 3. Move Wonder Woman to start (make her leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman is now the leader:", justice_league)

# 4. Separate Aquaman and Flash
print("\n4. Separating Aquaman and Flash...")
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Insert Green Lantern between them
if abs(flash_index - aquaman_index) == 1:
    # They are adjacent
    insert_position = max(aquaman_index, flash_index)
    justice_league.insert(insert_position, "Green Lantern")
else:
    # Insert between them
    if flash_index > aquaman_index:
        justice_league.insert(flash_index, "Green Lantern")
    else:
        justice_league.insert(aquaman_index, "Green Lantern")

print("   After separation:", justice_league)

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New team assembled by Superman:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("\n6. Alphabetically sorted Justice League:", justice_league)
print(f"   New leader (at index 0): {justice_league[0]}")
print("   BONUS: The new leader is Cyborg!")






# 4️⃣ IF CONDITIONS


print("\n----- Task 4: IF CONDITIONS -----")

# 1. BMI Calculator
print("\n--- BMI Calculator ---")
height = float(input("Enter height (in meters): "))
weight = float(input("Enter weight (in kilograms): "))
bmi = weight / (height ** 2)

if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"

print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")

# 2. City → Country Checker
print("\n--- City to Country Finder ---")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ").title()

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print("City not found in database")

# 3. Check if two cities are in same country
print("\n--- Same Country Checker ---")
city1 = input("Enter the first city: ").title()
city2 = input("Enter the second city: ").title()

# Find country for city1
country1 = None
if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"

# Find country for city2
country2 = None
if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"

# Compare countries
if country1 is None or country2 is None:
    print("One or both cities not found in database")
elif country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")





# 5️⃣ FOR LOOP

print("\n----- Task 5: FOR LOOP -----")

import random

# 1. Dice Rolling Simulation
print("\n--- Dice Rolling Simulation ---")
num_rolls = 20  # At least 20 rolls
six_count = 0
one_count = 0
double_six_count = 0
previous_roll = 0

print(f"Rolling a six-sided die {num_rolls} times...\n")

for i in range(num_rolls):
    current_roll = random.randint(1, 6)
    print(f"Roll {i+1}: {current_roll}")
    
    if current_roll == 6:
        six_count += 1
        if previous_roll == 6:
            double_six_count += 1
    
    if current_roll == 1:
        one_count += 1
    
    previous_roll = current_roll

print(f"\n--- Statistics ---")
print(f"Rolled a 6: {six_count} times")
print(f"Rolled a 1: {one_count} times")
print(f"Rolled two 6s in a row: {double_six_count} times")

# 2. Workout Routine - 100 Jumping Jacks
print("\n--- Workout Routine: 100 Jumping Jacks ---")
print("You need to complete 100 jumping jacks (10 per set)\n")

total_jacks = 100
jacks_per_set = 10
completed = 0

for set_num in range(1, 11):
    print(f"Set {set_num}: Perform {jacks_per_set} jumping jacks")
    input("Press Enter when done...")
    completed += jacks_per_set
    
    # Check if workout is complete
    if completed == total_jacks:
        print("\n🎉 Congratulations! You completed the full workout of 100 jumping jacks!")
        break
    
    # Ask if tired
    tired = input("Are you tired? (yes/no): ").lower()
    
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ['yes', 'y']:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jacks - completed
            print(f"\n{remaining} jumping jacks remaining. Keep going!\n")
    else:
        remaining = total_jacks - completed
        print(f"\n{remaining} jumping jacks remaining. Keep going!\n")

print("\n" + "="*60)
print("All tasks completed successfully!")
print("="*60)