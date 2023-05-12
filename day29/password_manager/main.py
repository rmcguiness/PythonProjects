from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=220, height=220)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

window.mainloop()
