from tkinter import *
#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
window = Tk()
window.title("AcadView Assignment q1 and q2")
window.geometry('350x200')
lbl = Label(window, text="Hello World Q1.")
lbl.grid(column=5, row=0)
btn = Button(window, text="Exit",command=window.destroy)
btn.grid(column=5, row=7)


#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
def clicked():
    lbl = Label(window, text="Button was clicked,So new Text Printed !!")
    lbl.grid(column=5, row=6)
    
btn = Button(window, text="Click Me Q2.", command=clicked)
btn.grid(column=5, row=5)
window.mainloop()

#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text
window = Tk()
window.title("AcadView Assignment question 3")
window.geometry('350x200')
lbl = Label(window, text="Hello World.")
lbl.grid(column=5, row=0)
btn = Button(window, text="Exit",command=window.destroy)
btn.grid(column=5, row=7)
def clicked():
    lbl.configure(text="Button was clicked so the old text is overwritten")
btn = Button(window, text="Click Me.", command=clicked)
btn.grid(column=5, row=5)
window.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
window = Tk()
window.title("AcadView assignment q4")
window.geometry('350x200')
lbl = Label(window, text="Input Here:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=12)
txt.grid(column=1, row=0)
def clicked():
    res = txt.get()
    lbl = Label(window, text="Your input was :"+res)
    lbl.grid(column=2, row=6)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()