# GRAPHICAL USER INTERFACE(GUI):

'''

Here are some basic operations perform for making GUI of project wolfra.

~ First we import tkinter and instantiate our user interface, giving it value Tk().

~ Secondly there are multiple functions, use to customize our user interface:

  1. user-interface.geometry(): Makes the interface according to given length and height.
  2. user-interface.title() : Gives a specific title to your user interface.
  3. user-interface.config() : It has a value 'background' which is use to give color to interface.

~ To give icon to your GUI, you first need to define a variable and convert it into photoimage by using function Photoimage(location of file),
  then you just need to use a function: user-interface.iconphoto(True , variable).
  
'''

# How to make Labels:

'''

To prequire label in python you first need to set a variable having a function Label(user-interface) and then initialize other keyword 
arguments in Label like:

1. text : Gives text to your user interface.
2. font : It contains three things (type , size , style) of the text.
3. fg : It gives the color to your label.
4. bg : Gives a background color to the label.
5. relief : Gives a border to our label. It has two values 'RAISED' and 'SUNKEN'.
6. bd : Gives a width to our border.
7. padx : Gives a specific width to our border on x-axis.
8. pady: Gives a specific width to our border on y-axis.
9. image : Import an image on user interface, having a value of variable. This variable is equal to Photoimage(file path).
10. compound : Sets the direction of image on the user interface.

To see the label on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our label.

'''

# Buttons:

'''

To prequire button in python you first need to set a variable having a function Button(user-interface) and then initialize other keyword 
arguments in Button function like:

1. text : Gives text to your user interface.
2. font : It contains three things (type , size , style) of the text.
3. fg : It gives the color to your button.
4. bg : Gives a background color to the button.
5. relief : Gives a border to our button. It has two values 'RAISED' and 'SUNKEN'.
6. bd : Gives a width to our border.
7. padx : Gives a specific width to our border on x-axis.
8. pady: Gives a specific width to our border on y-axis.
9. image : Import an image on user interface, having a value of variable. This variable is equal to Photoimage(file path).
10. compound : Sets the direction of image on the user interface like 'top' , 'bottom' etc.
11. state : It is equal to "ACTIVE" or "DISABLED". You can set your button to "DISABLED",  if you don't want anyone to click it.
12. command : It refers to a function which performs an action.

To see the button on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our button.

'''

# Entrybox:

'''

To prequire entrybox in python you first need to set a variable having a function Entry(user-interface) and then initialize other keyword 
arguments in entrybox function like:

1. font : It contains three things (type , size , style) of the text.
2. fg : It gives the color to your entrybox.
3. bg : Gives a background color to the entrybox.
4. relief : Gives a border to our entrybox. It has two values 'RAISED' and 'SUNKEN'.
5. bd : Gives a width to our border.
6. show : Give any symbol if you want to hide what you have written. Example like password.

To see the entrybox on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our entrybox.

Use variable.insert() to give a username before even entering anything in the entrybox. 

After using entrybox, we can use variable.config(state=DISABLED) function to stop the data in our entrybox from changing.

'''

# CheckButton:

'''

To prequire CheckButton in python you first need to set a variable having a function CheckButton(user-interface) and then 
initialize other keyword arguments in CheckButton function like:

1. font : It contains three things (type , size , style) of the text.
2. fg : It gives the color to your CheckButton.
3. bg : Gives a background color to the CheckButton.
4. relief : Gives a border to our CheckButton. It has two values 'RAISED' and 'SUNKEN'.
5. bd : Gives a width to our border.
6. variable : Groups Checkbuttons togather if they share the same variable.
7. command : It refers to a function which performs an action.
8. onvalue: We can set this to any value which can be performed in a function. (This value depends on the data type of the variable function)
9. offvalue: We can set this to any value which can be performed in a function. (This value depends on the data type of the variable function)
10. padx : Gives a specific width to our border on x-axis.
11. pady: Gives a specific width to our border on y-axis.
12. image : Import an image on user interface, having a value of variable. This variable is equal to Photoimage(file path).

To see the CheckButton on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our CheckButton.

'''

# RadioButtons:

