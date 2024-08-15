from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("300x480")
root.resizable(width=0, height=0)
root.configure(bg="black")

entry = Entry(root, bd=10, width=300, font="Arial 21 bold", background="lightGrey")
entry.pack()

# Buttons functionality
def click(number):
    current = entry.get()
    if current == "Error":
        clear()
        entry.insert(END, number)
    else:
        entry.insert(END, number)

def add():
    entry.insert(END, "+")

def subtract():
    entry.insert(END, "-")

def multiply():
    entry.insert(END, "x")

def divide():
    entry.insert(END, "÷")

def power():
    entry.insert(END, "^")

def sqr_root():
    entry.insert(END, "√")

def clear():
    entry.delete(0, END)

def delete():
    current = entry.get()
    if current == "Error":
        clear()
    else:
        clear()
        entry.insert(0, current[:-1])

def equal():
    current = entry.get()
    try:
        # Replace operators with Python operators
        current = current.replace("x", "*").replace("÷", "/").replace("^", "**")
        
        # Handling square root
        if "√" in current:
            while "√" in current:
                idx = current.index("√")
                number = ""
                # Extract the number following the square root symbol
                for i in range(idx + 1, len(current)):
                    if current[i].isdigit() or current[i] == ".":
                        number += current[i]
                    else:
                        break
                if number:
                    # Compute the square root and replace in the expression
                    sqrt_value = str(math.sqrt(float(number)))
                    current = current.replace("√" + number, sqrt_value)
                else:
                    raise ValueError("Invalid Input")

        # Evaluate the final expression
        result = eval(current)
        clear()
        entry.insert(END, result)
    except Exception:
        clear()
        entry.insert(END, "Error")

# Numbers Buttons
btn7 = Button(root, text="7", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(7))
btn7.place(x=5, y=145)
btn8 = Button(root, text="8", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(8))
btn8.place(x=80, y=145)
btn9 = Button(root, text="9", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(9))
btn9.place(x=155, y=145)
btn4 = Button(root, text="4", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(4))
btn4.place(x=5, y=230)
btn5 = Button(root, text="5", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(5))
btn5.place(x=80, y=230)
btn6 = Button(root, text="6", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(6))
btn6.place(x=155, y=230)
btn1 = Button(root, text="1", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(1))
btn1.place(x=5, y=315)
btn2 = Button(root, text="2", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(2))
btn2.place(x=80, y=315)
btn3 = Button(root, text="3", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(3))
btn3.place(x=155, y=315)
btn0 = Button(root, text="0", font="Arial 19 bold", bg="Grey", bd=10, padx=10, pady=5, command=lambda: click(0))
btn0.place(x=5, y=400)
dotbtn = Button(root, text=".", font="Arial 19 bold", bg="Grey", bd=10, padx=13, pady=5, command=lambda: click("."))
dotbtn.place(x=80, y=400)


# Operations Buttons
btnclear = Button(root, text="C", font="Arial 19 bold", bg="crimson", bd=10, padx=9, pady=6, command=clear)
btnclear.place(x=5, y=60)

btnroot = Button(root, text="√", font="Arial 19 bold", bg="skyBlue", bd=10, padx=11, pady=6, command=sqr_root)
btnroot.place(x=80, y=60)

btnpower = Button(root, text="^", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=6, command=power)
btnpower.place(x=155, y=60)

btndivide = Button(root, text="÷", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5, command=divide)
btndivide.place(x=228, y=60)

btnmultiply = Button(root, text="x", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5, command=multiply)
btnmultiply.place(x=228, y=145)

btnminus = Button(root, text="-", font="Arial 19 bold", bg="skyBlue", bd=10, padx=13, pady=5, command=subtract)
btnminus.place(x=228, y=230)

btnplus = Button(root, text="+", font="Arial 19 bold", bg="skyBlue", bd=10, padx=10, pady=5, command=add)
btnplus.place(x=228, y=315)

btndelete = Button(root, text="⌫", font="Arial 19 bold", bg="crimson", bd=10, padx=0, pady=5, command=delete)
btndelete.place(x=155, y=400)

btnequal = Button(root, text="=", font="Arial 19 bold", bg="khaki", bd=10, padx=10, pady=5, command=equal)
btnequal.place(x=228, y=400)

root.mainloop()
