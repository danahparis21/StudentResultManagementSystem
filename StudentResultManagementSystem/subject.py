from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class subjectClass:
    def __init__(self, root):
        self.root = root
        self.root.title("HS Student Result Management System")
        self.root.geometry("1200x470+170+220")
        self.root.config(bg="white")
        self.root.focus_force()
        self.edit_mode = False
        

        #====TITLE====#
        title = Label(self.root,
                      text="Manage Subject Details",
                      font=("Garamond", 17, "bold"),
                      bg="#191862", fg="white").place(x=8, y=15, width=1181, height=35)

        #===VARIABLES===#
        self.var_subjects = StringVar()
        self.var_duration = StringVar()
        self.var_units = StringVar()

        #==WIDGETS==#
        lbl_subjectName = Label(self.root,
                               text="Subject Name",
                               font=("Helvetica", 13, "bold"),
                               bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root,
                             text="Duration",
                             font=("Helvetica", 13, "bold"),
                             bg="white").place(x=10, y=100)
        lbl_units = Label(self.root,
                            text="Quarters",
                            font=("Helvetica", 13, "bold"),
                            bg="white").place(x=10, y=140)
        lbl_description = Label(self.root,
                                text="Description",
                                font=("Helvetica", 13, "bold"),
                                bg="white").place(x=10, y=180)

        #==ENTRY FIELDS==#
        self.txt_subjectName = Entry(self.root, textvariable=self.var_subjects,
                                    font=("Helvetica", 13),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_subjectName.place(x=150, y=60, width=400)
        self.txt_duration = Entry(self.root, textvariable=self.var_duration,
                             font=("Helvetica", 13),
                             bg="lightyellow", bd=0, relief=SOLID)
        self.txt_duration.place(x=150, y=100, width=400)
        self.txt_units = Entry(self.root, textvariable=self.var_units,
                            font=("Helvetica", 13),
                            bg="lightyellow", bd=0, relief=SOLID)
        self.txt_units.place(x=150, y=140, width=400)
        self.txt_description = Text(self.root,
                                    font=("Helvetica", 13),
                                    bg="lightyellow", bd=0, relief=SOLID)
        self.txt_description.place(x=150, y=180, width=500, height=200)

        #===BUTTONS WITH HOVER EFFECT===#
        self.create_button(self.root, 'Save', "#191862", "#007bff", 150, 400, self.add, relief=SOLID, bd=0) 
        
        self.update_button = self.create_button(
        self.root, 'Update', "#191862", "#28a745", 270, 400, 
        self.toggle_edit_mode, relief=SOLID, bd=0
    )
        self.create_button(self.root, 'Delete', "#191862", "#dc3545", 390, 400, self.delete, relief=SOLID, bd=0)
        self.create_button(self.root, 'Clear', "#191862", "#607d8b", 510, 400, self.clear, relief=SOLID, bd=0)


        #===SEARCH PANEL===#
        self.var_search = StringVar()

        lbl_search_subjectName = Label(self.root,
                                      text="Search Subject",
                                      font=("Helvetica", 13, "bold"),
                                      bg="white").place(x=715, y=65)
        self.txt_search_subjectName = Entry(self.root, textvariable=self.var_search,
                                      font=("Helvetica", 13),
                                      bg="#ecf0f1", bd=0, relief=SOLID)
        self.txt_search_subjectName.place(x=850, y=65, width=240)
        btn_search = Button(self.root, text='⌕',
                            font=("Times New Roman", 17, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1100, y=63, width=70, height=21)

        #==-CONTENT===#
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#ecf0f1")
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.subjectTable = ttk.Treeview(self.C_Frame, columns=("subjectID", "name", "duration", "quarter", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.subjectTable.xview)
        scrolly.config(command=self.subjectTable.yview)

        self.subjectTable.heading("subjectID", text="Subject ID")
        self.subjectTable.heading("name", text="Name")
        self.subjectTable.heading("duration", text="Duration")
        self.subjectTable.heading("quarter", text="Quarter")
        self.subjectTable.heading("description", text="Description")
        self.subjectTable["show"] = 'headings'
        self.subjectTable.column("subjectID", width=60)
        self.subjectTable.column("name", width=100)
        self.subjectTable.column("duration", width=100)
        self.subjectTable.column("quarter", width=100)
        self.subjectTable.column("description", width=150)
        self.subjectTable.pack(fill=BOTH, expand=1)
        self.subjectTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


#===========================================================

    #===BUTTON DESIGNS===#
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

        


    #===CLEAR INPUTS===#
    def clear(self):
        self.show()
        self.var_subjects.set("")
        self.var_duration.set("")
        self.var_units.set("")
        self.var_search.set("")

        self.txt_description.delete('1.0',END)
        self.txt_subjectName.config(state=NORMAL)
        self.txt_duration.config(state=NORMAL)
        self.txt_units.config(state=NORMAL)
        self.txt_search_subjectName.config(state=NORMAL)
        self.txt_description.config(state="normal", background="lightyellow")  
        self.txt_description.delete('1.0', END)
        

    #===DELETE A subject===#
    def delete(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            if self.var_subjects.get()=="":
                messagebox.showerror("Error", "Subject Name is required", parent=self.root)
            else:
                cur.execute("select * from subject where name = ?",(self.var_subjects.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please Select a Subject from the List", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from Subject where name=?",(self.var_subjects.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Subject Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    

    #===ADD A subject===#
    def add(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            if self.var_subjects.get()=="":
                messagebox.showerror("Error", "Subject Name is required", parent=self.root)
            else:
                cur.execute("select * from subject where name = ?",(self.var_subjects.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Subject Name already present", parent=self.root)
                else:
                    cur.execute("insert into subject(name, duration, units, description) values(?,?,?,?)", 
                                (self.var_subjects.get(),
                                 self.var_duration.get(),
                                 self.var_units.get(),
                                 self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Subject Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===AUTOMATICALLY DISPLAY DATA BY CLICKING FROM TABLE===#
    def get_data(self, ev):
        # READ ONLY DATA
        self.txt_subjectName.config(state="readonly")
        self.txt_duration.config(state="readonly")
        self.txt_units.config(state="readonly")

        r = self.subjectTable.focus()  
        content = self.subjectTable.item(r)
        row = content.get("values") 

        if row:
            
            self.subject_id = row[0] 

          
            self.var_subjects.set(row[1]) 
            self.var_duration.set(row[2]) 
            self.var_units.set(row[3])   

            self.txt_description.config(state="normal", background="#f0f0f0")  
            self.txt_description.delete('1.0', END) 
            self.txt_description.insert(END, row[4])  
            self.txt_description.config(state="disabled", background="#f0f0f0")  
        else:
            # where no row is selected
            print("No row selected.")
            self.txt_subjectName.config(state="normal")
            self.txt_duration.config(state="normal")
            self.txt_units.config(state="normal")
            self.txt_description.config(state="normal", background="lightyellow")  
            self.txt_description.delete('1.0', END)





    #===ALL TEXTS ARE READ ONLY UNTIL UPDATE IS TOGGLED=====
    def toggle_edit_mode(self):
        if not self.edit_mode:
            self.txt_subjectName.config(state="normal")
            self.txt_duration.config(state="normal")
            self.txt_units.config(state="normal")
            self.txt_description.config(state="normal", background="lightyellow")  
            self.edit_mode = True
            self.update_button.config(text="Submit")  
        else:
           
            self.update()
            self.txt_subjectName.config(state="readonly")
            self.txt_duration.config(state="readonly")
            self.txt_units.config(state="readonly")
            self.txt_description.config(state="disabled", background="#f0f0f0")
            self.edit_mode = False
            self.update_button.config(text="Update")  # Reset button text


    #====UPDATING THE NEW DATA INTO DATABASE====
    def update(self):
        con = sqlite3.connect(database="sgs.db")
        cur = con.cursor()
        
        try:
            
            if self.var_subjects.get() == "":
                messagebox.showerror("Error", "Subject Name is required", parent=self.root)
            else:
                if not hasattr(self, 'subject_id'):
                    messagebox.showerror("Error", "No Subject selected", parent=self.root)
                    return

                # Perform the update based on subject_id
                cur.execute(
                    "update subject set name=?, duration=?, units=?, description=? where subjectID=?",  
                    (
                        self.var_subjects.get(), 
                        self.var_duration.get(),
                        self.var_units.get(),
                        self.txt_description.get("1.0", END).strip(),
                        self.subject_id 
                    )
                )
                con.commit()
                messagebox.showinfo("Success", "Subject Updated Successfully", parent=self.root)
                self.show()  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()


    #===SHOW DETAILS IN TABLE===#
    def show(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            cur.execute("select * from subject ")
            rows = cur.fetchall()
            self.subjectTable.delete(*self.subjectTable.get_children())
            for row in rows:
                self.subjectTable.insert('', END, values = row)
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #===SEARCH subject===#
    def search(self):
        con=sqlite3.connect(database="sgs.db")
        cur=con.cursor()

        try:
            cur.execute(f"select * from subject where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.subjectTable.delete(*self.subjectTable.get_children())
            for row in rows:
                self.subjectTable.insert('', END, values = row)
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        
        
#===RUN FILE===#
if __name__ == '__main__':
    root=Tk()
    obj=subjectClass(root)
    root.mainloop()
