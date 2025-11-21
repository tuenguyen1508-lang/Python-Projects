## Author: Minnie Nguyen u3260265
## Date created: 29 October 2023
## Date last changed: 1 November 2023
## This program displays data from an external file 
## Input: ID from 1 to 10, choose gender and exercise level. Output: Age, height, weight and TDEE calculation of the ID selected

## Import necessary modules from the tkinter library
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu

## Define a function to read data from a file and store it in a dictionary
def readFile(path):
    loutput = {}
    with open(path, "r") as fs:
        for line in fs:
            cline = line.rstrip().split(",")
            loutput[cline[0]] = [int(x) for x in cline[1:]]
    return loutput

## Define a function to calculate Total Daily Energy Expenditure (TDEE) based on user inputs
def calculate_tdee(age, height, weight, gender, exercise_level):
    ## Calculate the Basal Metabolic Rate (BMR) based on gender
    if gender == "Male":
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    ## Calculate TDEE based on the selected exercise level
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

## Define a function to update the TDEE label when the user provides an ID
def update_tdee_label():
    ## age = int(age_entry.get())
    ## height = int(height_entry.get())
    ## weight = int(weight_entry.get())

    id = str(id_entry.get())
    if id in output.keys():
        age = output[id][0]
        height = output[id][1]
        weight = output[id][2]

        ## Set the age, height, and weight labels based on the retrieved data
        age_entry.set(str(age))
        height_entry.set(str(height))
        weight_entry.set(str(weight))

        gender = gender_var.get()
        exercise_level = exercise_var.get()

        ## Calculate and update the TDEE label with the calculated TDEE value
        tdee = calculate_tdee(age, height, weight, gender, exercise_level)
        tdee_label.config(text=f"TDEE: {tdee:.2f} calories")
    else:
        ## Display a message in the TDEE label if the provided ID is not found
        age_entry.set("")
        height_entry.set("")
        weight_entry.set("")
        tdee_label.config(text=f"Try another ID from 1 to 10")
        
## Define a function to close the application
def quit_application():
    root.destroy()  ## Properly close the program

## Define the main application function
def main():
    global root, age_entry, height_entry, weight_entry, id_entry, gender_var, exercise_var, tdee_label, output
    path = "data.txt"

    ## Read data from the file and store it in the 'output' dictionary
    output = readFile(path)
    ## print(output)
    
    ## Create the main application window using tkinter
    root = tk.Tk()
    root.geometry("350x350")
    root.title("TDEE Calculator")
    root.configure(bg="#E5E4E2")

    ## Introduction Label
    intro_label = Label(root, text="Welcome to the TDEE Calculator!\nCalculate your Total Daily Energy Expenditure.")
    intro_label.grid(row=0, columnspan=2)

    ## Labels
    Label(root, text="Age:").grid(row=1, column=0)
    Label(root, text="Height (cm):").grid(row=2, column=0)
    Label(root, text="Weight (kg):").grid(row=3, column=0)
    Label(root, text="Gender:").grid(row=4, column=0)
    Label(root, text="Exercise Level:").grid(row=5, column=0)

    Label(root, text="ID:").grid(row=6, column=0)

    ## Entry Widgets
    ## age_entry = Entry(root)
    ## height_entry = Entry(root)
    ## weight_entry = Entry(root)
    age_entry = StringVar()
    age_grid = Label(root, textvariable=age_entry)
    height_entry = StringVar()
    height_grid = Label(root, textvariable=height_entry)
    weight_entry = StringVar()
    weight_grid = Label(root, textvariable=weight_entry)

    id_entry = Entry(root)

    age_grid.grid(row=1, column=1)
    height_grid.grid(row=2, column=1)
    weight_grid.grid(row=3, column=1)
    id_entry.grid(row=6, column=1)

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
    calculate_button.grid(row=7, columnspan=2)

    ## Quit Button
    quit_button = Button(root, text="Quit", command=quit_application)
    quit_button.grid(row=9, columnspan=2)

    ## Output Label
    tdee_label = Label(root, text="")
    tdee_label.grid(row=8, columnspan=2)

    ## Start the tkinter main loop to run the application
    root.mainloop()
    
## Check if the script is being run as the main program
if __name__ == "__main__":
    main()
