from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql #pip install pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #===BG IMAGE====#
        self.bg = ImageTk.PhotoImage(file="StudentResultManagementSystem/images/side.png")
        left=Label(self,root,image=self.left).place(x=80, y=100, width=400, height=500)
        