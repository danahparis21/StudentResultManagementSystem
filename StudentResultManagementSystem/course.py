from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+170+220")
        self.root.config(bg="white")
        self.root.focus_force()

        #====TITLE====#
        title = Label(self.root,
                      text="Manage Course Details",
                      font=("Helvetica", 20, "bold"),
                      bg="#191862", fg="white").place(x=10, y=15, width=1181, height=35)

        #===VARIABLES===#
        self.var_courses = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        #==WIDGETS==#
        lbl_courseName = Label(self.root,
                               text="Course Name",
                               font=("Helvetica", 15, "bold"),
                               bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root,
                             text="Duration",
                             font=("Helvetica", 15, "bold"),
                             bg="white").place(x=10, y=100)
        lbl_charges = Label(self.root,
                            text="Charges",
                            font=("Helvetica", 15, "bold"),
                            bg="white").place(x=10, y=140)
        lbl_description = Label(self.root,
                                text="Description",
                                font=("Helvetica", 15, "bold"),
                                bg="white").place(x=10, y=180)

        #==ENTRY FIELDS==#
        self.txt_courseName = Entry(self.root, textvariable=self.var_courses,
                                    font=("Helvetica", 15),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_courseName.place(x=150, y=60, width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration,
                             font=("Helvetica", 15),
                             bg="lightyellow", bd=0, relief=SOLID).place(x=150, y=100, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges,
                            font=("Helvetica", 15),
                            bg="lightyellow", bd=0, relief=SOLID).place(x=150, y=140, width=200)
        self.txt_description = Text(self.root,
                                    font=("Helvetica", 15),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_description.place(x=150, y=180, width=500, height=130)

        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Save', "#191862", "#007bff", 150, 400, self.add, relief=SOLID, bd=0) 
        self.create_button(self.root, 'Update', "#191862", "#28a745", 270, 400, self.update, relief=SOLID, bd=0)
        self.create_button(self.root, 'Delete', "#191862", "#dc3545", 390, 400, self.delete, relief=SOLID, bd=0)
        self.create_button(self.root, 'Clear', "#191862", "#607d8b", 510, 400, self.clear, relief=SOLID, bd=0)


        #===SEARCH PANEL===#
        self.var_search = StringVar()

        lbl_search_courseName = Label(self.root,
                                      text="Search Course Name: ",
                                      font=("Helvetica", 15, "bold"),
                                      bg="white").place(x=715, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search,
                                      font=("Helvetica", 15),
                                      bg="#ecf0f1", bd=0, relief=SOLID).place(x=925, y=60, width=150)
        btn_search = Button(self.root, text='Search',
                            font=("Helvetica", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1080, y=60, width=110, height=28)

        #==-CONTENT===#
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#ecf0f1")
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("cid", width=60)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


#===========================================================

    #===BUTTON DESIGNS===#
    def create_button(self, parent, text, bg_color, hover_color, x, y, command, relief=SOLID, bd=0):
        btn = Button(
            parent,
            text=text,
            font=("Helvetica", 15),
            bg=bg_color,
            fg="white",
            cursor="hand2",
            command=command,
            relief=relief,  
            bd=bd  
        )
        btn.place(x=x, y=y, width=120, height=40)
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))


    #===CLEAR INPUTS===#
    def clear(self):
        self.show()
        self.var_courses.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        #self.var_courses.set("")

        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

    #===DELETE A COURSE===#
    def delete(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            if self.var_courses.get()=="":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name = ?",(self.var_courses.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please Select a Course from the List", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=?",(self.var_courses.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===AUTOMATICALLY DISPLAY DATA BY CLICKING FROM TABLE===#
    def get_data(self,ev):
        self.txt_courseName.config(state="readonly")

    
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)

        self.var_courses.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_courses.set(row[4])

        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END, row[4])

        


    #===ADD A COURSE===#
    def add(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            if self.var_courses.get()=="":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name = ?",(self.var_courses.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("insert into course(name, duration, charges, description) values(?,?,?,?)", 
                                (self.var_courses.get(),
                                 self.var_duration.get(),
                                 self.var_charges.get(),
                                 self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===UPDATE COURSE DETAILS===#
    def update(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            if self.var_courses.get()=="":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name = ?",(self.var_courses.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=?", 
                                (
                                 self.var_duration.get(),
                                 self.var_charges.get(),
                                 self.txt_description.get("1.0", END),
                                 self.var_courses.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Update Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===SHOW DETAILS IN TABLE===#
    def show(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            cur.execute("select * from course ")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values = row)
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===SEARCH COURSE===#
    def search(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values = row)
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        
        
#===RUN FILE===#
if __name__ == '__main__':
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()
