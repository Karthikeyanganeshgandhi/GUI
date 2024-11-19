from tkinter import *
from tkinter import ttk

root=Tk()
label=Label(root,text="this is an image")
label.pack(side=TOP, pady=0)

path=PhotoImage(file="C:/Users/karth/OneDrive/Pictures/pngtree-mike-tyson-png-image_6890237.png")
label_image=Label(root,image=path,width=400,height=400)
label_image.pack()
root.geometry("600x400")
root.title("python.com")
root.mainloop()


