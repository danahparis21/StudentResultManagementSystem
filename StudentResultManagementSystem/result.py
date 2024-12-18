from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


# RMS = SGS
class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x500+170+220")
        self.root.config(bg="white")
        self.root.focus_force()

        # ====TITLE====#
        title = Label(self.root,
                      text="Add Student Results",
                      font=("Garamond", 17, "bold"),
                      bg="#fff2bd", fg="#262626").place(x=10, y=15, width=1181, height=50)

        # =====WIDGETS====#

        # =============Variables==========#
        self.var_studentID = StringVar()
        self.var_name = StringVar()
        self.var_subject = StringVar()
        self.var_marks = StringVar()
        self.var_full_grades = StringVar()
        self.var_status = StringVar()
        self.studentID_list = []
        self.fetch_studentID()

        lbl_select = Label(self.root,
                           text="Select Student",
                           font=("Helvetica", 15, "bold"),
                           bg="white").place(x=50, y=100)
        lbl_name = Label(self.root,
                         text="Name",
                         font=("Helvetica", 15, "bold"),
                         bg="white").place(x=50, y=145)
        lbl_subject = Label(self.root,
                           text="Subject",
                           font=("Helvetica", 15, "bold"),
                           bg="white").place(x=50, y=190)
        lbl_marks_ob = Label(self.root,
                             text="Score",
                             font=("Helvetica", 15, "bold"),
                             bg="white").place(x=50, y=290)
        lbl_full_grades = Label(self.root,
                                text="Total Items",
                                font=("Helvetica", 15, "bold"),
                                bg="white").place(x=50, y=340)
        lbl_status = Label(self.root,
                           text="Status",
                           font=("Helvetica", 15, "bold"),
                           bg="white").place(x=50, y=390)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_studentID, values=self.studentID_list,
                                         font=("Helvetica", 15),
                                         state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        btn_search = Button(self.root, text='⌕',
                            font=("Times New Roman", 20, "bold"),
                            bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=500, y=100,
                                                                                                   width=70, height=28)

        # ======ENTRY FIELDS======#
        txt_name = Entry(self.root, textvariable=self.var_name,
                         font=("Helvetica", 18),
                         bg="lightyellow", state='readonly', bd=0, relief=SOLID).place(x=280, y=140, width=320)
        self.txt_subject = ttk.Combobox(self.root, textvariable=self.var_subject,
                                   font=("Helvetica", 15),
                                   values=[], state='normal', justify=CENTER)
        self.txt_subject.place(x=280, y=190, width=320)
        txt_marks = Entry(self.root, textvariable=self.var_marks,
                          font=("Helvetica", 18),
                          bg="lightyellow", bd=0, relief=SOLID).place(x=280, y=290, width=320)
        txt_full_grades = Entry(self.root, textvariable=self.var_full_grades,
                                font=("Helvetica", 18),
                                bg="lightyellow", bd=0, relief=SOLID).place(x=280, y=340, width=320)
        txt_status = Entry(self.root, textvariable=self.var_status,
                           font=("Helvetica", 18),
                           bg="lightyellow", state='readonly', bd=0, relief=SOLID).place(x=280, y=390, width=320)


    #====QUARTER
        # Variable for Quarter selection
        self.var_quarter = StringVar()

        # Quarter ComboBox
        lbl_quarter = Label(self.root, text="Quarter", font=("Helvetica", 15, "bold"), bg="white").place(x=50, y=240)
        self.txt_quarter = ttk.Combobox(self.root, textvariable=self.var_quarter,
                                        font=("Helvetica", 15), values=["1", "2", "3", "4"], state='normal', justify=CENTER)
        self.txt_quarter.place(x=280, y=240, width=320)

        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Submit', "#191862", "#007bff", 150, 440, self.add, relief=SOLID, bd=0) 
        self.create_button(self.root, 'Clear', "#191862", "#28a745", 270, 440, self.clear, relief=SOLID, bd=0)
        self.create_button(self.root, 'Update', "#191862", "#dc3545", 390, 440, self.update, relief=SOLID, bd=0)
        self.create_button(self.root, 'Calculate', "#191862", "#607d8b", 510, 440, self.calculate, relief=SOLID, bd=0)

        # ===IMAGE===#
        self.bg_img = Image.open("StudentResultManagementSystem/images/resultbg.png")
        self.bg_img = self.bg_img.resize((400, 400), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img, bg="white").place(x=650, y=80, width=400, height=400)
        

