import tkinter as tk
from tkinter import PhotoImage, Scrollbar, Text

root = tk.Tk()
root.title("cool gui")
root.geometry("1500x1000")

label = tk.Label(root, text="Hello everyone, This is my cool first GUI!", bg="Grey")
label.pack()
label = tk.Label(root, text="this is my first real GUI i have ever done, this is pretty much all by myself and i had little to no help when doing this, im very happy with the outcome of it lol")
label.pack()
click_count = 0

def on_button_click():
    global click_count
    click_count += 1
    if click_count <= 3:
        print("Button clicked!")
        new_label = tk.Label(root, text="Congrats, you have clicked my button!")
    else:
        new_label = tk.Label(root, text="ok, chill")
    new_label.pack()

def on_second_button_click():
    global click_count
    click_count += 1
    if click_count <= 4:
        print("Button clicked")
        new_label = tk.Label(root, text="this is the second button, you clicked it.")
    else:
        new_label = tk.Label(root, text="ok chill bro")
    new_label.pack()


button1 = tk.Button(root, text="click me yo!", command=on_button_click)
button1.pack()

button2 = tk.Button(root, text="you can also click me too you know", command=on_second_button_click)
button2.pack()

button1.place(x=300, y=100)
button2.place(x=1150, y=100)

image = PhotoImage(file=r"C:\Users\croix.chada\Pictures\totoro.gif")


image_label = tk.Label(root, image=image)
image_label.pack(side=tk.BOTTOM, pady=10)

text_box = tk.Text(root, height=4, width=50)
text_box.pack(side=tk.BOTTOM, pady=10)

scrollbar = Scrollbar(root)


root.mainloop()