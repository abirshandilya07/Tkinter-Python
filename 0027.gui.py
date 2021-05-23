import tkinter as tk
import tkinter.messagebox as msgbox

top = tk.Tk()
# Code to add widgets will go here...
w = tk.Label(top, text="Hello")
w.pack()

def helloCallBack():
   msgbox.showinfo( "Gunin ne Bola", "Mama Vanshi")

B = tk.Button(top, text ="Hello From Abir", command = helloCallBack)

B.pack()

top.mainloop()
