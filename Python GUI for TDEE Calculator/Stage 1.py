## Author: IIT Group 14
## Date created: 29 October 2023
## Date last changed: 3 November 2023
## This program provides users with a menu containing different choices and also calculates TDEE of the users with their inputs
## Input: age,height,weight,gender,exercise level, Output: TDEE calculation

## Function to calculate TDEE based on age, height, weight, gender, and exercise level
def calculate_tdee(age, height, weight, gender, exercise_level):
    ## Calculate BMR based on gender
    if gender == "Male":
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    ## Define exercise factors
    exercise_factors = {
        "No Exercise": 1.2,
        "Light Exercise (1-3 times a week)": 1.375,
        "Normal Exercise (4-5 times a week)": 1.55,
        "Hard Exercise (6-7 times a week)": 1.725,
        "Extreme Exercise (harsh intensity)": 1.9,
    }
    ## Calculate TDEE using BMR and exercise level
    tdee = bmr * exercise_factors[exercise_level]
    return bmr, tdee

## Function to get user input and calculate TDEE
def calculate_tdee_menu():
    print("TDEE Calculator")
    age = int(input("Enter your age: "))
    height = int(input("Enter your height in centimeters: "))
    weight = int(input("Enter your weight in kilograms: "))
    gender = input("Enter your gender (Male/Female): ")

    ## Define exercise level choices
    exercise_choices = {
        "1": "No Exercise",
        "2": "Light Exercise (1-3 times a week)",
        "3": "Normal Exercise (4-5 times a week)",
        "4": "Hard Exercise (6-7 times a week)",
        "5": "Extreme Exercise (harsh intensity)",
    }

    # Print exercise level options
    print("Choose your exercise level:")
    for key, value in exercise_choices.items():
        print(f"{key}: {value}")

    exercise_choice = input("Enter the number of your exercise level: ")

    if exercise_choice not in exercise_choices:
        print("Invalid choice. Please select a valid exercise level.")
        return

    exercise_level = exercise_choices[exercise_choice]

    bmr, tdee = calculate_tdee(age, height, weight, gender, exercise_level)

    print(f"Your TDEE is: {tdee:.2f} calories")

# Function to enter and display height
def enter_height():
    height = int(input("Enter your height in centimeters: "))
    print(f"Height: {height} cm")

# Function to enter and display weight
def enter_weight():
    weight = int(input("Enter your weight in kilograms: "))
    print(f"Weight: {weight} kg")

# Function to enter and display gender
def enter_gender():
    gender = input("Enter your gender (Male/Female): ")
    print(f"Gender: {gender}")

# Function to enter and display BMR score
def enter_bmr():
    age = int(input("Enter your age: "))
    height = int(input("Enter your height in centimeters: "))
    weight = int(input("Enter your weight in kilograms: "))
    gender = input("Enter your gender (Male/Female): ")
    if gender == "Male":
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    print(f"BMR: {bmr:.2f} calories")

# Function to display program options
def display_program_options():
    print("TDEE Calculation Program:")
    print("A: Display average total daily energy expenditure between the ages of 19 and 22 years")
    print("B: Display normal standard for BMR")
    print("C: Display exercise levels")
    print("D: Calculate your own TDEE")
    print("X: Quit")

# Function to display information for part A
def display_part_A():
    print("Average Total Daily Energy Expenditure:")
    print("Men (calories per day): 3000 kcal")
    print("Women (calories per day): 2100 kcal")

# Function to display information for part B
def display_part_B():
    print("Normal Standard for BMR:")
    print("Male (calories per hour):")
    print("Age 20-29: 39.5")
    print("Age 30-39: 39.5")
    print("Age 40-49: 38.5")
    print("Age 50-59: 37.5")
    print("Age 60-69: 36.5")
    print("Age 70-79: 35.5")
    print("Female (calories per hour):")
    print("Age 20-29: 37.0")
    print("Age 30-39: 36.5")
    print("Age 40-49: 36.5")
    print("Age 50-59: 35.0")
    print("Age 60-69: 34.0")
    print("Age 70-79: 33.0")

# Function to display information for part C
def display_part_C():
    print("Exercise Levels:")
    print("1. No Exercise")
    print("2. Light Exercise (1-3 times a week)")
    print("3. Normal Exercise (4-5 times a week)")
    print("4. Hard Exercise (6-7 times a week)")
    print("5. Extreme Exercise (harsh intensity)")

# Main menu function
def main_menu():
    display_program_options()
    while True:
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            display_part_A()
        elif choice == "B":
            display_part_B()
        elif choice == "C":
            display_part_C()
        elif choice == "D":
            calculate_tdee_menu()
        elif choice == "X":
            print("Thank you for using our program!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main_menu()
