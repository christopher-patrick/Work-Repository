import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog



# Window
window = Tk()
window.title("Webjob Based Application")

# Command function
def showBox():
    Info = textentry.get()
    messagebox.showinfo('Message Box', 'Is this your designated file path?: {}'.format(Info))

def file_path():
    file_info = filedialog.askopenfilename()
    textentry.insert(tkinter.END, file_info)

# Window Padding


# Photo
photo1 = PhotoImage(file="EVA image.PNG")
Label(window, image=photo1, bg="black") .grid(row=0, column=2, padx=20, pady=20)

# Submit Button
Button(window, text="Press", width=6, command=file_path) .grid(row=4, column=2, pady=20)

# Textbox
Label(window, text='File Path') .grid(row=1, column=2)
textentry= Entry(window, width=35)
textentry.grid(row=2, column=2, sticky=W, pady=20, padx=20)



# Run
window.mainloop()
