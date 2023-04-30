from tkinter import *
root = Tk()
root.geometry("200x100")


l1 = Label(root, text="login:")
l1.grid(column=0,row=0)
l1 = Label(root, text="password:")
l1.grid(column=0,row=1)

entry=Entry(root,)
entry.grid(column=1, row=0)
entry2=Entry(root,)
entry2.grid(column=1, row=1)

b=Button(root, text="authorise")
b.grid(column=1, row=2)
root.mainloop()
