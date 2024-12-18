from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageFont
import sqlite3
import os

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+100+50")

        #===BG IMAGE===#
        self.bg = ImageTk.PhotoImage(file="StudentResultManagementSystem/images/loginbg.jpg")  # Replace with the path to your image
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=500, y=150, width=400, height=400)

        font = ("Poppins") 
        # TITLE
        title = Label(Frame_login, text="Login", font=font, fg="#021e2f", bg="white")
        title.place(x=160, y=30)

        #===ICON IMAGES===#
        self.username_icon = ImageTk.PhotoImage(file="StudentResultManagementSystem/images/username.png")  
        self.password_icon = ImageTk.PhotoImage(file="StudentResultManagementSystem/images/lock.png")  
        
        #===USERNAME ENTRY FIELDS===#
        self.username_icon_label = Label(Frame_login, image=self.username_icon, bg="white")
        self.username_icon_label.place(x=50, y=135, width=30, height=30) 
        self.txt_username = ttk.Entry(Frame_login, font=("Poppins", 12), foreground="gray")
        self.txt_username.place(x=90, y=130, width=260, height=40) 
        self.txt_username.insert(0, "Username")  
        self.txt_username.bind("<FocusIn>", self.on_focus_in_username)
        self.txt_username.bind("<FocusOut>", self.on_focus_out_username)

        #===PASSWORD===#
        self.password_icon_label = Label(Frame_login, image=self.password_icon, bg="white")
        self.password_icon_label.place(x=50, y=215, width=30, height=30)  
        self.txt_password = ttk.Entry(Frame_login, font=("Poppins", 12), foreground="gray", show="*")
        self.txt_password.place(x=90, y=210, width=260, height=40)  
        self.txt_password.insert(0, "Password")
        self.txt_password.bind("<FocusIn>", self.on_focus_in_password)
        self.txt_password.bind("<FocusOut>", self.on_focus_out_password)

        #===ENTRY DESIGN===#
        self.style = ttk.Style()
        self.style.configure("TEntry", 
                             fieldbackground="#f2f2f2",  
                             padding=6,  
                             relief="flat",  
                             borderwidth=0)  
        self.style.map("TEntry", fieldbackground=[('focus', '#d5d5d5')])  

        #===LOGIN BUTTON===#
        btn_login = Button(Frame_login, text="Login", command=self.login_function, font=("Poppins", 15, "bold"), 
                           fg="white", bg="#004aad", cursor="hand2")
        btn_login.place(x=130, y=270, width=120, height=40)

        #===BUTTON EFFECTS===#
        def on_enter(event):
            btn_login.config(bg="#033f56")  

        def on_leave(event):
            btn_login.config(bg="#004aad")  

        # Bind hover events to the login button #
        btn_login.bind("<Enter>", on_enter)
        btn_login.bind("<Leave>", on_leave)\
        
#========================================================
    def on_focus_in_username(self, event):
        if self.txt_username.get() == "Username":
            self.txt_username.delete(0, "end")
            self.txt_username.config(foreground="black") 

    def on_focus_out_username(self, event):
        if self.txt_username.get() == "":
            self.txt_username.insert(0, "Username")
            self.txt_username.config(foreground="gray")  
    def on_focus_in_password(self, event):
        if self.txt_password.get() == "Password":
            self.txt_password.delete(0, "end")
            self.txt_password.config(foreground="black")  

    def on_focus_out_password(self, event):
        if self.txt_password.get() == "":
            self.txt_password.insert(0, "Password")
            self.txt_password.config(foreground="gray")  
    
    #===DATABASE CONNECTION===#
    def login_function(self):
        try:
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()
                
                # Set the journal mode to WAL (Write-Ahead Logging)
                cursor.execute("PRAGMA journal_mode=WAL")
                
        
                cursor.execute("CREATE TABLE IF NOT EXISTS teacher (username TEXT, password TEXT)")

            
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO teacher (username, password) VALUES ('teacher', '12345')")
                    conn.commit()

                username = self.txt_username.get()
                password = self.txt_password.get()
                cursor.execute("SELECT * FROM teacher WHERE username=? AND password=?", (username, password))
                row = cursor.fetchone()

                if row is not None:
                    messagebox.showinfo("Success", "Login Successful!")
                    self.root.destroy()  
                    os.system(r'python "C:\Users\63945\Documents\CompProgProject\StudentResultManagementSystem\dashboard.py"')
                else:
                    messagebox.showerror("Error", "Invalid Username or Password")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred with the database: {e}")



if __name__ == '__main__':
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
