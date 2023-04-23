from tkinter import *
# win = Tk()
# win.geometry("1000x500")
# win['bg'] = "#8c62c5"

# lab = Label(win)
# lab = Label(win, text="ahhhh")
# lab['bg'] = "lightblue"
# lab['foreground'] = "gold3"
# lab.pack
# ent = Entry(win,
#             wight=8,
#             borderwight=2,
#             font=("Arial 15 bold"))
# ent.pack
#
#
# txt = Text(win, wight=20, height=5, wrap='word')
# txt.pack()
#
# def ekshon():
#      print(cb_val.get())
#
# btn = Button(win, commmand=ekshon)
# btn['text'] = "button"
# btn.pack
# cb_val = BooleanVar()
# cb = Checkbutton(win,
#                  text="йа сникирс",
#                       command=ekshon,
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False
#                  )
# cb.pack()
# cb.select()
# cb.deselect()
#
# def get_rb():
#     print(rb_val.get())
# rb_val = IntVar()
# rb1 = Radiobutton(win,
#                  text="down",
#                  variable=rb_val,
#                  value=421,
#                  command=get_rb)
# rb1.pack()
# rb2 = Radiobutton(win,
#                  text="up",
#                  variable=rb_val,
#                  value=421,
#                  command=get_rb)
# rb2.pack()
# def get_scala(val):
#     print(scala.get())
#     print(val)
# scala = Scale(win,
#            from_=0,
#            to=150,
#            orient=HORIZONTAL,
#            length=600,
#            tickinterval=10,)
# scala.pack()
# img = PhotoImage(file="watermelon.png")
# img_small = img.subsample(1,2)
# #img_big = img.zoom(3,3)
# lab = Label(win, image=img_small)
# lab.pack()
# win.mainloop()

# Label(win, text="maus", bg="gold3").pack
# Label(win, text="tiger", bg="lightblue").pack(pady=15, ipady=3)

# def knopka(event):
#     lab['text'] = message = ent.get()
#
# root = Tk()
# root.geometry=("400x500")
#
# lab=Label(root, text="...")
# lab.pack()
#
# ent=Entry(root)
# ent.bind("<Button-3>", knopka)
# ent.insert(0,"Впиши и ПКМ")
# ent.pack()

# def hel_lo():
#     userchoise=rb_val.get()
#     if userchoise==1:
#         lab["text"] = "Hello " + rb1["text"]
#     else:
#         lab["text"] = "Hello " + rb2["text"]
#
#
# lab = Label(root, text="Hello ")
# lab.pack()
# rb_val=IntVar()
#
# rb1=Radiobutton(root, text="world", variable=rb_val, value=1, command=hel_lo)
# rb1.pack()
#
# rb2=Radiobutton(root, text="python", variable=rb_val, value=2, command=hel_lo)
# rb2.pack()

# def Activation():
#      if cb_val.get() == True:
#          b["text"] = "Активна"
#          b["state"] = "normal"
#      else:
#          b["text"] = "Неактивна"
#          b["state"] = "disabled"
# win = Tk()
# cb_val = BooleanVar()
# cb = Checkbutton(win, text="АКТИВАЦИЯ", variable=cb_val, onvalue=True, offvalue=False, command=Activation)
# cb.pack()
# b = Button(win, text="НЕАКТИВНА", state="disabled")
# b.pack()




win.mainloop()