#================================================================

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

    #===UPDATE STUDENT RESULTS ===#
    def update(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            if self.var_studentID.get() == "":
                messagebox.showerror("Error", "Student Number is required", parent=self.root)
                return
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Student Name is required", parent=self.root)
                return
            if not self.txt_subject.get():
                messagebox.showerror("Error", "Please select a subject", parent=self.root)
                return
            if self.var_quarter.get() == "":
                messagebox.showerror("Error", "Quarter is required", parent=self.root)
                return
            if self.var_marks.get() == "" or self.var_full_grades.get() == "" or self.var_status.get() == "":
                messagebox.showerror("Error", "Marks, Full Grades, and Status are required", parent=self.root)
                return

            selected_subject = self.txt_subject.get()
            selected_quarter = self.var_quarter.get()

          
            cur.execute("""
                SELECT * FROM result WHERE studentID = ? AND subject = ? AND quarter = ?
            """, (self.var_studentID.get(), selected_subject, selected_quarter))
            existing_result = cur.fetchone()

            if existing_result:
                per = (int(self.var_marks.get()) * 100) / int(self.var_full_grades.get())
                cur.execute("""
                    UPDATE result SET 
                        marks_ob = ?, 
                        full_grades = ?, 
                        per = ?, 
                        status = ? 
                    WHERE studentID = ? AND subject = ? AND quarter = ?
                """, (
                    self.var_marks.get(),
                    self.var_full_grades.get(),
                    per,
                    self.var_status.get(),
                    self.var_studentID.get(),
                    selected_subject,
                    selected_quarter
                ))
                messagebox.showinfo("Success", "Student result updated successfully", parent=self.root)
            else:
                self.add()
            con.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
        finally:
            con.close()

    #===FETCH STUDENT DETAILS FROM SEARCHING===#
    def fetch_studentID(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            cur.execute("select studentID from student ")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.studentID_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===SEARCH BY NAME COMBO BOX===#
    def search(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            # Fetch student name by studentID
            cur.execute("SELECT name FROM student WHERE studentID=?", (self.var_studentID.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])

                
                cur.execute(""" 
                    SELECT c.name 
                    FROM student_subject ss
                    JOIN subject c ON ss.subjectID = c.subjectID
                    WHERE ss.studentID = ? 
                """, (self.var_studentID.get(),))
                subjects = cur.fetchall()
                subject_list = [subject[0] for subject in subjects]  
                self.var_subject.set("Select")
                self.txt_subject['values'] = subject_list  
            else:
                messagebox.showerror("Error", "No Student Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===CALCULATE THE PERCENTAGE AND RETURNS THE STATUS===#
    def calculate(self):
        try:
            marks = int(self.var_marks.get())
            full_grades = int(self.var_full_grades.get())
            percentage = (marks * 100) / full_grades

            # Round the percentage to 2 decimal places
            percentage = round(percentage, 2)

            status = "Passed" if percentage >= 75 else "Failed"
            self.var_status.set(status)

            print(f"Percentage: {percentage:.2f}% Status: {status}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid marks and full grades.", parent=self.root)


     #===ADDING DETAILS TO RESULT TABLE===#
    def add(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            if self.var_studentID.get() == "Select" or self.var_subject.get() == "Select":
                messagebox.showerror("Error", "StudentID and subject are required", parent=self.root)
                return
            if self.var_quarter.get() == "":
                messagebox.showerror("Error", "Quarter is required", parent=self.root)
                return

            # Calculate the percentage
            per = (int(self.var_marks.get()) * 100) / int(self.var_full_grades.get())
            per = round(per, 2)  # Round to 2 decimal places

            # Insert data into the database
            cur.execute("""
                INSERT INTO result (studentID, subject, marks_ob, full_grades, per, status, quarter) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                self.var_studentID.get(),
                self.var_subject.get(),
                self.var_marks.get(),
                self.var_full_grades.get(),
                per,
                self.var_status.get(),
                self.var_quarter.get()
            ))

            con.commit()
            messagebox.showinfo("Success", "Student result added successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_studentID.set("Select")
        self.var_name.set("")
        self.var_subject.set("Select")
        self.var_marks.set("")
        self.var_full_grades.set("")
        self.var_status.set("")
        self.var_quarter.set("Select")


if __name__ == '__main__':
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
