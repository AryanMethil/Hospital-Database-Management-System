from tkinter import *
import sqlite3

def sql_connection():
    try:
        con= sqlite3.connect('mydatabase9.db')
        return con
    except Error:
        print(Error)
def sql_table(con):
    cursor=con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS patient(pid integer PRIMARY KEY,pname text, age integer,address text, tel text,did integer,disease text,admit text,rno integer,FOREIGN KEY(did) REFERENCES doctor(did),FOREIGN KEY(rno) REFERENCES room(rno))")
    cursor.execute("CREATE TABLE IF NOT EXISTS room(rno integer PRIMARY KEY,duration integer,charges real,pid integer, FOREIGN KEY(pid) REFERENCES patientad(pid))")
    cursor.execute("CREATE TABLE IF NOT EXISTS doctor(did integer PRIMARY KEY,dname text , specialization text, dcharge real, sshift integer, esheft integer)")
    cursor.execute("insert or ignore into doctor(did ,dname  , specialization , dcharge , sshift , esheft) values(1,'Ghanshyam','diabetologist',1000,800,1900)")
    cursor.execute("insert or ignore into doctor(did ,dname  , specialization , dcharge , sshift , esheft) values(2,'Baburao Ganpatrao Apte','oncosurgeon',4000,1000,2300)")
    cursor.execute("insert or ignore into doctor(did ,dname  , specialization , dcharge , sshift , esheft) values(3,'Aryan','Pediatrician',1000,1400,2000)")
    cursor.execute("insert or ignore into doctor(did ,dname  , specialization , dcharge , sshift , esheft) values(4,'Adit','Gynecologist',3000,1300,2100)")
    cursor.execute("insert or ignore into doctor(did ,dname  , specialization , dcharge , sshift , esheft) values(5,'Hrishil','Neurologist',5000,1100,1700)")
    cursor.execute("select * from doctor")
    con.commit()

#add function
def add():
    def func():
        pid1 = e1.get()
        pname1 = e2.get()
        pname1.lower()
        age1 = int(e3.get())
        address1 = e4.get()
        address1.lower()
        tel1 = e5.get()
        disease1 = e6.get()
        disease1.lower()
        did1 = int(e7.get())
        admit1 = e8.get()
        admit1.lower()
        rno1 = int(e9.get())
        d1=int(e10.get())

        t2.destroy()
        if (pid1 == 0 or (admit1=="yes" and rno1==0)):
            print("Patient cannot be added")
            add()

        else:
            cursor = con.cursor()
            cursor.execute("INSERT INTO patient(pid,pname,age,address,tel,did,disease,admit,rno) VALUES(?,?,?,?,?,?,?,?,?)",(pid1, pname1, age1, address1, tel1, did1, disease1, admit1, rno1))
            con.commit()
            if admit1=='yes':
                cursor.execute("Insert into room(rno,duration,charges,pid) values(?,?,?,?)",(rno1,d1,1000,pid1))
                con.commit()
            print("Patient Added")



    t2 = Tk()
    t2.title("Add page")
    t2.geometry("1200x1200")

    Label(t2, text="Enter ID ", fg="Red").place(x=400, y=200)
    Label(t2, text="Enter Name ", fg="Red").place(x=400, y=250)
    Label(t2, text="Enter Age ", fg="Red").place(x=400, y=300)
    Label(t2, text="Enter Address ", fg="Red").place(x=400, y=350)
    Label(t2, text="Enter Contact No ", fg="Red").place(x=400, y=400)
    Label(t2, text="Enter Disease ", fg="Red").place(x=400, y=450)
    Label(t2, text="Enter Doctor ID ", fg="Red", ).place(x=400, y=500)
    Label(t2, text="Enter Admitted ", fg="Red").place(x=400, y=550)
    Label(t2, text="Enter Room No ", fg="Red").place(x=400, y=600)
    Label(t2, text="Enter Duration ", fg="Red").place(x=400, y=650)


    e1 = Entry(t2,textvariable=v1)
    e2 = Entry(t2,textvariable=v2)
    e3 = Entry(t2,textvariable=v3)
    e4 = Entry(t2,textvariable=v4)
    e5 = Entry(t2,textvariable=v5)
    e6 = Entry(t2,textvariable=v6)
    e7 = Entry(t2,textvariable=v7)
    e8 = Entry(t2,textvariable=v8)
    e9 = Entry(t2,textvariable=v9)
    e10=Entry(t2,textvariable=v10)

    e1.place(x=500, y=200)
    e2.place(x=500, y=250)
    e3.place(x=500, y=300)
    e4.place(x=500, y=350)
    e5.place(x=500, y=400)
    e6.place(x=500, y=450)
    e7.place(x=500, y=500)
    e8.place(x=500, y=550)
    e9.place(x=500, y=600)
    e10.place(x=500,y=650)


    Button(t2, text="Submit ", fg="Blue", width=10, command=func).pack()





