from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+100+50")

        title = Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("ARIAL",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

#Variable used

        self.Roll_no_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.Dob_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


#MANAGE FRAME

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_frame,text="Manage Students",font=("ARIAL",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_frame,text="Roll_no",font=("ARIAL",20,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_frame,textvariable=self.Roll_no_var, font=("ARIAL",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_frame, text="Name", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_frame,textvariable=self.Name_var, font=("ARIAL", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_frame, text="Email", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_frame,textvariable=self.Email_var, font=("ARIAL", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_frame, text="Gender", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.Gender_var,font=("ARIAL", 13, "bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")


        lbl_Contact = Label(Manage_frame, text="Contact", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_frame,textvariable=self.Contact_var, font=("ARIAL", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_frame, text="DOB", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(Manage_frame,textvariable=self.Dob_var, font=("ARIAL", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_frame, text="Address", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address=Text(Manage_frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

#BUTTON FRAME

        Button_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="crimson")
        Button_frame.place(x=10, y=530, width=420)

        Addbtn=Button(Button_frame,text="Add",width=10,command=self.Add_Students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(Button_frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(Button_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
        clearbtn = Button(Button_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)

#Detail frame

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_frame.place(x=500, y=100, width=830, height=600)

        lbl_Search = Label(Detail_frame, text="Search By", font=("ARIAL", 20, "bold"), bg="crimson", fg="white")
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_frame, font=("ARIAL", 13, "bold"),textvariable=self.search_by,width=10, state="readonly")
        combo_Search['values'] = ("Roll_no", "Name", "Contact")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_Search = Entry(Detail_frame,width=15,textvariable=self.search_txt,font=("ARIAL", 13, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showbtn = Button(Detail_frame, text="Show", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

#Table Frame

        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg="crimson")
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Student_Table=ttk.Treeview(Table_frame,columns=("Roll","Name","Email","Gender","Contact","Dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Roll",text="Roll no.")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Email", text="Email")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("Dob", text="DOB.")
        self.Student_Table.heading("Address", text="Address.")
        self.Student_Table['show']="headings"
        self.Student_Table.column("Roll",width=100)
        self.Student_Table.column("Name", width=100)
        self.Student_Table.column("Email", width=100)
        self.Student_Table.column("Gender", width=100)
        self.Student_Table.column("Contact", width=100)
        self.Student_Table.column("Dob", width=100)
        self.Student_Table.column("Address", width=100)
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#Add_Students used to insert the record in Database

    def Add_Students(self):
        if self.Roll_no_var.get()=="" or self.Name_var.get=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.Dob_var.get=="" :
            messagebox.showerror("Eror","Alll fields are required")
        else:
            con=pymysql.connect(host="localhost",user="testuser",password="test123",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
                                                                               self.Name_var.get(),
                                                                               self.Email_var.get(),
                                                                               self.Gender_var.get(),
                                                                               self.Contact_var.get(),
                                                                               self.Dob_var.get(),
                                                                               self.txt_Address.get('1.0',END)
                                                                              ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Succes","Recorcd has been inserted")

# Fetch_data used to show all records from Database


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="testuser", password="test123", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            con.commit()
        con.close()

#Clear is used to clear all the entries on manage frame

    def clear(self):
        self.Roll_no_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.Dob_var.set("")
        self.txt_Address.delete('1.0', END)

#get_cursor is used to fetch the data from detail frame to manage frame

    def get_cursor(self,e):
        cursor_row=self.Student_Table.focus()
        content=self.Student_Table.item(cursor_row)
        row=content['values']
        self.Roll_no_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.Dob_var.set(row[5])
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END,row[6])

#Update_data is used to modify the data of existing student

    def update_data(self):
        con = pymysql.connect(host="localhost", user="testuser", password="test123", database="stm")
        cur = con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,Dob=%s,Address=%s,Roll_no=%s", (
                                                                          self.Name_var.get(),
                                                                          self.Email_var.get(),
                                                                          self.Gender_var.get(),
                                                                          self.Contact_var.get(),
                                                                          self.Dob_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.Roll_no_var.get()
                                                                          ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

# Delete_data is used to delete the data of existing student

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="testuser", password="test123", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where Roll_no=%s",self.Roll_no_var.get())
        con.commit()
        con.close()
        messagebox.showinfo("Succes", "Recorcd Deleted")

        self.fetch_data()
        self.clear()

# Search_data is used to search the data of existing student


    def search_data(self):
        con = pymysql.connect(host="localhost", user="testuser", password="test123", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
            con.commit()
        con.close()


root=Tk()
ob=Student(root)
root.mainloop()

