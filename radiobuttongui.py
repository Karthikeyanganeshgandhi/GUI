# from tkinter import * 
# user=Tk()
# user.title("python lobby")
# l=Label(user,text="python radio button test",font="60")
# l.pack()

# rb1=StringVar(user,"2")

# rbtn=Radiobutton(user,text="hello",variable=rb1,value=1)
# rbtn.pack()
# rbtn1=Radiobutton(user,text="hii",variable=rb1,value=2)
# rbtn1.pack()

# user.geometry("330x220")
# user.mainloop()

from tkinter import *

user=Tk()
user.title("example.com")
l=Label(user,text="this is just an example",font="60")
l.pack()

rb=StringVar(user,"1")

rbtn1=Radiobutton(user,text="select me",variable=rb,value=1)
rbtn1.pack()
rbtn2=Radiobutton(user,text="click me either",variable=rb,value=2)
rbtn2.pack()
rbtn3=Radiobutton(user,text="ignore them select me",variable=rb,value=3)
rbtn3.pack()

user.geometry("340x240")
user.mainloop()