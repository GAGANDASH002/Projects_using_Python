from tkinter import *

# -------------Actual logic of calculator goes here-------------
def click(event):
    global scvalue
    text=event.widget.cget("text")#extracts the text from the button that has been clicked
    print(text)

     # if "=" button is clicked, it will evaluate the expression on the screen
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            # when the evaluating expression is not valid
            try:
                value=eval(screen.get())#evaluates string values

            except Exception as e:
                print(e)
                value="Error"
         # updating the display with the result
        scvalue.set(value)
        screen.update()

    # if "C" button is clicked, it will clear the display
    elif text=="C":
        scvalue.set("")
        screen.update()

     # if "<-" button is clicked, it will erase the last char of expression on the display
    elif text == "<-":
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    
    # except all above, if any other button is clicked, it will be appended to the expression on the display
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()#updates screen value with the number or expression pressed pressed


# -------------Defining the GUI structure-------------
root=Tk()
root.geometry("345x640")
root.title("Calculator GUI")
root.configure(background="black")
root.minsize(345, 640)
root.maxsize(345, 640)


scvalue=StringVar()
scvalue.set("")

# Creating main screen where i/o will be displayed
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold",justify=RIGHT,bg="black",fg="white"
             ,relief=SUNKEN)
screen.pack(fill=X,pady=10,padx=10,side=TOP)

# List of buttons to be placed in the calculator
buttons = [["C", "%", "<-", "/"],
           ["7", "8", "9", "*"],
           ["4", "5", "6", "-"],
           ["1", "2", "3", "+"],
           ["00", "0", ".", "="]]


# creating buttons using for loops and iterating the items in above list
for row in buttons:
    f= Frame(root,bg="black")
    f.pack(fill=X,side=TOP,padx=20)
    for btn in row:
        b=Button(f,text=btn,font="Lucida 28 bold",pady=15,bg="black",fg="white",width=3,height=1,
                 activebackground="black",activeforeground="white")
        b.pack(side=LEFT)
        b.bind("<Button-1>",click)

root.mainloop()