from tkinter import *


root = Tk()
root.title("Moving Play Button")

window_width = 500
window_height = 500
root.geometry(f"{window_width}x{window_height}")

font = ("Arial", 48)
text = "PLAY"

button_x = window_width // 2
button_y = window_height // 2

velocity_x = 100
velocity_y = 100

def move_button():
    global button_x, button_y, velocity_x, velocity_y
    button_x += velocity_x
    button_y += velocity_y
    
    if button_x + button.winfo_width() > window_width or button_x < 0:
        velocity_x = -velocity_x
    if button_y + button.winfo_height() > window_height or button_y < 0:
        velocity_y = -velocity_y
    
    button.place(x=button_x, y=button_y)
    
def on_click(event):
    move_button()

button = Button(root, text=text, font=font, bg="red", fg="white", command=move_button)
button.place(x=button_x, y=button_y)

root.bind("<Button-1>", on_click)

while True:
    root.update()
