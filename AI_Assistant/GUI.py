from tkinter import *
from PIL import Image , ImageTk
import speech_to_text
import actions


root = Tk()
root.title("Your AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="dark orchid")

# ask function

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = actions.Actions(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot_val != None:
        text.insert(END,"JARVIS--->"+str(bot_val)+"\n")
    if bot_val == "Ok boss , glad i could help":
        root.destroy()


# send function

def send():
    send = entry.get()
    bot = actions.Actions(send)
    text.insert(END,'User--->'+send+"\n")
    if bot != None:
        text.insert(END,"JARVIS--->"+str(bot)+"\n")
    if bot == "Ok boss , glad i could help":
        root.destroy()

# delete text function

def delText():
    text.delete("1.0","end")

# Frame creation

f = Frame(root, padx=100,pady=7,borderwidth=3,relief=RAISED)
f.config(bg="dark orchid")
f.grid(row=0,column=1,padx=55,pady=10)

# Text Label 

text_label = Label(f,text="JARVIS",font=("Lexend 14 bold"),bg="plum" )
text_label.grid(row=0,column=0,padx=20,pady=10)

# Image Label

image = Image.open("python_projects/AI_Assistant/img/jarvis.jpg")
image=image.resize((250,250))
photo = ImageTk.PhotoImage(image)
image_label = Label(f,image=photo)
image_label.grid(row=1,column=0,pady=20)


# Adding Text widget

text = Text(root,font="Lexend 10 bold",bg="plum",padx=10,pady=10)
text.grid(row=2,column=0)
text.place(x=100,y=380,width=375,height=100)

# Entry Widget

entry = Entry(root,justify=CENTER)
entry.place(x=110,y=500,width=350,height=30)

# Buttton 1

b1 = Button(root,text="Ask",bg="plum",pady=14,padx=45,borderwidth=3,relief=SOLID,command=ask,font="Arial 8 bold",activebackground="plum")
b1.place(x=70,y=565)

# Buttton 2

b1 = Button(root,text="Delete",bg="plum",pady=14,padx=45,borderwidth=3,relief=SOLID,command=delText,font="Arial 8 bold",activebackground="plum")
b1.place(x=225,y=565)

# Buttton 3

b1 = Button(root,text="Send",bg="plum",pady=14,padx=45,borderwidth=3,relief=SOLID,command=send,font="Arial 8 bold",activebackground="plum")
b1.place(x=400,y=565)
root.mainloop()