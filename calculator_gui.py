import Tkinter
import tkMessageBox

window = Tkinter.Tk()

# choose operation prompt
operation_prompt = Tkinter.Label(window, text="Choose math operation (+, -, *, /)")
operation_prompt.pack()

# operation entry field
operation = Tkinter.Entry(window)
operation.pack()

# enter x prompt
x_prompt = Tkinter.Label(window, text="Enter x")
x_prompt.pack()

# x entry field
x = Tkinter.Entry(window)
x.pack()

# enter y prompt
y_prompt = Tkinter.Label(window, text="Enter y")
y_prompt.pack()

# y entry field
y = Tkinter.Entry(window)
y.pack()

def calculate():
    if operation.get() == "+":
        result_text = int(x.get()) + int(y.get())
    elif operation.get() == "-":
        result_text = int(x.get()) - int(y.get())
    elif operation.get() == "*":
        result_text = int(x.get()) * int(y.get())
    elif operation.get() == "/":
        result_text = int(x.get()) / int(y.get())
    else:
        result_text = "Wrong operation!"

    tkMessageBox.showinfo("Result", result_text)

# submit button
submit = Tkinter.Button(window, text="Submit", command=calculate)  # check_guess, not check_guess()
submit.pack()

window.mainloop()