import tkinter as tk
from tkinter import simpledialog, messagebox

def create_password():
    p = simpledialog.askstring("Password","Create your new password", show = "*")
    open("pass.txt", "w").write(p)

def write_password():
    p = simpledialog.askstring("Password", "Enter a new secret code", show="*")

    if p == open("pass.txt").read():
        s = simpledialog.askstring("Secret", "Enter your secret code", show="*")
        open("secret.txt", "w").write(s)
        messagebox.showinfo("Success","Your new password has been created")
    else:
        messagebox.showerror("Error","Incorrect Password")

def read_password():
    p = simpledialog.askstring("Password", "Enter your secret code", show="*")
    if p == open("pass.txt").read():
        secret = open("secret.txt").read()
        messagebox.showinfo("Denied","Wrong Password")

def exit_window():
    root.destroy()

root = tk.Tk()
root.geometry("400x450")
root.title("Secret Code GUI")
root.configure(background="#99a8bd")

label = tk.Label(root, text="Secret Code GUI",bg="white",font=("Times New Roman", 15),padx=10,pady=10)
label.pack(side="top",fill="y", pady=20,ipady=2)

label1 = tk.Label(root, text= """
1. Create new passward
2. Enter new secret code
3. Enter your secret code
4. Go back to main menu
""",
bg="#c8d0dc",
font = ("Arial", 12)
)
label1.pack(side="top",fill="both",pady=3,ipady=3)

b1 = tk.Button(root, text="1",width= 20, height=2, command=create_password)
b1.pack(side="top",fill="y",padx=4, pady=6)
b2 = tk.Button(root, text="2",width= 20, height=2,command=write_password)
b2.pack(side="top",fill="y",padx=4, pady=6)
b3 = tk.Button(root, text="3",width= 20, height=2,command=read_password)
b3.pack(side="top",fill="y",padx=4, pady=6)
b4 = tk.Button(root, text="4",width= 20, height=2,command=exit_window)
b4.pack(side="top",fill="y",padx=4, pady=6)

root.mainloop()
