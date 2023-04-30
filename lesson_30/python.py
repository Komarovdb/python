from tkinter import *
root = Tk()
# lst=[1,2,True]
# root.geometry("600x1000")
# lstbox = Listbox(root)
# lstbox.pack()
#
# for elem in lst:
#     lstbox = Listbox(root)
# from tkinter import messagebox
# messagebox.showinfo("ахaхaхaхх", "пон")
# messagebox.showerror()
# messagebox.showwarning()

#
# lst = [1,2,3]
# lst_tk = StringVar(value=lst)
# lstbox = Listbox(root, listvariable=lst_tk)
# lstbox.pack()
#
# def fu():
#     print(lstbox.curselection())
# lstbox.bind('<<ListboxSelect>>', fu)
# btn = Button(root, text="output",command=fu)
# btn.pack()

# btn1 = Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn2 = Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn.pack(anchor=SW, expand=True)
# btn1.pack(fill=BOTH, expand=True)
# btn1.pack(pady=50)
# btn2.pack(fill=BOTH, expand=True)
# btn2.pack(pady=50)
# btn1 =Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn1.grid(column=0, row=0)
# btn2 =Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn2.grid(column=1, row=0)
# btn3 =Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn3.grid(column=2, row=0, rowspan=2, sticky=NS)
# btn4 =Button(root, text="Знакомьтесь с клавиатурой Gboard! Здесь будет текст который вы копируете")
# btn4.grid(column=0, row=1, columnspan=2, sticky=EW)

# b1 = Button(root, tetx="PSL NXU")
# b1.place(x=10,y=10)

from time import sleep
# def fu():
#     print("print")
#     root.after(1100,fu)
# root.after(3000,fu)
#
# root.mainloop()



def fu(pelmeni):
    print("print")
b1=Button(root, text="txt1")
b1.bind("<Enter>", fu)
b1.bind("<MouseWheel>", fu)
b1.bind("<FocusIn>", fu)
b1.focus_set()

