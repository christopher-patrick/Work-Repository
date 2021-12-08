from tkinter import *
from tkinter import messagebox



# Window
window = Tk()
window.title("My App")

# Command function
def showBox():
    Info = textentry.get()
    messagebox.showinfo('Message Box', 'Is this your designated file path?: {}'.format(Info))

# Photo
photo1 = PhotoImage(file="EVA image.PNG")
Label(window, image=photo1, bg="black") .grid(row=0, column=2)

# Textbox
Label(window, text="Enter the file path of the notification:") .grid(row=1, column=2)
textentry= Entry(window, width=35)
textentry.grid(row=2, column=2, sticky=W)

# Submit Button
Button(window, text="Submit", width=6, command=showBox) .grid(row=4, column=2)

# Run
window.mainloop()
