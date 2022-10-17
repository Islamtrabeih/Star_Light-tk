from tkinter import *



class ToggleButton(Canvas):
    def __init__(self, root, command=None, fg='#FF8787', bg='#EDEDED', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width=50, height=30, borderwidth=0, highlightthickness=0)
        self.root = root
        self.right_arc = self.create_arc((0, 0, 0, 0), start=90, extent=180, fill=bg, outline=bg)
        self.left_arc = self.create_arc((0, 0, 0, 0), start=-90, extent=180, fill=bg, outline=bg)
        self.rect = self.create_rectangle(0, 0, 0, 0, fill=bg, outline=bg)
        self.circle = self.create_oval(0, 0, 0, 0, fill=fg, outline="#FFD1D1", width=5)
        self.bind('<Configure>', self._resize)
        self.bind('<Button>', self._animate, add='+')
        self.bind('<Button>', command, add='+')
        self.state = 0


    def _resize(self, event):
        self.coords(self.right_arc, 5, 5, event.height-5, event.height-5)
        self.coords(self.left_arc, 5, 5, event.height, event.height-5)
        factor = event.width-(self.coords(self.left_arc)[2]-self.coords(self.left_arc)[0])-10
        self.move(self.left_arc, factor, 0)
        self.coords(self.rect, self.bbox(self.right_arc)[2]-2, 5, self.bbox(self.left_arc)[0]+2, event.height-5)
        self.coords(self.circle, 5, 5, event.height-5, event.height-5)
        if self.state:
            self.moveto(self.circle, self.coords(self.left_arc)[0]+4, 4)


    def _animate(self, event):
        x, y, w, h = self.coords(self.circle)
        x = int(x-1)
        y = int(y-1)
        if x == self.coords(self.left_arc)[0]+6:
            self.moveto(self.circle, 4, 2)
            self.state = 0
            #print("left")
        else:
            self.moveto(self.circle, self.coords(self.left_arc)[0]+4, 2)
            self.state = 1
            #print("ff")


    def get_state(self):
        return self.state


#Your own function
def hello(event=''):
    if bool(btn2.get_state()):
        print(1)
    elif not bool(btn2.get_state()):
        print(0)

