# from tkinter import *
# root=Tk()

# textbox=Text(root,width=20,height=13,wrap=WORD)
# textbox.grid(row=0,column=0)

# scroll=Scrollbar(root,orient=VERTICAL,command=textbox.yview)

# scroll.grid(row=0,column=3,sticky=N+S)
# textbox.config(yscrollcommand=scroll.set)

# root.geometry("350x220")
# root.title("python lobby.com")
# root.mainloop()

# from tkinter import *
# root=Tk()

# textbox=Text(root,width=20,height=13,wrap=NONE)
# textbox.grid(row=0,column=0)

# scroll=Scrollbar(root,orient=HORIZONTAL,command=textbox.xview)

# scroll.grid(row=3,column=0,sticky=E+W)
# textbox.config(xscrollcommand=scroll.set)

# root.geometry("350x220")
# root.title("python lobby.com")
# root.mainloop()



from tkinter import *

user=Tk()
user.title("NOTEPAD")

textbox=Text(user,width=30,height=40,wrap=WORD)
textbox.grid(row=0,column=0)

scroll=Scrollbar(user,orient=VERTICAL,command=textbox.yview)
scroll.grid(row=0,column=3,sticky=N+S)

textbox.config(yscrollcommand=scroll.set)

textbox1=Text(user,width=30,height=40,wrap=NONE)
textbox1.grid(row=0,column=0)

scroll1=Scrollbar(user,orient=HORIZONTAL,command=textbox1.xview)
scroll1.grid(row=3,column=0,sticky=E+W)

textbox.config(xscrollcommand=scroll1.set)

user.geometry("350x250")
user.mainloop()