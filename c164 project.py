from tkinter import *

root =Tk()

root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="black")


label_planet_image = Label(root,bg="gold",highlightthickness=5,borderwidth=2,relief=SOLID)
label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)



def planet_info():
    print("CHECK")


btn = Button(root,text="Choose Image",command=planet_info)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn = Button(root,text="Rotate",command=planet_info)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)

root.mainloop()
