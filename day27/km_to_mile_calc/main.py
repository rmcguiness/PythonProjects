from tkinter import *

window = Tk()
window.title('Mi/Km converter')
checked_state = IntVar()

label = Label(text="Mi/Km Converter")
label.pack()

def action():
    new_speed = 0
    if(checked_state.get()):
        speed = entry.get()
        new_speed = str(float(speed) * 1.609) + "km"
    else:
        speed = entry.get()
        new_speed = str(float(speed) / 1.609) + "mi"

    output.config(text=new_speed)
    

entry = Entry(width=30)
entry.insert(END, string="Enter Speed")
entry.pack()

check_button = Checkbutton(text="Check to convert Mi to Km", variable=checked_state)
check_button.pack()


button = Button(text="Convert", command=action)
button.pack()

output = Label(text="")
output.pack()


window.mainloop()