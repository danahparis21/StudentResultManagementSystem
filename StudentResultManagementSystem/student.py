from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3


#RMS = SGS
class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+170+220")
        self.root.config(bg="white")
        self.root.focus_force()


        #====TITLE====#
        title = Label(self.root, 
                      text="Manage Student Details" ,
                      font =("Helvetica",20,"bold"),
                      bg="#033054",fg="white").place(x=10,y=15,width=1181,height=35) 
        
        #===VARIABLES===#
        self.var_studentID = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_a_date=StringVar()
        self.var_city=StringVar()
        self.var_province=StringVar()
        self.var_region=StringVar()



        #=========WIDGETS=========#
        self.course_list=[]
       
        self.txt_course = Listbox(self.root, selectmode=MULTIPLE, 
                                  font=("Helvetica", 15, ), bg="lightyellow", bd=0, relief=SOLID)
        self.txt_course.place(x=480, y=180, width=200, height=100)
        self.fetch_course()

        #======COLUMN1======#
        lbl_studentID=  Label(self.root, 
                      text="Student No." ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=60) 
        lbl_name =  Label(self.root, 
                      text="Name" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=100) 
        lbl_email =  Label(self.root, 
                      text="Email" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=140) 
        lbl_gender =  Label(self.root, 
                      text="Gender" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=180) 
        
        lbl_city =  Label(self.root, 
                      text="City" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=300)
        txt_city =  Entry(self.root, textvariable=self.var_city,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=150,y=300,width=120) 
        
        lbl_province =  Label(self.root, 
                      text="Province" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=280,y=300)
        txt_province =  Entry(self.root, textvariable=self.var_province,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=370,y=300,width=100)
        
        lbl_region =  Label(self.root, 
                      text="Region" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=490,y=300)
        txt_region =  Entry(self.root, textvariable=self.var_region,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=560,y=300,width=120)
        
        lbl_address =  Label(self.root, 
                      text="Address" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=10,y=340)
        
        #==ENTRY FIELDS==#
        self.txt_studentID =  Entry(self.root, textvariable=self.var_studentID,
                                    font=("Helvetica", 15),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_studentID.place(x=150,y=60,width=200) 
        txt_name=  Entry(self.root, textvariable=self.var_name,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=150,y=100, width=200) 
        txt_email =  Entry(self.root, textvariable=self.var_email,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=150,y=140,width=200) 
        self.txt_gender=  ttk.Combobox(self.root, textvariable=self.var_gender,values=("Male","Female","Other"),
                      font =("Helvetica",15,),
                      state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180, width=200) 
        self.txt_gender.set("Select")
        
        
        
        #======COLUMN2======#
        lbl_dob=  Label(self.root, 
                      text="Date of Bith" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=360,y=60) 
        lbl_contact =  Label(self.root, 
                      text="Contact" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=360,y=100) 
        lbl_admissio =  Label(self.root, 
                      text="Admission" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=360,y=140) 
        lbl_course =  Label(self.root, 
                      text="Course" ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=360,y=180) 
        
        #==ENTRY FIELDS==#
        self.txt_dob =  Entry(self.root, textvariable=self.var_dob,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=480,y=60,width=200) 
        txt_contact=  Entry(self.root, textvariable=self.var_contact,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=480,y=100, width=200) 
        txt_admission =  Entry(self.root, textvariable=self.var_a_date,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID).place(x=480,y=140,width=200) 
        
        #======TEXT ADDRESS=====#
        self.txt_address =  Text(self.root, 
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_address.place(x=150,y=340, width=540, height=50) 

                      
        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Save', "#191862", "#007bff", 150, 400, self.add, relief=SOLID, bd=0) 
        self.create_button(self.root, 'Update', "#191862", "#28a745", 270, 400, self.update, relief=SOLID, bd=0)
        self.create_button(self.root, 'Delete', "#191862", "#dc3545", 390, 400, self.delete, relief=SOLID, bd=0)
        self.create_button(self.root, 'Clear', "#191862", "#607d8b", 510, 400, self.clear, relief=SOLID, bd=0)


        #===SEARCH PANEL===#
        self.var_search=StringVar()

        lbl_search_studentID =  Label(self.root, 
                      text="Student No. " ,
                      font =("Helvetica",15,"bold"),
                      bg="white").place(x=720,y=60)
        txt_search_studentID=  Entry(self.root, textvariable=self.var_search,
                      font =("Helvetica",15,),
                      bg="#ecf0f1", bd=0, relief=SOLID).place(x=905,y=60,width=170) 
        btn_search = Button(self.root, text='Search', 
                            font=("Helvetica", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1080,y=60,width=110,height=28)

        #==-CONTENT FOR TREEVIEW TABLE===#
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("studentID", "name", "email", "gender", "dob", "contact", "admission", "city", "province", "region", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill = Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        #===HEADING===#      
        self.CourseTable.heading("studentID", text="Student No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="Date of Birth")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("province", text="Province")
        self.CourseTable.heading("region", text="Region")
        self.CourseTable.heading("address", text="Address")
        self.CourseTable["show"] = 'headings'

        #===CONTENT===#      
        self.CourseTable.column("studentID", width = 60)
        self.CourseTable.column("name", width = 100)
        self.CourseTable.column("email", width = 100)
        self.CourseTable.column("gender", width = 100)
        self.CourseTable.column("dob", width = 150)
        self.CourseTable.column("contact", width = 150)
        self.CourseTable.column("admission", width = 150)
        self.CourseTable.column("city", width = 150)
        self.CourseTable.column("province", width = 150)
        self.CourseTable.column("region", width = 150)
        self.CourseTable.column("address", width = 150)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        

#===========================================================

    #===BUTTON DESIGN===#      
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

    #===CLEAR ENTRY FIELDS===#      
    def clear(self):
        self.show()  # Show the updated list of students (if applicable)
        
        # Reset StringVars
        self.var_studentID.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select") 
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_city.set("")
        self.var_province.set("")
        self.var_region.set("")
        self.var_search.set("")

        self.txt_address.delete("1.0", END)  
        # studentID field IS editable
        self.txt_studentID.config(state=NORMAL)
        self.txt_gender.set("Select")


    #===DELETE A STUDENT===#      
    def delete(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            if self.var_studentID.get() == "":
                messagebox.showerror("Error", "Student Number is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE studentID = ?", (self.var_studentID.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please Select a Student from the List", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        # Deleting related entries in student_course
                        cur.execute("DELETE FROM student_course WHERE studentID = ?", (self.var_studentID.get(),))
                        
                        # Deleting the student record
                        cur.execute("DELETE FROM student WHERE studentID = ?", (self.var_studentID.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                        self.clear()  # Clear the fields after deletion
                        self.show()  # Refresh the student list
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
        finally:
            con.close()



    #===FETCH DATA TO AUTOMATICALLY DISPLAY IN ENTRY FIELDS===#      
    def get_data(self, ev):
        self.txt_studentID.config(state="readonly")
        
        r = self.CourseTable.focus()
        if not r:  # Ensure there's a selected row
            return
        
        content = self.CourseTable.item(r)
        row = content["values"]

        self.var_studentID.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_city.set(row[7])
        self.var_province.set(row[8])
        self.var_region.set(row[9])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[10])

        # Fetch the courses the student is enrolled in from the database
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            
            student_id = self.var_studentID.get()
            cur.execute("""
                SELECT course.name FROM course
                JOIN student_course ON course.cid = student_course.cid
                WHERE student_course.studentID = ?
            """, (student_id,))
            courses = cur.fetchall()
            # Add all courses to the Listbox 
            enrolled_courses = [course[0] for course in courses]


            for index in range(self.txt_course.size()):
                course_name = self.txt_course.get(index)
                if course_name in enrolled_courses:
                    self.txt_course.select_set(index)  # Select the enrolled courses

        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching courses: {str(ex)}")

        finally:
            con.close()


    #===ADD A STUDENT===#      
    def add(self):
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "" or self.var_email.get() == "":
                messagebox.showerror("Error", "Name and Email are required", parent=self.root)
                return
            # Insert student details
            cur.execute(
                "INSERT INTO student (name, email, gender, dob, contact, admission, city, province, region, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_city.get(),
                    self.var_province.get(),
                    self.var_region.get(),
                    self.txt_address.get("1.0", END).strip(),
                ),
            )
            student_id = cur.lastrowid
    
            selected_courses = self.txt_course.curselection()
            
            for course_index in selected_courses:
                course_name = self.txt_course.get(course_index)
                print(course_name)  
            for i in selected_courses:
                course_name = self.txt_course.get(i)
                cur.execute("SELECT cid FROM course WHERE name = ?", (course_name,))
                course_id = cur.fetchone()[0]
                cur.execute("INSERT INTO student_course (studentID, cid) VALUES (?, ?)", (student_id, course_id))

            con.commit()
            messagebox.showinfo("Success", "Student added successfully", parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


    #===UPDATE STUDENT DETAILS===#      
    def update(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            if self.var_studentID.get() == "":
                messagebox.showerror("Error", "Student Number is required", parent=self.root)
            else:
                # Check if student exists
                cur.execute("SELECT * FROM student WHERE studentID = ?", (self.var_studentID.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select student from List", parent=self.root)
                else:
                    cur.execute("UPDATE student SET name=?, email=?, gender=?, dob=?, contact=?, admission=?, city=?, province=?, region=?, address=? WHERE studentID=?", 
                                (
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_contact.get(),
                                    self.var_a_date.get(),
                                    self.var_city.get(),
                                    self.var_province.get(),
                                    self.var_region.get(),
                                    self.txt_address.get("1.0", END),
                                    self.var_studentID.get()
                                ))

                    # Retrieve the selected courses from the Listbox
                    selected_courses = self.txt_course.curselection()
                    
                    # Remove old courses for the student
                    cur.execute("DELETE FROM student_course WHERE studentID = ?", (self.var_studentID.get(),))
    
                    # Insert the new courses for the student
                    for course_index in selected_courses:
                        course_name = self.txt_course.get(course_index)
                        cur.execute("SELECT cid FROM course WHERE name = ?", (course_name,))
                        course_id = cur.fetchone()[0]  # Get courseID
                        cur.execute("INSERT INTO student_course (studentID, cid) VALUES (?, ?)", 
                                    (self.var_studentID.get(), course_id))

                    con.commit()
                    messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                    self.show()  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    #===SHOW STUDENT DETAILS TO TABLE===#
    def show(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM student")  # Query to get all students
            rows = cur.fetchall()

            # Clear existing data in the table
            self.CourseTable.delete(*self.CourseTable.get_children())

            # Insert new rows into the table
            for row in rows:
                self.CourseTable.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
        finally:
            con.close()

    #===FETCH COURSE FOR LIST BOX===#
    def fetch_course(self):
        self.course_list.clear()
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
            self.txt_course.delete(0, END)
            for row in rows:
                self.txt_course.insert(END, row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===SEARCH BY STUDENT ID===#
    def search(self):
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Student ID is required", parent=self.root)
                return
            
            cur.execute("SELECT * FROM student WHERE studentID = ?", (self.var_search.get(),))
            student = cur.fetchone()
            if student:
                self.txt_studentID.delete(0, END)
                self.txt_studentID.insert(0, student[0])
                self.var_name.set(student[1])
                self.var_email.set(student[2])
                self.var_gender.set(student[3])
                self.var_dob.set(student[4])
                self.var_contact.set(student[5])
                self.var_a_date.set(student[6])
                self.var_city.set(student[7])
                self.var_province.set(student[8])
                self.var_region.set(student[9])
                self.txt_address.delete("1.0", END)
                self.txt_address.insert("1.0", student[10])

                cur.execute("SELECT c.name FROM student_course sc JOIN course c ON sc.cid = c.cid WHERE sc.studentID = ?", (student[0],))
                courses = cur.fetchall()
                self.txt_course.delete(0, END)
                for course in courses:
                    self.txt_course.insert(END, course[0])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == '__main__':
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()
