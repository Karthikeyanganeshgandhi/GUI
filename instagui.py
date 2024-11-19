from tkinter import *
from tkinter import ttk

user=Tk()
label=Label(user,text="INSTAGRAM",font=(("billabong","10")))
label.pack(side=TOP,padx=50,pady=50)

path=PhotoImage(file="C:/Users/karth/Downloads/instagram-logo-with-thick-circle-border-free-png.png")
label_image=Label(user,image=path,width=100,height=100)
label_image.pack(padx=50,pady=50)

label1=Label(user,text="E-mail or mobile number")
label1.pack(padx=30,pady=30)

entry=Entry(user,bg="white",fg="black",bd=10)
entry.pack()

label2=Label(user,text="PASSWORD.,\U0001f600")
label2.pack(padx=30,pady=30)

entry1=Entry(user,bg="white",fg="black",bd=10)
entry1.pack()

def LOGIN():
    print("Login successfully")

btn=Button(user,text="LOGIN",command=LOGIN,bg="green",activebackground="blue",fg="black")
btn.pack(padx=30,pady=30)



user.geometry("500x600")
user.title("instagram login page")
user.mainloop()

