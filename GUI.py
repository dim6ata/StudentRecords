import DB_Funct
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import re

def viewALL():
    records = DB_Funct.View()
    #print(records)
    clearTree()# clear before displaying
    for row in records:
        tv.insert("", 0, values=row)
'''
def validateName(name):
    if not re.match("^[a-z]*$", name):
        print("Only Alphabet Allowed")
'''

   
#def validateMark():
    
'''
def validateActive():
'''    

def dbAdd():
    name = studentName_field.get()
    #validateName(name)
    lName = studentLName_field.get()
    imgL = imgLoc_field.get()
    mark = mark_field.get()
    #if mark0 != '':
     #   mark=mark0
    active = active_field.get()
    #print(name,lName,imgL,mark, active)
    DB_Funct.Add(name,lName,imgL,mark, active)
    reset()
    
def update():
    ID = studentID_field.get()
    name = studentName_field.get()
    lName = studentLName_field.get()
    imgL = imgLoc_field.get()
    mark = mark_field.get()
    active = active_field.get()
    #print(name,lName,imgL,mark, active)
    DB_Funct.Update(ID,name,lName,imgL,mark, active)
    reset()

def search():
    ID = studentID_field.get()
    name = studentName_field.get()
    lName = studentLName_field.get()
    active = active_field.get()
    mark = mark_field.get()
    data = DB_Funct.Search(ID,name, lName, active, mark)
    clearTree()
    for row in data:
        tv.insert("", 0, values=row)
    
    
def reset():
    setDefaultImage()
    clearTree()
    viewALL()
    clearTop()


def insertTree():
    for row in list:
        tv.insert("", 0, values=row)
        #tv.insert('',END,values=row)
def clearTree():
    x = tv.get_children()
    
    for item in x:
        tv.delete(item)
    setDefaultImage()
def deleteLine():
    ID = studentID_field.get()
    #print(ID,"to be deleted")
    DB_Funct.Delete(ID)
    reset()
    
def clearTop():
        studentID_field.delete(0,END)
        studentName_field.delete(0,END)
        studentLName_field.delete(0,END)
        mark_field.delete(0, END)
        active_field.delete(0, END)
        imgLoc_field.delete(0, END)
        setDefaultImage()


def select_item(event):
        row = tv.item(tv.selection())
        #print("row",type(row),row)
        item = tv.selection()[0]
        #print ('item clicked ', item)
        #print (tv.item(item)['values'][0])
        studentID_field.delete(0,END)
        studentName_field.delete(0,END)
        studentLName_field.delete(0,END)
        mark_field.delete(0, END)
        active_field.delete(0, END)
        imgLoc_field.delete(0, END)
        studentID_field.insert(END,row['values'][0])
        studentName_field.insert(END,row['values'][1])
        studentLName_field.insert(END,row['values'][2])
        imgLoc_field.insert(END,row['values'][3])
        mark_field.insert(END,row['values'][4])
        active_field.insert(END,row['values'][5])
        pic = imgLoc_field.get()
        imgChange(pic)
        '''
        img=ImageTk.PhotoImage(Image.open('img/'+ pic).resize((120,120)))
        photoHolder.configure(image=img)
        photoHolder.image = img
        '''
#changes images
def imgChange(pic):
        try:
            img=ImageTk.PhotoImage(Image.open('img/'+ pic).resize((120,120)))
            photoHolder.configure(image=img)
            photoHolder.image = img
        except FileNotFoundError:
            errorImg()
        except IsADirectoryError:
            errorImg()

def errorImg():
        holder=" - No Such File"
        #default=ImageTk.PhotoImage(Image.open('img/eye.jpg').resize((120,120)))
        #photoHolder.configure(image=default)
        #photoHolder.image = default
        setDefaultImage()
        imgLoc_field.insert(END,holder)

def setDefaultImage():
    default=ImageTk.PhotoImage(Image.open('img/eye.jpg').resize((120,120)))
    photoHolder.configure(image=default)
    photoHolder.image = default
        
#def errorInput():
        
'''

def imageSwap():
    
    img = ImageTk.PhotoImage(Image.open('img/eye.jpg').resize((120,120))) #"img/"+str(pic)
    
  '''      

    

    

win = Tk()
#Background
win.title("Student Record")
win.geometry("950x400")
win.configure(background='LightGreen')
#Student Frame
studentFrame = LabelFrame(win, text='Student')
studentFrame.configure(background='LightBlue2')
studentFrame.grid(row=0, column=0,sticky=NSEW, padx=8, pady=8)
#row/column set the position.
#padx/y deal with the padding of the element





#Student Name
studentName = Label(studentFrame,text='First Name: ')
studentName.grid(row=0, column=1, padx=8)
student_text = StringVar()
studentName_field = Entry(studentFrame,textvariable=student_text)
studentName_field.grid(row=0, column=2, padx=5)

