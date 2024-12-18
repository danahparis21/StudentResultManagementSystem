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
        self.edit_mode = False


        #====TITLE====#
        title = Label(self.root, 
                      text="Manage Student Details" ,
                      font =("Garamond",17,"bold"),
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
        self.subject_list=[]
       
        self.txt_subject = Listbox(self.root, selectmode=MULTIPLE, 
                                  font=("Helvetica", 13, ), bg="lightyellow", bd=0, relief=SOLID)
        self.txt_subject.place(x=480, y=180, width=200, height=100)
        self.fetch_subject()

        #======COLUMN1======#
        lbl_studentID=  Label(self.root, 
                      text="LRN" ,
                      font =("Helvetica",13, "bold"),
                      bg="white").place(x=10,y=60) 
        lbl_name =  Label(self.root, 
                      text="Name" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=10,y=100) 
        lbl_email =  Label(self.root, 
                      text="Email" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=10,y=140) 
        lbl_gender =  Label(self.root, 
                      text="Sex" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=10,y=180) 
        
        lbl_city =  Label(self.root, 
                      text="City" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=10,y=300)
        self.txt_city =  Entry(self.root, textvariable=self.var_city,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_city.place(x=150,y=300,width=120) 
        
        lbl_province =  Label(self.root, 
                      text="Province" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=280,y=300)
        self.txt_province =  Entry(self.root, textvariable=self.var_province,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_province.place(x=370,y=300,width=100)
        
        lbl_region =  Label(self.root, 
                      text="Region" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=490,y=300)
        self.txt_region =  Entry(self.root, textvariable=self.var_region,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_region.place(x=560,y=300,width=120)
        
        lbl_address =  Label(self.root, 
                      text="Address" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=10,y=340)
        
        #==ENTRY FIELDS==#
        self.txt_studentID =  Entry(self.root, textvariable=self.var_studentID,
                                    font=("Helvetica", 15),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_studentID.place(x=150,y=60,width=200) 
        self.txt_name=  Entry(self.root, textvariable=self.var_name,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_name.place(x=150,y=100, width=200) 
        self.txt_email =  Entry(self.root, textvariable=self.var_email,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_email.place(x=150,y=140,width=200) 
        self.txt_gender=  ttk.Combobox(self.root, textvariable=self.var_gender,values=("Male","Female"),
                      font =("Helvetica",15,),
                      state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180, width=200) 
        self.txt_gender.set("Select")
        
        
        
        #======COLUMN2======#
        lbl_dob=  Label(self.root, 
                      text="Date of Bith" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=360,y=60) 
        lbl_contact =  Label(self.root, 
                      text="Contact" ,
                      font =("Helvetica",13, "bold"),
                      bg="white").place(x=360,y=100) 
        lbl_admissio =  Label(self.root, 
                      text="Admission" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=360,y=140) 
        lbl_subject =  Label(self.root, 
                      text="Subject" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=360,y=180) 
        
        #==ENTRY FIELDS==#
        self.txt_dob =  Entry(self.root, textvariable=self.var_dob,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_dob.place(x=480,y=60,width=200) 
        self.txt_contact=  Entry(self.root, textvariable=self.var_contact,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_contact.place(x=480,y=100, width=200) 
        self.txt_admission =  Entry(self.root, textvariable=self.var_a_date,
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_admission.place(x=480,y=140,width=200) 
        
        #======TEXT ADDRESS=====#
        self.txt_address =  Text(self.root, 
                      font =("Helvetica",15,),
                      bg="lightyellow", bd=0, relief=SOLID)
        self.txt_address.place(x=150,y=340, width=540, height=50) 

                      
        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Save', "#191862", "#007bff", 150, 420, self.add, relief=SOLID, bd=0) 
        self.update_button = self.create_button(
        self.root, 'Update', "#191862", "#28a745", 270, 420, 
        self.toggle_edit_mode, relief=SOLID, bd=0
    )
        self.create_button(self.root, 'Delete', "#191862", "#dc3545", 390, 420, self.delete, relief=SOLID, bd=0)
        self.create_button(self.root, 'Clear', "#191862", "#607d8b", 510, 420, self.clear, relief=SOLID, bd=0)


        #===SEARCH PANEL===#
        self.var_search=StringVar()

        lbl_search_studentID =  Label(self.root, 
                      text="LRN" ,
                      font =("Helvetica",13,"bold"),
                      bg="white").place(x=720,y=60)
        self.txt_search_studentID=  Entry(self.root, textvariable=self.var_search,
                      font =("Helvetica",15,),
                      bg="#ecf0f1", bd=0, relief=SOLID)
        self.txt_search_studentID.place(x=780,y=60,width=200) 
        btn_search = Button(self.root, text='⌕', 
                            font=("Times New Roman", 13, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=990,y=60,width=70,height=25)

        #==-CONTENT FOR TREEVIEW TABLE===#
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.subjectTable = ttk.Treeview(self.C_Frame, columns=("studentID", "name", "email", "gender", "dob", "contact", "admission", "city", "province", "region", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill = Y)
        scrollx.config(command=self.subjectTable.xview)
        scrolly.config(command=self.subjectTable.yview)

        #===HEADING===#      
        self.subjectTable.heading("studentID", text="Student No.")
        self.subjectTable.heading("name", text="Name")
        self.subjectTable.heading("email", text="Email")
        self.subjectTable.heading("gender", text="Gender")
        self.subjectTable.heading("dob", text="Date of Birth")
        self.subjectTable.heading("contact", text="Contact")
        self.subjectTable.heading("admission", text="Admission")
        self.subjectTable.heading("city", text="City")
        self.subjectTable.heading("province", text="Province")
        self.subjectTable.heading("region", text="Region")
        self.subjectTable.heading("address", text="Address")
        self.subjectTable["show"] = 'headings'

        #===CONTENT===#      
        self.subjectTable.column("studentID", width = 60)
        self.subjectTable.column("name", width = 100)
        self.subjectTable.column("email", width = 100)
        self.subjectTable.column("gender", width = 100)
        self.subjectTable.column("dob", width = 150)
        self.subjectTable.column("contact", width = 150)
        self.subjectTable.column("admission", width = 150)
        self.subjectTable.column("city", width = 150)
        self.subjectTable.column("province", width = 150)
        self.subjectTable.column("region", width = 150)
        self.subjectTable.column("address", width = 150)

        self.subjectTable.pack(fill=BOTH,expand=1)
        self.subjectTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        

#===========================================================

    #===BUTTON DESIGN===#      
    def create_button(self, parent, text, bg_color, hover_color, x, y, command, relief=SOLID, bd=0):
        btn = Button(
            parent,
            text=text,
            font=("Times New Roman", 13),
            bg=bg_color,
            fg="white",
            cursor="hand2",
            command=command,
            relief=relief, 
            bd=bd 
        )
        btn.place(x=x, y=y, width=100, height=30)
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        return btn

    #===CLEAR ENTRY FIELDS===#      
    def clear(self):
        self.show() 
        
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

        
        self.txt_address.config(state="normal") 
        self.txt_address.delete("1.0", END)  
        self.txt_address.config(state="normal", background="lightyellow")  

        # Set fields back to normal
        self.txt_studentID.config(state="normal")
        self.txt_gender.set("Select")
        self.txt_studentID.config(state="normal")
        self.txt_address.config(state="normal", background="lightyellow")
        self.txt_admission.config(state="normal")
        self.txt_name.config(state="normal")
        self.txt_email.config(state="normal")
        self.txt_dob.config(state="normal")
        self.txt_contact.config(state="normal")
        self.txt_city.config(state="normal")
        self.txt_province.config(state="normal")
        self.txt_region.config(state="normal")
        self.txt_search_studentID.config(state="normal")
        self.txt_subject.config(state="normal")


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
                       
                        cur.execute("DELETE FROM student_subject WHERE studentID = ?", (self.var_studentID.get(),))
           
                        cur.execute("DELETE FROM student WHERE studentID = ?", (self.var_studentID.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                        self.clear() 
                        self.show()  
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
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
    
            selected_subjects = self.txt_subject.curselection()
            
            for subject_index in selected_subjects:
                subject_name = self.txt_subject.get(subject_index)
                print(subject_name)  
            for i in selected_subjects:
                subject_name = self.txt_subject.get(i)
                cur.execute("SELECT subjectID FROM subject WHERE name = ?", (subject_name,))
                subject_id = cur.fetchone()[0]
                cur.execute("INSERT INTO student_subject (studentID, subjectID) VALUES (?, ?)", (student_id, subject_id))

            con.commit()
            messagebox.showinfo("Success", "Student added successfully", parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    #===FETCH DATA TO AUTOMATICALLY DISPLAY IN ENTRY FIELDS===#      
    def get_data(self, ev):
        #everything is non editable 
        self.txt_studentID.config(state="readonly") 
        self.txt_address.config(state="disabled", background="#f0f0f0")  
        self.txt_admission.config(state="readonly")
        self.txt_name.config(state="readonly")  
        self.txt_email.config(state="readonly")  
        self.txt_gender.config(state="readonly")  
        self.txt_dob.config(state="readonly")
        self.txt_contact.config(state="readonly") 
        self.txt_city.config(state="readonly") 
        self.txt_province.config(state="readonly") 
        self.txt_region.config(state="readonly") 
        self.txt_search_studentID.config(state="readonly") 
        self.txt_subject.config(state="disabled")

        self.update_button.config(text="Update") 
        r = self.subjectTable.focus()
        if not r:
            return

        content = self.subjectTable.item(r)
        row = content["values"]

        if row:
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
            
            self.txt_address.config(state="normal", background="#f0f0f0")  
            self.txt_address.delete('1.0', END) 
            self.txt_address.insert(END, row[10])  
            self.txt_address.config(state="disabled", background="#f0f0f0")  
      
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            student_id = self.var_studentID.get()
            cur.execute(""" 
                SELECT subject.name FROM subject
                JOIN student_subject ON subject.subjectID = student_subject.subjectID
                WHERE student_subject.studentID = ?
            """, (student_id,))
            subjects = cur.fetchall()

            enrolled_subjects = [subject[0] for subject in subjects]

            for index in range(self.txt_subject.size()):
                subject_name = self.txt_subject.get(index)
                if subject_name in enrolled_subjects:
                    self.txt_subject.select_set(index)

        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching subjects: {str(ex)}")

        finally:
            con.close()

    #===ALL TEXTS ARE READ ONLY UNTIL UPDATE IS TOGGLED=====
    def toggle_edit_mode(self):
        if not self.edit_mode:
            # Make fields editable
            self.txt_studentID.config(state="normal")
            self.txt_address.config(state="normal", background="lightyellow")
            self.txt_admission.config(state="normal")
            self.txt_name.config(state="normal")
            self.txt_email.config(state="normal")
            self.txt_gender.config(state="normal")
            self.txt_dob.config(state="normal")
            self.txt_contact.config(state="normal")
            self.txt_city.config(state="normal")
            self.txt_province.config(state="normal")
            self.txt_region.config(state="normal")
            self.txt_search_studentID.config(state="normal")
            self.txt_subject.config(state="normal")
        
            self.update_button.config(text="Submit")

            self.edit_mode = True

        else:
           
            self.update()

            self.txt_studentID.config(state="readonly")
            self.txt_address.config(state="disabled", background="#f0f0f0")
            self.txt_admission.config(state="readonly")
            self.txt_name.config(state="readonly")
            self.txt_email.config(state="readonly")
            self.txt_gender.config(state="readonly")
            self.txt_dob.config(state="readonly")
            self.txt_contact.config(state="readonly")
            self.txt_city.config(state="readonly")
            self.txt_province.config(state="readonly")
            self.txt_region.config(state="readonly")
            self.txt_search_studentID.config(state="readonly")
            self.txt_subject.config(state="disabled")
            
           
            self.update_button.config(text="Update")
            self.edit_mode = False

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

                  
                    selected_subjects = self.txt_subject.curselection()
                    
                    cur.execute("DELETE FROM student_subject WHERE studentID = ?", (self.var_studentID.get(),))
    
                    # Insert the new subjects for the student
                    for subject_index in selected_subjects:
                        subject_name = self.txt_subject.get(subject_index)
                        cur.execute("SELECT subjectID FROM subject WHERE name = ?", (subject_name,))
                        subject_id = cur.fetchone()[0]  # Get subjectID
                        cur.execute("INSERT INTO student_subject (studentID, subjectID) VALUES (?, ?)", 
                                    (self.var_studentID.get(), subject_id))

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
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()

           
            self.subjectTable.delete(*self.subjectTable.get_children())

            for row in rows:
                self.subjectTable.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
        finally:
            con.close()

    #===FETCH subject FOR LIST BOX===#
    def fetch_subject(self):
        self.subject_list.clear()
        con = sqlite3.connect('sgs.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM subject")
            rows = cur.fetchall()
            self.txt_subject.delete(0, END)
            for row in rows:
                self.txt_subject.insert(END, row[0])
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

                cur.execute("SELECT c.name FROM student_subject ss JOIN subject c ON ss.subjectID = c.subjectID WHERE ss.studentID = ?", (student[0],))
                subjects = cur.fetchall()
                self.txt_subject.delete(0, END)
                for subject in subjects:
                    self.txt_subject.insert(END, subject[0])
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
