from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from subject import subjectClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import os
import sqlite3


# RMS = SRMS
class SRMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1360
        window_height = 700
        position_top = (screen_height - window_height) // 2 - 30  
        position_right = (screen_width - window_width) // 2
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
       
        self.root.config(bg="white")
        
        #==ICONS==#
        self.logo_dash = ImageTk.PhotoImage(file="StudentResultManagementSystem/images/logo.png")
        #====TITLE====#
        font = ("Poppins")
        title = Label(self.root, 
                      text="Student Result Management System",
                      padx=10,
                      compound=LEFT,
                      image=self.logo_dash, 
                      font=(font, 20, "bold"),
                      bg="#191862", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #====BUTTON EFFECTS====#
        def on_enter(e):
            e.widget['background'] = '#4a90e2'  # Change to light yellow on hover

        def on_leave(e):
            e.widget['background'] = '#191862'  # Revert back to original color

        def create_button(text, command, x_position):
            button = Button(text=text, font=("Helvetica", 15, "bold"), bg="#191862", fg="white", cursor="hand2", command=command,
                            relief=FLAT, bd=0, padx=10, pady=10)
            button.place(x=x_position, y=50, width=240, height=60)
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            return button

        btn_subject = create_button("Subject", self.add_subject, 0)
        btn_student = create_button("Student", self.add_student, 240)
        btn_result = create_button("Result", self.add_result, 450)
        btn_view = create_button("View Students Results", self.add_report, 680)
        btn_logout = create_button("Log Out", self.logout, 920)
        btn_exit = create_button("Exit", self.exit, 1140)

        #===CONTENT WINDOW===#
        self.bg_img = Image.open("StudentResultManagementSystem/images/dashboard.png")
        self.bg_img = self.bg_img.resize((1360, 450), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img, bg="white").place(x=0, y=150, width=1360, height=450)
        
        #===LABELS===#
        self.lbl_subject = Label(self.root, text="Total Subject\n[0]", 
                                font=("Poppins", 20, "bold"), bd=5, bg="#4a90e2", fg="white", 
                                padx=10, pady=10, anchor="center")
        self.lbl_subject.place(x=10, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[0]", 
                                 font=("Poppins", 20, "bold"), bd=5, bg="#3b8cdb", fg="white", 
                                 padx=10, pady=10, anchor="center")
        self.lbl_student.place(x=320, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[0]", 
                                font=("Poppins", 20, "bold"), bd=5, bg="#47b0b6", fg="white", 
                                padx=10, pady=10, anchor="center")
        self.lbl_result.place(x=630, y=530, width=300, height=100)

        #====FOOTER====#
        title = Label(self.root, 
                      text="SRMS-Student Result Management System\n Contact Email: university@uni.com",
                      font=("goudy old style", 12),
                      bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

        self.update_details()

#================================================================
    def update_details(self):
        try:
            with sqlite3.connect(database="sgs.db") as con:
                cur = con.cursor()

                # Get the total counts
                cur.execute("SELECT COUNT(*) FROM subject")
                subject_count = cur.fetchone()[0]
                self.lbl_subject.config(text=f"Total Subject\n[{str(subject_count)}]")

                cur.execute("SELECT COUNT(*) FROM student")
                student_count = cur.fetchone()[0]
                self.lbl_student.config(text=f"Total Students\n[{str(student_count)}]")

                cur.execute("SELECT COUNT(*) FROM result")
                result_count = cur.fetchone()[0]
                self.lbl_result.config(text=f"Total Result\n[{str(result_count)}]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    #===BUTTON ACTIONEVENTS===#
    def add_subject(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = subjectClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)
    
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to log out?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system(r'python "C:\Users\63945\Documents\CompProgProject\StudentResultManagementSystem\login.py"')

    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to EXIT?", parent=self.root)
        if op == True:
            self.root.destroy()

#course
if __name__ == '__main__':
    root = Tk()
    obj = SRMS(root)
    root.mainloop()
