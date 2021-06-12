import sqlite3


def DB_Connect():
    try:
        global conn
        global cur
        conn = sqlite3.connect("student.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE if NOT exists Student \
                (studentID INTEGER  PRIMARY KEY AUTOINCREMENT,\
                studentName VARCHAR (25) NOT NULL,\
                studentLName VARCHAR (25),\
                imgLoc VARCHAR (25), \
                mark INTEGER NOT NULL,\
                active tinyint(1) NOT NULL DEFAULT 1)")
        conn.commit()

    except Error as e:
        print(e)

def View():
    conn = sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute('Select * from Student')
    rows = cur.fetchall()
    conn.close()
    return rows

def Add(fname, lname, imageloc, mark, active):
    conn = sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("insert into Student values (null,?,?,?,?,?)",(fname, lname, imageloc, mark, active))
    conn.commit()
    conn.close()
    #View()

def Update(ID, StudentName, StudentLName, ImgLoc, Mark, Active):
    conn = sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("update Student set \
    studentName=?, studentLName =?, imgLoc =?, mark = ?, active =? where StudentID=?", (StudentName, StudentLName, ImgLoc, Mark, Active, ID))
    conn.commit()
    conn.close()
    
def Delete(ID):
    conn = sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("delete from Student where studentID=?", (ID,))
    #cur.execute("update Student set active=0 where studentID=?",(ID,))
    conn.commit()
    conn.close()

def Search(ID="",name="", LName="", activeS="", mark=""):
    conn = sqlite3.connect("student.db")
    cur=conn.cursor()
    if ID=="" and name=="" and activeS=="" and LName!="":#when only Last Name is selected
        cur.execute("select * from Student where studentLname=?", (LName,))
    elif ID=="" and LName=="" and activeS=="" and name!="":#when only first name is selected
        cur.execute("select * from Student where studentName=?", (name,))
    elif name=="" and LName=="" and activeS=="" and ID!="":#when only ID is selected
        cur.execute("select * from Student where studentID=?", (ID,))
    elif ID=="" and name=="" and LName=="" and activeS!="":#when only active is selected
        cur.execute("select * from Student where active=?", (activeS,))
    elif name!="" and LName!="":#when searched by both names
        cur.execute("select * from Student where studentName=? or studentLName=?", (name, LName,))
    elif mark!="":#when searched by mark
        cur.execute("select * from Student where mark >= ?", (mark,))
    
    rows = cur.fetchall()
    conn.close()
    return rows

    
        
    '''      
    cur.execute("select * from Student where studentID=? or studentName =? or studentLname =? or active =?", (ID, name, LName, activeS))
    #cur.execute("select * from employee whereempName like ",name)
    '''
    

    

def Retrieve(id):
    cur.execute("select * from Student where studentID=?", (id))#this retrieves information from a specific row in the DB(data-base)
    rows = cur.fetchall()
    print(rows)

#DB_Connect()
#Add("me", "lastname", "0.png", 0, 1)
