from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from tkcalendar import DateEntry
import mysql.connector as a
root = Tk()
root.geometry("1350x700")
root.title("Student Management System")
#------------------VARIABLES--------------------------
r_var = StringVar()
n_var = StringVar()
dob_var = StringVar()
e_var = StringVar()
c_var = StringVar()
g_var = StringVar()
search_var = StringVar()
s_var = StringVar()
#------------------FUNCTIONS--------------------------
def add_data():
    if r_var.get() == "" or n_var.get() == "":
        messagebox.showerror("Error","All Fields are required!!")
    else:
        mydb = a.connect(host="localhost",user="root",password="Mysql@1234",database="stud")
        """ if mydb.is_connected():
                print("Successfully Connected")
        else:
            print("NotConnected") """
        cur = mydb.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(n_var.get(),r_var.get(),dob_var.get(),g_var.get(),c_var.get(),e_var.get(),address_txt.get('1.0',END)))
        mydb.commit()
        get_data()
        clear()
        mydb.close
        messagebox.showinfo("Success","Data has been added successfully!!")
def get_data():
    mydb = a.connect(host="localhost",user="root",password="Mysql@1234",database="stud")
    cur = mydb.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    if len(rows)!=0:
        S_table.delete(*S_table.get_children())
        for row in rows:
            S_table.insert('',END,values=row)
        mydb.commit()
    mydb.close() 
def clear():
    r_var.set("")
    n_var.set("")
    dob_var.set("")
    e_var.set("")
    c_var.set("")
    g_var.set("")   
    address_txt.delete("1.0",END)
def get_value(ev):
    cursor_row = S_table.focus()
    content = S_table.item(cursor_row)
    row = content['values']
    #print(row)
    n_var.set(row[0])
    r_var.set(row[1])
    dob_var.set(row[2])
    g_var.set(row[3])
    c_var.set(row[4])
    e_var.set(row[5])
    address_txt.delete('1.0',END)
    address_txt.insert(END,row[6])
def update():
    mydb = a.connect(host="localhost",user="root",password="Mysql@1234",database="stud")
    '''if mydb.is_connected():
            print("Successfully Connected")
    else:
        print("NotConnected")'''
    cur = mydb.cursor()
    cur.execute("update student set name=%s,dob=%s,gender=%s,contact=%s,email=%s,address=%s where reg_no=%s",(n_var.get(),dob_var.get(),g_var.get(),c_var.get(),e_var.get(),address_txt.get('1.0',END),r_var.get()))
    mydb.commit()
    get_data()
    clear()
    mydb.close
    messagebox.showinfo("Update","Successfully updated the data")
def delete():
    mydb = a.connect(host="localhost",user="root",password="Mysql@1234",database="stud")
    cur = mydb.cursor()
    cur.execute(f"Delete from student where reg_no = {r_var.get()}")
    mydb.commit()
    mydb.close
    get_data()
    clear()
    messagebox.showinfo("Update","Successfully deleted the record")
def search():
    mydb = a.connect(host="localhost",user="root",password="Mysql@1234",database="stud")
    cur = mydb.cursor()
    cur.execute("select * from student where "+str(search_var.get())+" LIKE '%"+str(s_var.get())+"%'")
    rows = cur.fetchall()
    if len(rows)!=0:
        S_table.delete(*S_table.get_children())
        for row in rows:
            S_table.insert('',END,values=row)
        mydb.commit()
    mydb.close() 