def update():
    def update_in_db():
        def update_in_db_final():
            cursor.execute(
                "update patient set pname=? ,age=?,address=?,tel=?,disease=?,did=?,admit=?,rno=? where pid=?",
                (e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), pid1))

            con.commit()
            cursor.execute("Select * from room where pid=?",(pid1,))
            f3=cursor.fetchall()
            if f3:
                cursor.execute("update room set rno=?,duration=?,charges=? where pid=?",(e9.get(), e10.get(), 1000, pid1))
                con.commit()
            else:
                cursor.execute("insert into room(rno,duration,charges,pid) values(?,?,?,?)",(e9.get(),e10.get(),1000,pid1))
                con.commit()
            print("Record Updated!!")
            t9.destroy()



        global pid1
        pid1 = e1.get()
        cursor.execute("SELECT * from patient where pid=(?)", (pid1,))
        f = cursor.fetchall()[0]
        cursor.execute("Select duration from room where pid=(?)",(pid1,))
        f2=cursor.fetchall()
        t8.destroy()
        t9 = Tk()


        global v2,v3,v4,v5,v6,v7,v8,v9,v10
        Label(t9, text="Enter Name ", fg="Red").pack()
        e2 = Entry(t9, textvariable=v2)
        e2.insert(0,f[1])
        e2.pack()

        Label(t9, text="Enter Age ", fg="Red").pack()
        e3 = Entry(t9, textvariable=v3)
        e3.insert(0,f[2])
        e3.pack()

        Label(t9, text="Enter Address ", fg="Red").pack()
        e4 = Entry(t9, textvariable=v4)
        e4.insert(0,f[3])
        e4.pack()

        Label(t9, text="Enter Contact No ", fg="Red").pack()
        e5 = Entry(t9, textvariable=v5)
        e5.insert(0,f[4])
        e5.pack()

        Label(t9, text="Enter Disease ", fg="Red").pack()
        e6 = Entry(t9, textvariable=v6)
        e6.insert(0,f[6])
        e6.pack()

        Label(t9, text="Enter Doctor ID ", fg="Red").pack()
        e7 = Entry(t9, textvariable=v7)
        e7.insert(0,f[5])
        e7.pack()

        Label(t9, text="Enter Admitted ", fg="Red").pack()
        e8 = Entry(t9, textvariable=v8)
        e8.insert(0,f[7])
        e8.pack()

        Label(t9, text="Enter Room No ", fg="Red").pack()
        e9 = Entry(t9, textvariable=v9)
        e9.insert(0,f[8])
        e9.pack()

        if not f2:
            Label(t9,text="Enter Duration ",fg="Red").pack()
            e10 = Entry(t9,textvariable=v10)
            e10.insert(0,0)
            e10.pack()
        else:
            Label(t9, text="Enter Duration ", fg="Red").pack()
            e10 = Entry(t9, textvariable=v10)
            e10.insert(0,f2[0][0])
            e10.pack()

        b1 = Button(t9, text="Submit ", fg="Red", width=10, command=update_in_db_final).pack()
    cursor=con.cursor()
    t8=Tk()
    t8.geometry("1200x1200")
    t8.title("Update details")
    pid1 = 0
    v2 = StringVar()
    v3 = IntVar()
    v4 = StringVar()
    v5 = StringVar()
    v6 = StringVar()
    v7 = IntVar()
    v8 = StringVar()
    v9 = IntVar()
    v10 = IntVar()
    Label(t8, text="Enter ID ", fg="Red").place(x=400, y=200)
    tv=IntVar()
    e1 = Entry(t8,textvariable=tv)
    e1.place(x=500, y=200)
    Button(t8, text="Submit ", fg="Red", width=10, command=update_in_db).place(x=500, y=250)