'''

To prequire RadioButtons in python you first need to set a variable having a function RadioButtons(user-interface) and 
then initialize other keyword arguments in RadioButtons function like:

1. font : It contains three things (type , size , style) of the text.
2. fg : It gives the color to your RadioButtons.
3. bg : Gives a background color to the RadioButtons.
4. relief : Gives a border to our RadioButtons. It has two values 'RAISED' and 'SUNKEN'.
5. bd : Gives a width to our border.
6. variable : Groups RadioButtons togather if they share the same variable.
7. command : It refers to a function which performs an action.
8. compound : Sets the direction of image on the user interface like 'top' , 'bottom' etc.
9. indicatoron : Having values 0 and 1, It eliminates circle indicators.
10. padx : Gives a specific width to our border on x-axis.
11. pady: Gives a specific width to our border on y-axis.
12. value : Assigns each radiobutton a different value. (It is taken as the index of the items in a list which are made as a button)
13. text : Adds text to RadioButton. (If its a list then it should be stated with it's index so that it will print according to it's index)
14. image : Import an image on user interface, having a value of variable. This variable is equal to Photoimage(file path).

To see the RadioButton on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our RadioButton. Also to print all the radiobuttons put the variable.place(x,y)
in the for loop and change the value of x and y and accordingly so that the radiobuttons don't overlap.

Example:

from tkinter import *

foodapp = Tk()

def check():
    if(x.get() == 0):
        print("Pizza will be delivered in 20 mins")
    elif(x.get() == 1):
        print("Burger will be delivered in 10 mins")
    else:
        print("Improper command, Please select a proper meal")

x = IntVar()
foods = ["Pizza", "Burger"]
pizza = PhotoImage(file="Images//pizza.png")
burger = PhotoImage(file="Images//burger.png")
foodphoto = [pizza , burger]

for index in range(len(foods)):
    radiobutton = Radiobutton(foodapp,
                            text=foods[index],
                            font=("Impact",50),
                            value=index,
                            variable=x,
                            image=foodphoto[index],
                            compound="left",
                            command=check,
                            bd=30,
                            padx=10,
                            pady=10,
                            indicatoron=0)
    radiobutton.pack(anchor=W)

foodapp.mainloop()

'''

# Scale:

'''

To prequire Scale in python you first need to set a variable having a function Scale(user-interface) and 
then initialize other keyword arguments in Scale function like:

1. font : It contains three things (type , size , style) of the text.
2. fg : It gives the color to your Scale.
3. bg : Gives a background color to the Scale.
4. relief : Gives a border to our Scale. It has two values 'RAISED' and 'SUNKEN'.
5. bd : Gives a width to our border.
6. from_ : Sets a starting limit for scale.
7. to: Sets an ending limit for Scale.
8. length : Gives a specific length to the scale. Width can also be given.
9. orient : Sets Orientation of Scale. (VERTICAL or HORIZONTAL)
10. padx : Gives a specific width to our border on x-axis.
11. pady: Gives a specific width to our border on y-axis.
12. tickinterval: Adds numerical interval for scale.
13. resolution: Increment of slider by a given percent.
14. troughcolor: Gives color to the numeric interval.
15. image : Import an image on user interface, having a value of variable. This variable is equal to Photoimage(file path).

To see the Scale on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our Scale.

variable.set() function sets a value on scale beforehand.

Example:

from tkinter import *

Tempsensor = Tk()

def check(self):
    print("The temperature is " +str(scale.get())+ " degree celsius")

scale = Scale(Tempsensor,
         from_ = 0,
         to = 100,
         length=600,
         command=check,
         orient="vertical",
         font=("Casual",25),
         tickinterval=10,
         resolution=10,
         fg="red",
         bg="black",
         troughcolor="#34c9eb"
         )

scale.pack()
Tempsensor.mainloop()

'''

# Listbox:

'''

To prequire Listbox in python you first need to set a variable having a function Listbox(user-interface) and 
then initialize other keyword arguments in Listbox function like:

1. font : It contains three things (type , size , style) of the text.
2. fg : It gives the color to your Listbox.
3. bg : Gives a background color to the Listbox.
4. relief : Gives a border to our Listboxle. It has two values 'RAISED' and 'SUNKEN'.
5. bd : Gives a width to our border.
6. selectmode : Allows you to select elements inside the listbox.. 
7. width: Gives width to Listbox.
8. length : Gives a specific length to the Listbox.
10.padx : Gives a specific width to our border on x-axis.
11. pady: Gives a specific width to our border on y-axis.

To insert elements in a Listbox, use variable.insert(index, text you want).

To adjust the size of the Listbox, use variable.config(height = listbox.size()). This func will make the Listbox according
to the number of elements present in Listbox.

To see the listbox on user interface use function: variable.place(x,y) . Here x and y have suitable numerical values.
We can also use variable.pack() function to see our listbox.

To submit the element from listbox, we use print(variable.curselection()) as shown in example

'''

