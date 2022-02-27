from tkinter import *
from tkinter import ttk

import pymysql
import tkinter.messagebox as MessageBox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management Model")
        self.root.geometry("1350x700+0+0")

        title =Label(self.root,text="Student Management Model",relief=GROOVE,bd=10,font=("times new romans",40,"bold"),
                     bg="yellow")
        title.pack(side=TOP,fill=X)

        #=================All Variables=================================================================================
        self.roll_no_var =StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

        # =======================Manage Frame===========================================================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg='#003e53')
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title = Label(Manage_Frame,text="Manage Students",bg='#003e53',fg='white',font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll =Label(Manage_Frame,text="Roll No.",bg='#003e53',fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        text_roll = Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        text_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name",bg='#003e53',fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        text_name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        text_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        text_email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        text_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_Frame, text="Contact", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        text_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        text_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dbo = Label(Manage_Frame, text="D.O.B", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_dbo.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        text_dbo = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        text_dbo.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.text_address = Text(Manage_Frame,width=30,height=4, font=("", 10))
        self.text_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        # ===========================frame Button=======================================================================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='#003e53')
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame,text="Add",width=10, command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



        # ================Students Details Frame========================================================================

        details_Frame = Frame(self.root, bd=4, relief=RIDGE,bg='#003e53')
        details_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(details_Frame, text="Search By", bg='#003e53', fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(details_Frame,width=10,textvariable=self.search_by, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        text_search = Entry(details_Frame,width=20,textvariable=self.search_text, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        text_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(details_Frame, text="Search", width=10,pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(details_Frame, text="Show All", width=10,pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        loginoutbtn = Button(details_Frame, text="LogOut", width=10, pady=5, command=root.destroy).grid(row=0,
                                                                                                            column=5,
                                                                                                            padx=7,
                                                                                                            pady=10)


        #================= Student Updated Profile Frame================================================================

        Table_frame =Frame(details_Frame,bd=4,relief=RIDGE,bg="#003e53")
        Table_frame.place(x=10,y=70,width=760,height=500)

        scroll_x = Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("roll","Name","Email","Gender","Contact","DOB","Address")
                                   ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("DOB", text="D.O.B")
        self.student_table.heading("Address", text="Address")

        self.student_table['show'] ='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=130)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Contact", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Address", width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

# ================================FUNCTION ADD STUDENTS DETAILS=========================================================
    def add_student(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="smt")
        cur = con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.text_address.get('1.0',END)
        ))
        MessageBox.showinfo("Student Status", "Submitted Successful")
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

# ==================================FUNCTION TO FETCH STUDENTS DATA=====================================================
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="smt")
        cur = con.cursor()
        cur.execute("select *from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


# ==========================FUNCTION TO CLEAR STUDENTS DATA============================================================
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_address.delete("1.0", END)
        self.text_address.insert(END,row[6])

# ===============================FUNCTION TO UPDATE STUDENTS DATA========================================================
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="smt")
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                self.name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.text_address.get('1.0',END),
                                                                                                self.roll_no_var.get(),
                                                                                                    ))
        MessageBox.showinfo("Update Status", "Student Data Updated Successfully")
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


# ===================================FUNCTION TO DELETE STUDENTS DATA==================================================
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="smt")
        cur = con.cursor()
        cur.execute("delete from student where roll_no=%s",self.roll_no_var.get())
        MessageBox.showinfo("Delete Status", "Student Data Successfully Deleted")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
# ================FUNCTION TO SEARCH FOR A PARTICULAR STUDENT USING EITHER ROLL-NO,NAME,CONTACT=========================
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="smt")
        cur = con.cursor()

        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
root = Tk()
ob = Student(root)
root.mainloop()