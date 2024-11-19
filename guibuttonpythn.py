# from tkinter import *

# root=Tk()
# root.title("THIS IS MY SITE")
# def login():
#     print("login successfully")

# btn=Button(root,text="login",command=login,activebackground="blue",fg="green")
# btn.pack()
# root.geometry("500x200")
# root.mainloop()

from tkinter import *

root=Tk()
root.title("WELCOME TO SNAPCHAT")
def signup():
    print("sign up successfully")

action=Button(root,text="SIGN UP",command=signup,bg="green",activebackground="blue",fg="white")
action.pack()
root.geometry("500x400")
root.mainloop()