# Example 1: 
# Selecting single element in list box

'''

from tkinter import *

foodapp = Tk()

def submit():
    print("You have ordered: " +str(listbox.get(listbox.curselection())))

def add():
    listbox.insert(listbox.size(), entryb.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

listbox = Listbox(foodapp,
                  font=("Aesthetic", 25),
                  bg="Light Yellow",
                  )

submitB = Button(foodapp,
                text="submit",
                command=submit)

entryb = Entry(foodapp,
               font=("Arial",15))

addB = Button(foodapp,
              text="Add an Item",
              command=add)

deleteb = Button(foodapp,
                 text="Delete an item",
                 command=delete)

listbox.insert(1 , "Pizza")
listbox.insert(2 , "Burger")
listbox.insert(3 , "Biryani")
listbox.insert(4 , "Pepsi")
listbox.insert(5 , "Nihari")

listbox.config(height=listbox.size())

entryb.place(x= 550, y=550)
addB.place(x=800, y=550)
deleteb.place(x=800, y=575)
submitB.place(x=800, y=600)
listbox.place(x=500, y=300)
foodapp.mainloop()

'''

# Example 2: 
# Selecting Multiple elements in listbox:


'''

from tkinter import *

foodapp = Tk()

def submit():

    foods = []

    for i in listbox.curselection():
        foods.insert(i , listbox.get(i))

    print("You have ordered: " )
    for items in foods:
        print(items)

def add():
    listbox.insert(listbox.size(), entryb.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

listbox = Listbox(foodapp,
                  font=("Aesthetic", 25),
                  bg="Light Yellow",
                  selectmode="multiple"
                  )

submitB = Button(foodapp,
                text="submit",
                command=submit)

entryb = Entry(foodapp,
               font=("Arial",15))

addB = Button(foodapp,
              text="Add an Item",
              command=add)

deleteb = Button(foodapp,
                 text="Delete an item",
                 command=delete)

listbox.insert(1 , "Pizza")
listbox.insert(2 , "Burger")
listbox.insert(3 , "Biryani")
listbox.insert(4 , "Pepsi")
listbox.insert(5 , "Nihari")

listbox.config(height=listbox.size())

entryb.place(x= 550, y=550)
addB.place(x=800, y=550)
deleteb.place(x=800, y=575)
submitB.place(x=800, y=600)
listbox.place(x=500, y=300)
foodapp.mainloop()

'''

# Messagebox:

'''

from tkinter import * 
from tkinter import messagebox

message = Tk()

def click():

    # messagebox.showinfo(message="You are gay!")
    # messagebox.showwarning(message="Warning, You are being touched by a gay!")
    # messagebox.showerror(message="Error, Opposite gender touch!")
    # messagebox.askokcancel(message="Registring you as gay!")
    # messagebox.askretrycancel(message="Gender reveal: You are gay!")
    # messagebox.askyesno(message="Are you gay?")
    # messagebox.askyesnocancel(message="Do you even have a gender?")
    # messagebox.askquestion(message="Are you gay?")

buton = Button(message, 
               command = click,
               text = "Don't you Dare click me!")

buton.pack()
message.mainloop()

We can also set a title in messagebox. We can also implement conditional statements on messageboxes.
Any messagebox can be put inside a while loop to make it appear again and again.
We can also change the icon of the message command to "warning", info etc.

'''

# Colorchosser:

'''

from tkinter import *
from tkinter import colorchooser

bgchanger = Tk()

def click():
    color =  colorchooser.askcolor()
    bgchanger.config(bg=color[1])

buton = Button(bgchanger,
               text="Click",
               command=click)

bgchanger.geometry("500x500")
buton.pack()
bgchanger.mainloop()

'''

# Textarea:

'''

from tkinter import *

notebook = Tk()

def submit():
    input = text.get("1.0", END)
    print(input)

button = Button(notebook,
                command=submit,
                text="Submit")

text = Text(notebook,
            font=("Arial",15,"italic"),
            padx=15,
            pady=15,
            bg="Light Yellow",
            fg="Royal Blue"
            )

button.pack()
text.pack()
notebook.mainloop()

'''

