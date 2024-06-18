from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    # Delete all content from the 0th charachter of the 1st line (1.0) to the END
    TextArea.delete(1.0,END) 

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files","*.*"),
                           ("Text Documents","*.txt")])
    # If No File is Selected
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f= open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    # If there is no current file, prompt the user to save as a new file.
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                defaultextension=".txt",
                                filetypes=[("All Files","*.*"),
                                ("Text Documents","*.txt")])
        if file == "":
            # If the user doesn't specify a file name and location, then cancel.
            file=None
        else:
            # If the user specifies a file name and location, save the content.
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
    else:
         # If the file already has a name, save the current content to it.
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
   TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","This is Notepad GUI created by Gagan")

if __name__ == '__main__':
    #Basic Tkinter setup
    root=Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x788")

    #Add TextArea
    TextArea= Text(root,font="lucida 13")
    file=None
    TextArea.pack(fill=BOTH,expand=True)

    #Lets create a menuvar
    Menubar = Menu(root)
    # FileMenu Starts
    FileMenu = Menu(Menubar,tearoff=0)
    # To open new file
    FileMenu.add_command(label="New",command=newFile)
    

    # To open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    # To save the current file

    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    # File Menu Ends


    # Edit Menu Starts
    EditMenu = Menu(Menubar,tearoff=0)
    # To give a feature of cut,copy,paste
    EditMenu.add_command(label="Cut",command=cut) 
    EditMenu.add_command(label="Copy",command=copy) 
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu) 
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    # Help Menu Ends
    root.config(menu=Menubar)

    # Adding Scrollbar
    ScrollBar = Scrollbar(TextArea)
    ScrollBar.pack(side=RIGHT,fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)

    root.mainloop()