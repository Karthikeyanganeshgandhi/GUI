# from tkinter import *

# user=Tk()
# user.title("python lobby")
# a=Label(user,text="python lobby.com",font="60")
# a.pack()

# checkbox1=IntVar()
# checkbox2=IntVar()

# button0=Checkbutton(user,text="learning",
#                     variable=checkbox1,
#                     onvalue=1,
#                     offvalue=0,
#                     height=3,
#                     width=12)
# button1=Checkbutton(user,text="tutorial",
#                     variable=checkbox2,
#                     onvalue=1,
#                     offvalue=0,
#                     height=3,
#                     width=12)

# button0.pack()
# button1.pack()

# user.geometry("320x220")
# user.mainloop()

from tkinter import *

windw=Tk()
windw.title("review mallu")
l=Label(windw,text="THIS IS JUST AN EXAMPLE",font="60")
l.pack()

checkbox1=IntVar()
checkbox2=IntVar()

button0=Checkbutton(windw,text="just an example",
                    variable=checkbox1,
                    onvalue=1,
                    offvalue=0,
                    height=3,
                    width=12)
button1=Checkbutton(windw,text="tick here",
                    variable=checkbox2,
                    onvalue=1,
                    offvalue=0,
                    height=3,
                    width=12)

button0.pack()
button1.pack()

windw.geometry("330x220")
windw.mainloop()