#Student Surname

studentLName = Label(studentFrame,text='Last Name: ')
studentLName.grid(row=2, column=1, pady=8)
studentLName_text = StringVar()
studentLName_field = Entry(studentFrame,textvariable=studentLName_text)
studentLName_field.grid(row=2, column=2)

#Image Location

imgLoc = Label(studentFrame,text='Image Loc: ')
imgLoc.grid(row=3, column=1, pady=8)
imgLoc_text = StringVar()
imgLoc_field = Entry(studentFrame,textvariable=imgLoc_text)
imgLoc_field.grid(row=3, column=2)

#Photo Placeholder
#photo=imgLoc_field.get()
#print(photo)
openImage = Image.open('img/eye.jpg')         #'img/eye.jpg'
img=ImageTk.PhotoImage(openImage.resize((120,120)))
photoHolder = Label(studentFrame, image = img)
photoHolder.grid(row=0, column=0, rowspan=5, pady = 2, padx=2)

#Student ID
studentID = Label(studentFrame,text='Student ID: ')
studentID.grid(row=0, column=3, padx=2)
studentID_text = StringVar()
studentID_field = Entry(studentFrame,textvariable=studentID_text)
studentID_field.grid(row=0, column=4, padx=8)

#Mark
mark = Label(studentFrame,text='Mark: ')
mark.grid(row=2, column=3, padx=15)
mark_text = StringVar()
mark_field = Entry(studentFrame,textvariable=mark_text)
mark_field.grid(row=2, column=4, padx=8)

#Active
active = Label(studentFrame,text='Active: ')
active.grid(row=3, column=3, padx=8)
active_text = StringVar()
active_field = Entry(studentFrame,textvariable=active_text)
active_field.grid(row=3, column=4)




#buttons
btnFrame = LabelFrame(win,text='Action:')
btnFrame.configure(background='DarkViolet')
btnFrame.grid(row=0, column=3,sticky=NSEW,rowspan = 8, padx=8,pady=8)
b1=Button(btnFrame,text="View all",width=16, height=2, command=viewALL)
b1.grid(row=0, column=0, pady=4)

b2=Button(btnFrame,text="Search Entry",width=16, height=2, command=search)
b2.grid(row=3, column=0, pady=4)

b3=Button(btnFrame,text="Add Entry",width=16, height=2, command=dbAdd)
b3.grid(row=4, column=0, pady=4)

b4=Button(btnFrame,text="Update",width=16, height=2, command=update)
b4.grid(row=5, column=0, pady=4)

b5=Button(btnFrame,text="Delete",width=16, height=2, command=deleteLine)
b5.grid(row=6, column=0, pady=4)

b6=Button(btnFrame,text="Close",width=16, height=2, command=win.destroy)
b6.grid(row=7, column=0, padx = 6, pady=4)

b7=Button(btnFrame,text="Clear Display",width=16, height=2, command=clearTree)
b7.grid(row=2, column=0, pady=4)

b8=Button(btnFrame,text="Clear Student",width=16, height=2, command=clearTop)
b8.grid(row=1, column=0, pady=4)

#win.mainloop()


#Version 3


dispFrame = LabelFrame(win, text='Display:')
dispFrame.configure(background='Pink')
dispFrame.grid(row=1, column=0, sticky=NSEW, padx=8, pady=8)
tv = ttk.Treeview(dispFrame, height=10, columns=3)
tv.grid(row=1, column=1, columnspan=6)
tv["columns"] = ["Student ID", "First Name", "Last Name", "Image Loc", "Mark", "Active"]
tv["show"] = "headings"
tv.heading("Student ID", text="Student ID")
tv.column("Student ID", anchor='center', width=120)
tv.heading("First Name", text="First Name")
tv.column("First Name", anchor='center', width=120)
tv.heading("Last Name", text="Last Name")
tv.column("Last Name", anchor='center', width=120)
tv.heading("Image Loc", text="Image Loc")
tv.column("Image Loc", anchor='center', width=120)
tv.heading("Mark", text="Mark")
tv.column("Mark", anchor='center', width=120)
tv.heading("Active", text="Active")
tv.column("Active", anchor='center', width=120)


#Scrollbar
sb1 = Scrollbar(dispFrame,command=tv.yview,
orient=VERTICAL)
sb1.grid(row=0,column=7,rowspan=2,sticky='ns')
tv.configure(yscrollcommand=sb1.set)

#CONNECTING DISPLAY FRAMES


tv.bind('<<TreeviewSelect>>', select_item)

#tv.bind('<ButtonRelease-1>', select_item)
#tv.bind('<Up>', select_item)
#tv.bind('<Down>', select_item)
#tv.bind('<1>', imgChange)


win.mainloop()




