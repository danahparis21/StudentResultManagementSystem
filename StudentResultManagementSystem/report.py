from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import tkinter as tk
import sqlite3

# RMS = SGS
class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+170+220")
        self.root.config(bg="white")
        self.root.focus_force()

        #====TITLE====#
        title = Label(self.root, 
                      text="View Student Results" ,
                      font=("Helvetica",20,"bold"),
                      bg="#fff2bd", fg="#262626").place(x=10, y=15, width=1181, height=50)

        # ======SEARCH COMBOBOX=======#
        self.var_search = StringVar()
        lbl_search = Label(self.root,
                           text="Search By Student Name",
                           font=("Helvetica", 15, "bold"),
                           bg="white").place(x=260, y=100)
        
        # Fetch students from database 
        self.student_list = self.get_students()
        self.student_combo = ttk.Combobox(self.root, textvariable=self.var_search, 
                                           values=self.student_list, font=("Helvetica", 15),
                                           state="readonly", width=20)
        self.student_combo.place(x=520, y=100, width=150)
        
        
        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Search', "#03a9f4", "#007bff", 680, 100, self.search, relief=SOLID, bd=0) 
        self.create_button(self.root, 'Clear', "#191862", "#607d8b", 800, 100, self.clear, relief=SOLID, bd=0)


        # ====RESULT LABELS=====#
        lbl_studentID = Label(self.root,
                              text="Student ID", 
                              font=("goudy old style", 15, "bold"),
                              bg="white", bd=2, relief=GROOVE).place(x=80, y=150, width=150, height=50)
        lbl_name = Label(self.root,
                         text="Name", 
                         font=("goudy old style", 15, "bold"),
                         bg="white", bd=2, relief=GROOVE).place(x=230, y=150, width=150, height=50)
        lbl_course = Label(self.root,
                           text="Course", 
                           font=("goudy old style", 15, "bold"),
                           bg="white", bd=2, relief=GROOVE).place(x=380, y=150, width=150, height=50)
        lbl_marks_obj = Label(self.root,
                              text="Marks Obtained", 
                              font=("goudy old style", 15, "bold"),
                              bg="white", bd=2, relief=GROOVE).place(x=530, y=150, width=150, height=50)
        lbl_full_grades = Label(self.root,
                                text="Full Marks", 
                                font=("goudy old style", 15, "bold"),
                                bg="white", bd=2, relief=GROOVE).place(x=680, y=150, width=150, height=50)
        lbl_per = Label(self.root,
                        text="Percent", 
                        font=("goudy old style", 15, "bold"),
                        bg="white", bd=2, relief=GROOVE).place(x=830, y=150, width=150, height=50)
        
        lbl_per = Label(self.root,
                        text="Status", 
                        font=("goudy old style", 15, "bold"),
                        bg="white", bd=2, relief=GROOVE).place(x=980, y=150, width=150, height=50)

        #========TABLE DISPLAY===========
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.place(x=80, y=210, width=1050, height=200)  

        #===CANVAS WITH SCROLLBAR FOR TABLE===#
        self.canvas = tk.Canvas(self.results_frame)
        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        #===TREEVIEW TO HOLD THE TABLE===#
        self.table_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        #===BIND CANVAS TO ADJUST SCROLL REGION TO TABLE SIZE===#
        self.table_frame.bind(
            "<Configure>", 
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create the Treeview (table) widget
        self.tree = ttk.Treeview(self.table_frame, columns=("studentID", "name", "course", "marks_ob", "full_marks", "percent", "status"), show="headings")

        #===COLUMNS===#
        self.tree.column("studentID", width=150, anchor="center")
        self.tree.column("name", width=150, anchor="center")
        self.tree.column("course", width=150, anchor="center")
        self.tree.column("marks_ob", width=150, anchor="center")
        self.tree.column("full_marks", width=150, anchor="center")
        self.tree.column("percent", width=150, anchor="center")
        self.tree.column("status", width=150, anchor="center")

        #===TREEVIEW TABLE DESIGN===#
        style = ttk.Style()
        style.configure("Treeview", font=("Times New Roman", 14))  # Adjust font size here
        style.configure("Treeview.Heading", font=("Times New Roman", 14, "bold"))  # Adjust heading font size here

        self.tree.pack(fill="both", expand=True)

        # ======== AVERAGE AND OVERALL STATUS LABELS ========
        self.lbl_avg = Label(self.root, text="Average: ", font=("Helvetica", 15, "bold"), fg="red", bg="white")
        self.lbl_avg.place(x=80, y=420)
        self.lbl_status = Label(self.root, text="Overall Status: ", font=("Helvetica", 15, "bold"), fg="red", bg="white")
        self.lbl_status.place(x=500, y=420)

#============================================================

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


    #===FETCH STUDENTS DATA FROM COMBOBOX===#
    def get_students(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()
        cur.execute("SELECT DISTINCT name FROM student") 
        students = [row[0] for row in cur.fetchall()]
        return students

    #===SEARCH STUDENT BY NAME===#
    def search(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()

        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Student Name is required", parent=self.root)
            else:
                name = self.var_search.get()

                
                cur.execute("SELECT * FROM student WHERE name=?", (name,))
                student_row = cur.fetchone()

                if student_row:
                    # Get the student ID from the student table
                    studentID = student_row[0]
                    # Fetch results from the 'result' table based on the student ID
                    cur.execute("SELECT * FROM result WHERE studentID=?", (studentID,))
                    result_rows = cur.fetchall()
                    # If results are found
                    if result_rows:
                        self.display_results(result_rows)  # Pass all result rows to the display_results
                    else:
                        messagebox.showerror("Error", "No results found for this student.", parent=self.root)
                else:
                    messagebox.showerror("Error", "No student found with that name.", parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===CONVERT STRING VALUES TO FLOAT===#
    def to_float(self, value):
        print(f"Converting value: {value}")  # Debug print
        try:
            return float(value)
        except ValueError:
            return 0  


    #===DISPLAY RESULTS TO TABLE===#
    def display_results(self, results):
        con = sqlite3.connect("sgs.db")
        cur = con.cursor()

        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert into the treeview (table)
        for row in results:
            studentID = row[1]  # Student ID 
            name = row[2]        # Student name 
            course = row[3]      # Course name 
            marks_ob = float(row[4])  # Marks obtained
            full_marks = float(row[5])  # Full marks 
            percent = float(row[6])  # Percentage 
            status = row[7]  # Status 

            # Insert each result 
            self.tree.insert("", "end", values=(studentID, name, course, marks_ob, full_marks, percent, status))
             # Calculate the average percentage and overall status
            average, overall_status = self.calculate_average_and_status(results)
            self.lbl_avg.config(text=f"Average: {average:.2f}%")
            self.lbl_status.config(text=f"Overall Status: {overall_status}")

    #===CLEAR TREEVIEW TABLE===#        
    def clear(self):
        self.var_search.set("")
        for item in self.tree.get_children():
            self.tree.delete(item)

    #===CALCULATE AVERAGE AND RETURN STATUS PASSED OR FAILES===#      
    def calculate_average_and_status(self, results):
        total_percent = 0
        count = len(results)
        overall_status = "Passed"  

        for row in results:
            percent = float(row[6])  # Percentage = 7th column
            status = row[7]  # Status = 8th column 

            total_percent += percent
            if status.lower() == "failed":
                overall_status = "Failed"  # set to failed if a row has 'failed'

        average = total_percent / count if count > 0 else 0 
        return average, overall_status


#===============RUN SYSTEM=============

if __name__ == '__main__':
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()
