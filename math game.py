import tkinter as tk
from tkinter import messagebox

# Function definitions
def addition():
    messagebox.showinfo("Addition", "Addition function called")

def subtraction():
    messagebox.showinfo("Subtraction", "Subtraction function called")

def multiplication():
    messagebox.showinfo("Multiplication", "Multiplication function called")

# Function to start the game
def start_game():
    window = tk.Tk()
    window.title("Math Practice Game")
    window.geometry("1000x900")

    tk.Label(window, text="Welcome to the Math Practice Game!", font=("Arial", 12)).pack(pady=10)
    
    tk.Button(window, text="Addition", command=addition, width=20).pack(pady=5)
    tk.Button(window, text="Subtraction", command=subtraction, width=20).pack(pady=5)
    tk.Button(window, text="Multiplication", command=multiplication, width=20).pack(pady=5)
    
    window.mainloop()

# Call the start_game function to run the game
start_game()





def addition():
    # Code for addition practice
    print("Addition function called")

def subtraction():
    # Code for subtraction practice
    print("Subtraction function called")

def multiplication():
    # Code for multiplication practice
    print("Multiplication function called")

def start_game():
    print("\nWelcome to math practice.")
    print("here you can practice your addition, subtraction, and multiplication skills")
    print("which would you like to do?")
    print("A - addition")
    print("B - subtraction")
    print("C - Multiplication")
    print("D - Exit game\n")

    choice = input("> ")

    if choice == "A":
        addition()
    elif choice == "B":
        subtraction()
    elif choice == "C":
        multiplication()
    elif choice == "D":
        return None
    else:
        print("that's not one of the choices! Try again.\n")
        start_game()            