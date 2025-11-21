## Author: Minnie Nguyen u3260265
## Date created: 29 October 2023
## Date last changed: 3 November 2023
## This program calculates Total Daily Energy Expenditure 
## Input: age,height,weight,gender,exercise level, Output: TDEE calculation

import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu

## Function to calculate Total Daily Energy Expenditure (TDEE)
def calculate_tdee(age, height, weight, gender, exercise_level):
    if gender == "Male":
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    if exercise_level == "No Exercise":
        tdee = bmr * 1.2
    elif exercise_level == "Light Exercise (1-3 times a week)":
        tdee = bmr * 1.375
    elif exercise_level == "Normal Exercise (4-5 times a week)":
        tdee = bmr * 1.55
    elif exercise_level == "Hard Exercise (6-7 times a week)":
        tdee = bmr * 1.725
    elif exercise_level == "Extreme Exercise (harsh intensity)":
        tdee = bmr * 1.9

    return tdee

## Function to update the TDEE label based on user input
def update_tdee_label():
    age = int(age_entry.get())
    height = int(height_entry.get())
    weight = int(weight_entry.get())
    gender = gender_var.get()
    exercise_level = exercise_var.get()

    tdee = calculate_tdee(age, height, weight, gender, exercise_level)

    tdee_label.config(text=f"TDEE: {tdee:.2f} calories")

## Function to quit the application
def quit_application():
    root.destroy()  ## Properly close the program

## Function to create the GUI
def create_gui():
    global root, age_entry, height_entry, weight_entry, gender_var, exercise_var, tdee_label

    root = tk.Tk()
    root.title("TDEE Calculator")
    root.configure(bg="#E5E4E2")

    ## Introduction Label
    intro_label = Label(root, text="Welcome to the TDEE Calculator!\nCalculate your Total Daily Energy Expenditure.")
    intro_label.grid(row=0, columnspan=2)

    ## Labels for user input fields
    Label(root, text="Age:").grid(row=1, column=0)
    Label(root, text="Height (cm):").grid(row=2, column=0)
    Label(root, text="Weight (kg):").grid(row=3, column=0)
    Label(root, text="Gender:").grid(row=4, column=0)
    Label(root, text="Exercise Level:").grid(row=5, column=0)

    ## Entry Widgets for user input
    age_entry = Entry(root)
    height_entry = Entry(root)
    weight_entry = Entry(root)

    age_entry.grid(row=1, column=1)
    height_entry.grid(row=2, column=1)
    weight_entry.grid(row=3, column=1)

    ## Gender Dropdown
    gender_var = StringVar(root)
    gender_var.set("Male")
    gender_menu = OptionMenu(root, gender_var, "Male", "Female")
    gender_menu.grid(row=4, column=1)

    ## Exercise Level Dropdown
    exercise_var = StringVar(root)
    exercise_var.set("No Exercise")
    exercise_menu = OptionMenu(
        root,
        exercise_var,
        "No Exercise",
        "Light Exercise (1-3 times a week)",
        "Normal Exercise (4-5 times a week)",
        "Hard Exercise (6-7 times a week)",
        "Extreme Exercise (harsh intensity)"
    )
    exercise_menu.grid(row=5, column=1)

    ## Calculate Button
    calculate_button = Button(root, text="Calculate TDEE", command=update_tdee_label)
    calculate_button.grid(row=6, columnspan=2)

    ## Quit Button
    quit_button = Button(root, text="Quit", command=quit_application)
    quit_button.grid(row=8, columnspan=2)

    ## Output Label to display TDEE result
    tdee_label = Label(root, text="")
    tdee_label.grid(row=7, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