# Open A File:

'''

from tkinter import *
from tkinter import filedialog

FileOpener = Tk()

def Open():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\dell\\Desktop\\DEVELOPMENT",
                                          title="PY-Stuff",
                                          filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

Buton = Button(FileOpener,
               text="Open",
               command=Open)

Buton.pack()
FileOpener.mainloop()

'''

# Save a File:

'''

from tkinter import * 
from tkinter import filedialog

savefile = Tk()

def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    initialdir="C:\\Users\\dell\\Desktop\\DESIGNING\\DOCUMENTS\\Circuits\\Arduino Extracted codes",
                                    filetypes=(("Text Files", "*.txt"),("All Files","*.*")))
    filetext = text.get(1,END)
    file.write(filetext)
    file.close()

buton = Button(savefile,
               text="Save",
               command = save)
text = Text(savefile)

text.pack()
buton.pack()
savefile.mainloop()

We can also use console window to input some text.

'''

# Menubar:

'''

from tkinter import *

def Openfile():
    print("File has been opened")

def savefile():
    print("File has been saved")

app = Tk()
menubar = Menu(app)
app.config(menu=menubar)

filemenu = Menu(app, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open", command=Openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editmenu = Menu(app, tearoff=0)
menubar.add_cascade(label="Edit", menu=menubar)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

app.mainloop()

Note: We can also add images and customize our commands, just like mentioned above.

'''

# Frames:

'''

from tkinter import *

framing = Tk()

frames = Frame(framing, width = 5, bg="light yellow")

Button(frames, text = "UP", font=("aesthetic",20), bg="grey").pack()
Button(frames, text = "DOWN", font=("aesthetic",20), bg="grey").pack(side=BOTTOM)
Button(frames, text = "LEFT", font=("aesthetic",20), bg="grey").pack(side=LEFT)
Button(frames, text = "RIGHT", font=("aesthetic",20), bg="grey").pack(side=RIGHT)

frames.pack()
framing.mainloop()

'''

# Window Within a Window:

'''

1. Toplevel() : It makes new window on top of the other window. If we close one window the other will be closed automatically.
2. Tk() : It makes a totally new window. If we close one window the other will not be closed.
3. variable.destroy(): It is used to destroy the old window.

Example:

from tkinter import *

old = Tk()

def New():
    new = Tk()
    old.destroy()

Button(old, text="New Tab", command=New).pack()

old.mainloop()

'''

# New Tabs:

'''

The expand and fill makes the tab fit the whole window.

Example:

from tkinter import *
from tkinter import ttk
from notebook import *

drome = Tk()
drome.title("Drome")
drome.geometry("600x400")
drome.config(bg="light yellow")

note = ttk.Notebook(drome)

tab1 = Frame(note)
tab2 = Frame(note)

note.add(tab1, text="Tab 1")
note.add(tab2, text="Tab 2")

Label(tab1, text="This is Tab 1", fg="red", bg="white").pack()
Label(tab2, text="This is Tab 2", fg="blue", bg="white").pack()

note.pack(expand=True, fill="both")
drome.mainloop()

'''

# Grid:

'''

from tkinter import *

griding = Tk()

def submit():
    print("Login Info saved")

label1 = Label(griding, text="Enter your information" ,font=(20)).grid(row=0,column=0)

label2 = Label(griding, text="Enter Your Email: ").grid(row=1,column=0)
entry1 = Entry(griding).grid(row=1, column=1)

label3 = Label(griding, text="Enter Your Password: ").grid(row=2,column=0)
entry2 = Entry(griding).grid(row=2, column=1)

Button(griding, text="Submit",command=submit).grid(row=3, column=0, columnspan=2)

griding.mainloop()

'''

# Progress Bar:

'''

from tkinter import *
from tkinter.ttk import Progressbar
import time

Baring = Tk()
Baring.title("Progress Bar")

p = StringVar()

def run():
    for x in range(101): 
        time.sleep(0.05)
        bar['value'] = x
        p.set(str(x) + "%")
        Baring.update_idletasks()

bar = Progressbar(Baring, orient=HORIZONTAL, length=300, mode='determinate')
bar.pack(pady=10)

label = Label(Baring, textvariable=p)
label.pack()

button = Button(Baring, text="Download", command=run)
button.pack(pady=10)

Baring.mainloop()

'''