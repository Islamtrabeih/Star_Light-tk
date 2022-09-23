from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import time


window = ThemedTk(theme="breeze")
# window.geometry('%dx%d+%d+%d' % (width, height, x, y))
# Explanation: ('width x height + X coordinate + Y coordinate')
window.geometry("%dx%d+%d+%d" % (427, 250, (window.winfo_screenwidth() / 2) - (427 / 2), (window.winfo_screenheight() / 2) - (250 / 2)))
window.overrideredirect(1)

image = Image.open("data/icons/1.jpg")
if image.size != (427, 250):
    image = image.resize((427, 250), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)
bg_label = Label(window, image=image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = image

s = ttk.Style()
s.theme_use('alt')
s.configure("#00.Horizontal.TProgressbar", foreground='#ff4040', background='#ffbf00')
progress = Progressbar(window, style="#00.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=-10, y=235)
color = '#1b1d46'


def callback():
    import GUI


def bar():
    l4 = Label(window, text='Loading...', fg='white', bg='#1b1d46')
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=210)
    r = 0
    for i in range(100):
        progress['value'] = r
        window.update_idletasks()
        time.sleep(0.01)
        r = r + 1
    window.destroy()
    callback()


# Frame(window, width=427, height=241, bg=color).place(x=0, y=0)
b1 = Button(window, width=10, height=1, text='Start', command=bar, border=0, fg=color, bg='white')
b1.place(x=170, y=200)
# Label
l1 = Label(window, text='Star-Light', fg='white', bg=color)
lst1 = ('Apple Chancery', 25)
l1.config(font=lst1)
l1.place(x=5, y=30)
x = 'LEO Orbits        \nAzhar University'
l2 = Label(window, text=x, fg='#ff4040', bg=color)
lst2 = ('Times New Roman', 13)
l2.config(font=lst2)
l2.place(x=10, y=80)

window.mainloop()
