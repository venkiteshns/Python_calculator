from tkinter import *


# function Creation Starts

def button_press(num):
    global equation_text

    equation_text += str(num)

    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:

        equation_label.set("Can't Divide By Zero")

        equation_text = ""

    except SyntaxError:

        equation_label.set("Invalid Action")

        equation_text = ""


def clear():
    global equation_text

    equation_text = ""

    equation_label.set("")


def delete():
    global equation_text

    current_text = equation_label.get()

    equation_label.set(current_text[:-1])

    equation_text = current_text[:-1]


def plusOMinus():
    global equation_text

    current_value = (eval(equation_text)) * -1

    equation_label.set(str(current_value))

    equation_text = str(current_value)


def percentage():
    global equation_text

    try:
        current_value = (eval(equation_text)) / 100
        equation_label.set(str(current_value))
        equation_text = str(current_value)
    except ZeroDivisionError:
        equation_label.set("Can't Divide By Zero")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Invalid Action")
        equation_text = ""
    except Exception as e:
        equation_label.set("Error")
        equation_text = ""



# End of Functions


#Class Created For Rounded Corners

class RoundedButton:
    def __init__(self, master, text, command, radius=20):
        self.master = master
        self.text = text
        self.command = command
        self.radius = radius
        self.canvas = Canvas(master, bg='black', highlightthickness=0)
        self.original_color = 'grey'
        self.pressed_color = 'darkgrey'

        # Create a rounded rectangle
        self.draw_button(self.original_color)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def draw_button(self, color):
        width = 55
        height = 55
        self.canvas.config(width=width, height=height)

        # Clear the canvas and redraw the button
        self.canvas.delete("all")  # Clear previous drawings
        self.canvas.create_oval(0, 0, self.radius, self.radius, fill=color, outline=color)
        self.canvas.create_oval(width - self.radius, 0, width, self.radius, fill=color, outline=color)
        self.canvas.create_oval(0, height - self.radius, self.radius, height, fill=color, outline=color)
        self.canvas.create_oval(width - self.radius, height - self.radius, width, height, fill=color, outline=color)
        self.canvas.create_rectangle(self.radius // 2, 0, width - self.radius // 2, height, fill=color, outline=color)
        self.canvas.create_rectangle(0, self.radius // 2, width, height - self.radius // 2, fill=color, outline=color)
        self.canvas.create_text(width // 2, height // 2, text=self.text, fill='white', font=("Arial", 10))

    def on_press(self, event):
        self.draw_button(self.pressed_color)  # Change to pressed color

    def on_release(self, event):
        self.draw_button(self.original_color)  # Change back to original color
        self.command()  # Execute the button's command

    def on_click(self, event):
        pass  # You can remove this if you just want to handle clicks in on_release


# Class Ends


# Window Creation

window = Tk()
window.title("Calculator")
window.geometry("300x380")
window.configure(bg="black")

# Window Creation Ends

# Variables Creation For Calculation and Display

equation_text = ""
equation_label = StringVar()


# Variables Creation Eds


#Label for Output

label = Label(window, textvariable=equation_label, font=('times new roman', 20), bg="grey", width=16, height=2,fg="white",anchor='e')
label.pack()

# Label Ends

# Frame Creation

frame = Frame(window,bg="black")
frame.pack()

# Frame Created

# Buttons Creation

button_AC = RoundedButton(frame, text="AC",command=clear)
button_AC.canvas.grid(row=0, column=0,padx=3, pady=3)

button_Del = RoundedButton(frame, text="Del",  command=delete)
button_Del.canvas.grid(row=0, column=1,padx=3, pady=3)

button_percentage = RoundedButton(frame, text="%", command=percentage)
button_percentage.canvas.grid(row=0, column=2,padx=3, pady=3)

button_division = RoundedButton(frame, text="/", command=lambda: button_press("/"))
button_division.canvas.grid(row=0, column=3,padx=3, pady=3)

button7 = RoundedButton(frame, text=7,  command=lambda: button_press(7))
button7.canvas.grid(row=1, column=0,padx=3, pady=3)

button8 = RoundedButton(frame, text=8, command=lambda: button_press(8))
button8.canvas.grid(row=1, column=1,padx=3, pady=3)

button9 = RoundedButton(frame, text=9, command=lambda: button_press(9))
button9.canvas.grid(row=1, column=2,padx=3, pady=3)

button_Mul = RoundedButton(frame, text="x", command=lambda: button_press("*"))
button_Mul.canvas.grid(row=1, column=3,padx=3, pady=3)

button4 = RoundedButton(frame, text=4, command=lambda: button_press(4))
button4.canvas.grid(row=2, column=0,padx=3, pady=3)

button5 = RoundedButton(frame, text=5,  command=lambda: button_press(5))
button5.canvas.grid(row=2, column=1,padx=3, pady=3)

button6 = RoundedButton(frame, text=6, command=lambda: button_press(6))
button6.canvas.grid(row=2, column=2,padx=3, pady=3)

button_sub = RoundedButton(frame, text="-",command=lambda: button_press("-"))
button_sub.canvas.grid(row=2, column=3,padx=3, pady=3)

button1 = RoundedButton(frame, text=1,command=lambda: button_press(1))
button1.canvas.grid(row=3, column=0,padx=3, pady=3)

button2 = RoundedButton(frame, text=2, command=lambda: button_press(2))
button2.canvas.grid(row=3, column=1,padx=3, pady=3)

button3 = RoundedButton(frame, text=3,  command=lambda: button_press(3))
button3.canvas.grid(row=3, column=2,padx=3, pady=3)

button_add = RoundedButton(frame, text="+",  command=lambda: button_press("+"))
button_add.canvas.grid(row=3, column=3,padx=3, pady=3)

button_pom = RoundedButton(frame, text="+/-", command=plusOMinus)
button_pom.canvas.grid(row=4, column=0,padx=3, pady=3)

button0 = RoundedButton(frame, text=0,  command=lambda: button_press(0))
button0.canvas.grid(row=4, column=1,padx=3, pady=3)

button_decimal = RoundedButton(frame, text=".", command=lambda: button_press("."))
button_decimal.canvas.grid(row=4, column=2,padx=3, pady=3)

button_equals = RoundedButton(frame, text="=", command=equals)
button_equals.canvas.grid(row=4, column=3,padx=3, pady=3)

# Buttons Creation Ends

window.mainloop()
