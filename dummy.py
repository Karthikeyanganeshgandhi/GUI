from tkinter import *
from tkinter import ttk

user=Tk()
lbl=Label(user,text="WELCOME TO THE WWE CHAMPIONSHIP 2024",font=(("Times","50")))
lbl.pack(side=TOP,pady=10)
path=PhotoImage(file="C:/Users/karth/OneDrive/Pictures/pngtree-mike-tyson-png-image_6890237.png")
give_image=Label(user,image=path,width=400,height=400)
give_image.pack()

label=Label(user,text="USERNAME")
label.pack()

entry=Entry(user,bg="white",fg="black",bd=10)
entry.pack()

label1=Label(user,text="E-MAIL")
label1.pack()

entry1=Entry(user,bg="white",fg="black",bd=5)
entry1.pack()

label2=Label(user,text="PASSWORD")
label2.pack()

entry2=Entry(user,bg="white",fg="black",bd=5)
entry2.pack()

def RegisterNow():
    print("registered successfully")

btn=Button(user,text="RegisterNow",command=RegisterNow,bg="green",activebackground="blue",fg="black")
btn.place(x=700,y=700)
user.title("WWE CHAMPIONSHIP 2024 REGISTERING SITE.WWAP.IN")
user.geometry("600x500")
user.mainloop()