#bill function
def bill():
    def bill_fun():
        i = int(e1.get())
        t6.destroy()
        cursor.execute("SELECT admit from patient where pid=?", (i,))
        s = cursor.fetchall()[0][0]
        cursor.execute("select did from patient where pid=?",(i,))
        b=cursor.fetchall()[0][0]
        con.commit()
        cursor.execute("SELECT dcharge from doctor where did=?", (b,))
        a = cursor.fetchall()[0][0]

        if (s == "no"):
            amt = a
            amt *= 1.18
            print(amt)
        else:
            # cursor.execute("select rno from patient where")
            cursor.execute("SELECT charges from room where rno=(SELECT rno from patient where pid=?)", (i,))
            c = cursor.fetchall()
            cursor.execute("SELECT duration from room where rno=(SELECT rno from patient where pid=?)", (i,))
            d = cursor.fetchall()
            amt = a + (c[0][0] * d[0][0])
            amt *= 1.18
            print(amt)
    cursor=con.cursor()
    t6=Tk()
    t6.title("Bill page")
    t6.geometry("1200x1200")
    l1=Label(t6,text="Enter Patient id ",fg="Red")
    l1.place(x=400,y=300)
    e1=Entry(t6,textvariable=v1)
    e1.place(x=525,y=300)
    b1=Button(t6,text="Submit",command=bill_fun)
    b1.place(x=500,y=400)

def doctime():
    cursor=con.cursor()
    def doclis():
        time = int(e1.get())
        sp=e2.get()
        cursor.execute("Select * from doctor where ? >= sshift and ? <= esheft and specialization==?", (time, time,sp))
        result = cursor.fetchall()
        print(result)
        t7.destroy()
    t7=Tk()
    t7.title("Doctor time")
    t7.geometry("1200x1200")
    Label(t7, text="Enter time ", fg="Red").place(x=400, y=200)
    e1 = Entry(t7)
    e1.place(x=500, y=200)
    Label(t7, text="Enter speciality ", fg="Red").place(x=400, y=250)
    e2 = Entry(t7)
    e2.place(x=500, y=250)

    b1 = Button(t7, text="Submit ", fg="Blue", width=10, command=doclis).place(x=500, y=300)





#second page
def command1():
    if entry1.get()=="admin" and entry2.get()=="pass@123":
        root.destroy()
        t1=Tk()
        t1.geometry("1200x1200")
        t1.title("Main Page")
        b1=Button(t1,text="Add Patient ",fg="Red",command=add).place(x=400,y=250)
        b2=Button(t1,text="Update Patient details ",fg="Red",command=update).place(x=400,y=300)
        b3=Button(t1,text="Doctor Availability",fg="Red",command=doctime).place(x=400,y=350)
        b4=Button(t1,text="Display Bill ",fg="Red",command=bill).place(x=400,y=400)
    else:
        print("Invalid username or password")
        entry1.delete(0,END)
        entry2.delete(0, END)
#first page
con=sql_connection()
sql_table(con)
root=Tk()
tv=IntVar()

v1 = IntVar()
v2 = StringVar()
v3 = IntVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = IntVar()
v8 = StringVar()
v9 = IntVar()
v10=IntVar()

e1=Entry()
e2=Entry()
e3=Entry()
e4=Entry()
e5=Entry()
e6=Entry()
e7=Entry()
e8=Entry()
e9=Entry()
e10=Entry()

f=[]
pid1=0
did1=0
admit1=""
rno1=0
pname1=""
disease1=""
age1=0
address1=""
tel1=""


root.geometry("1200x1200")
root.title("Login Page")
label1=Label(root,text="Username")
entry1=Entry(root)
label2=Label(root,text="Password")
entry2=Entry(root,show="*")
button=Button(root,text="Submit",command=command1)
label1.place(x=400,y=250)
label2.place(x=400,y=300)
entry1.place(x=500,y=250)
entry2.place(x=500,y=300)
button.place(x=450,y=350)
root.mainloop()