#------------------FRAME 1--------------------------
title = Label(text="Student Management System",bd=12,relief=GROOVE,bg="green",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
F1 = LabelFrame(text="Student Details",bg="dark turquoise",fg="purple",font=("times new roman",20,"bold"))
F1.place(x=20,y=100,width=490,height=700)
#------------------Student Deatils--------------------------
name_lbl = Label(F1,text="Name",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
name_lbl.grid(row=0,column=0,padx=30,pady=15)
name_txt = Entry(F1,width=20,font="arial 15 bold",textvariable=n_var)
name_txt.grid(row=0,column=1,padx=30,pady=15)

regno_lbl = Label(F1,text="Registration No.",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
regno_lbl.grid(row=1,column=0,padx=30,pady=15)
regno_txt = Entry(F1,width=20,font="arial 15 bold",textvariable=r_var)
regno_txt.grid(row=1,column=1,padx=30,pady=15)

dob_lbl = Label(F1,text="Date of Birth",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
dob_lbl.grid(row=2,column=0,padx=30,pady=15)
#dob = DateEntry(F1,background="dark blue",state='readonly')
#dob.grid(row=5,column=1,padx=30,pady=15)
dob_txt = Entry(F1,width=20,font="arial 15 bold",textvariable=dob_var)
dob_txt.grid(row=2,column=1,padx=30,pady=15)

gender_lbl = Label(F1,text="Gender",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
gender_lbl.grid(row=3,column=0,padx=30,pady=15)
cgender = ttk.Combobox(F1,font=("times new roman",15,"bold"),state='readonly',textvariable=g_var)
cgender['values'] = ("Male","Female","Others")
cgender.grid(row=3,column=1,padx=30,pady=15)

email_lbl = Label(F1,text="Email",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
email_lbl.grid(row=5,column=0,padx=30,pady=15)
email_txt = Entry(F1,width=20,font="arial 15 bold",textvariable=e_var)
email_txt.grid(row=5,column=1,padx=30,pady=15)

contact_lbl = Label(F1,text="Contact No.",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
contact_lbl.grid(row=4,column=0,padx=30,pady=15)
contact_txt = Entry(F1,width=20,font="arial 15 bold",textvariable=c_var)
contact_txt.grid(row=4,column=1,padx=30,pady=15)

address_lbl = Label(F1,text="Address",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
address_lbl.grid(row=6,column=0,padx=30,pady=15)
address_txt = Text(F1,width=20,height=3,font="arial 15 bold")
address_txt.grid(row=6,column=1,padx=30,pady=15)
#------------------Buttons--------------------------
btn1 = Button(F1,text="Add",font="arial 15 bold",bg='coral1',width=10,command=add_data)
btn1.grid(row=7,column=0)  

btn2 = Button(F1,text="Update",font="arial 15 bold",bg='coral1',width=10,command=update)
btn2.grid(row=7,column=1) 

btn3 = Button(F1,text="Delete",font="arial 15 bold",bg='coral1',fg="black",width=10,command=delete)
btn3.grid(row=8,column=0,padx=20,pady=30) 

btn4 = Button(F1,text="Clear",font="arial 15 bold",bg='Black',fg="white",width=10,command=clear)
btn4.grid(row=8,column=1,padx=20,pady=30)
#------------------FRAME 2--------------------------
F2 = Frame(root,relief=GROOVE,bd=8,bg="dark turquoise")
F2.place(x=575,y=100,width=910,height=700)
#------------------Search and Details--------------------------
search_lbl = Label(F2,text="Search By",font=("times new roman",15,"bold"),bg="dark turquoise",fg="black")
search_lbl.grid(row=0,column=0,padx=10,pady=8)
csearch = ttk.Combobox(F2,font=("times new roman",15,"bold"),state='readonly',textvariable=search_var)
csearch['values'] = ("Reg_no","Name","Contact","DOB")
csearch.grid(row=0,column=1,padx=10,pady=8)
search_txt = Entry(F2,width=20,font="arial 15 bold",textvariable=s_var)
search_txt.grid(row=0,column=2,padx=10,pady=8)
#------------------Buttons--------------------------
btn5 = Button(F2,text="Search",font="arial 15 bold",bg='gray50',fg="black",width=10,command=search)
btn5.grid(row=0,column=3,padx=10,pady=8) 

btn6 = Button(F2,text="Display All",font="arial 15 bold",bg='gray50',fg="black",width=10,command=get_data)
btn6.grid(row=0,column=4,padx=10,pady=8)
#------------------FRAME 3--------------------------
F3 = Frame(F2,relief=GROOVE,bd=4,bg="dark turquoise")
F3.place(x=10,y=70,width=870,height=600)
scroll_x = Scrollbar(F3,orient=HORIZONTAL)
scroll_y = Scrollbar(F3,orient=VERTICAL)
S_table = ttk.Treeview(F3,columns=("name","reg_no","dob","gender","contact","email","addr"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=S_table.xview)
scroll_y.config(command=S_table.yview)
S_table.heading("name",text="Name")
S_table.heading("reg_no",text="Registration Number")
S_table.heading("dob",text="Date of Birth")
S_table.heading("gender",text="Gender")
S_table.heading("contact",text="Contact")
S_table.heading("email",text="Email")
S_table.heading("addr",text="Address")
S_table['show'] = 'headings'
S_table.pack(fill=BOTH,expand=1)
S_table.bind("<ButtonRelease-1>",get_value)
get_data()
root.mainloop()