from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "Untitled"  # Correct typo in variable name
    text.delete(0.0, END)

def saveFile():
    global filename
    if filename is None:  # Add a check if the file is not yet defined
        saveAs()
    else:
        t = text.get(0.0, END)
        with open(filename, 'w') as f:  # Use `with` to handle files safely
            f.write(t)

def saveAs():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is not None:  # Ensure the file dialog wasn't canceled
        filename = f.name
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
            f.close()  # Explicitly close the file to save changes
        except Exception as e:  # Catch any exception
            showerror(title="Oops!", message="Unable to save file: " + str(e))

def openFile():
    global filename
    f = askopenfile(mode='r')
    if f is not None:  # Ensure the file dialog wasn't canceled
        filename = f.name
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)

# GUI Setup
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)  # Correct typo: mixsize -> maxsize

text = Text(root, width=400, height=400)
text.pack()

# Menu Setup
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)  # Correct typo: lable -> label
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)  # Correct typo: lable -> label

root.config(menu=menubar)
root.mainloop()