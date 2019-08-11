from tkinter import *
from tkinter import filedialog, messagebox
import os, glob, tkinter.messagebox


# FUNCTIONS
def Directory(event):
    dir = filedialog.askdirectory(title='Please select a directory')
    dirLabel.config(text=dir)
    os.chdir(dir)
def GetEx1():
    ex1 = ExtAsk1.get()
    return ex1
def GetEx2():
    ex2 = ExtAsk2.get()
    return ex2
def Scan(event):
    ext_scan = '*.' + GetEx1()
    count = 0
    result = ''
    for files in glob.glob(ext_scan):
        count += 1
    if count == 0:
        result = "There is no " + GetEx1() + " file here"
    elif count == 1:
        result = "There is 1 " + GetEx1() + " file here."
    else:
        result = "There are " + str(count) + " " + GetEx1() +  " files"
    label4.config(text = result)
def Change(event):
    old_ext = "*." + GetEx1()
    try:
        for file in glob.glob(old_ext):
            file_name , file_old_ext = os.path.splitext(file)
            file_new_name = file_name + '.' + GetEx2()
            os.rename(file,file_new_name)
        os.startfile(os.getcwd())
        tkinter.messagebox.showinfo("Conversion completed!", "Thanks for using!")
    except:
        messagebox.showerror("Error", "Something went wrong, please try again")
root = Tk()
root.title("Change Extension")
root.geometry('400x300')
# MAIN MENU BAR
menuBar = Menu(root)
root.config(menu = menuBar)
subMenu = Menu(menuBar)
menuBar.add_cascade(label = "File", menu = subMenu)
menuBar.add_cascade(label = "Edit", menu = subMenu)
menuBar.add_cascade(label = "About",menu = subMenu)

# MAIN FRAME
topFrame = Frame(root)
topFrame.pack(side = TOP, pady = 10)

## DIRECTORY (CHOOSE AND SHOW DIR)
dirButton = Button(topFrame, text = "Choose directory")
dirButton.bind("<Button-1>", Directory)
dirButton.grid(row = 0, sticky = W, pady = (0,15))
dirLabel = Label(topFrame, text = "Current Directory", justify = LEFT, width = 20)
dirLabel.grid(row = 0, column = 1, pady = (0,15), sticky = W)

## EXTENSION ASK
label1 = Label(topFrame, text = "Your current \nfiles's extension: ", justify = LEFT)
label1.grid(row = 1, column = 0, sticky = W)
ExtAsk1 = Entry(topFrame)
ExtAsk1.grid(row = 1, column = 1)
label2 = Label(topFrame, text = "change to: ", justify = LEFT)
label2.grid(row = 3, column = 0, sticky = W)
ExtAsk2 = Entry(topFrame)
ExtAsk2.grid(row = 3, column = 1)

## SCAN FILES
scan_but = Button(topFrame, text = "Scan files")
scan_but.bind("<Button-1>", Scan)
scan_but.grid(row = 2, column = 0, sticky = W)
label4 = Label(topFrame, text = "Your number of files here", pady = 10 )
label4.grid(row = 2, column = 1, sticky = W) #add counting command

## CONVERT BUTTON
ConBut = Button(topFrame, text = "Convert!", width = 10)
ConBut.bind("<Button-1>",Change)
ConBut.grid(row = 4, column = 0, columnspan = 4, pady = (25,0))

## STATUS BAR
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM, fill = X)
statusLabel = Label(bottomFrame, text = "Written by Hoang Quan", bd = 1, relief = SUNKEN, justify = LEFT, anchor = W)
statusLabel.pack(side = BOTTOM, fill = X)


root.mainloop()