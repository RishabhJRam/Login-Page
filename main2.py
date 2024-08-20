from tkinter import *
from tkinter import messagebox
import ast
import os

# Construct the path to datasheet.txt within the 'loginpage' folder
file_path = os.path.join('loginpage', 'datasheet.txt')

# Create the main application window
root = Tk()
root.title('Login/Signup App')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Function to handle sign-in
def signin():
    username = user.get()
    password = code.get()
        # Ensure the datasheet file exists
    if not os.path.isfile(file_path):
        messagebox.showerror('Error', 'No user data found.')
        return
        
    try:
        with open(file_path ,'r') as file:
            d = file.read()
            r = ast.literal_eval(d) if d else {}

        if r.get(username) == password:
            messagebox.showinfo('Login', 'Successfully logged in')
            screen = Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg='white')
            Label(screen, text='Welcome Back!!!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
        else:
            messagebox.showerror('Invalid', 'Invalid username or password')
        user.delete(0, 'end')
        user.insert(0,'Username')
        code.delete(0, 'end')
        code.insert(0,'Password')
    except Exception as e:
        messagebox.showerror('Error','Invalid username or password')
        user.delete(0, 'end')
        user.insert(0,'Username')
        code.delete(0, 'end')
        code.insert(0,'Password')

# Function to handle sign-up
def signup():
    username1 = user1.get()
    password1 = code1.get()
    confirm_password1 = confirm_password.get()

    if password1 == confirm_password1:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write('{}')
        try:
            with open(file_path, 'r+') as file:
                d = file.read()
                r=ast.literal_eval(d) if d else {}

                if username1 in r:
                    messagebox.showerror('Invalid', 'Username already exists')
                    user1.delete(0, 'end')
                    user1.insert(0, 'Username')
                    code1.delete(0, 'end')
                    code1.insert(0, 'Password')
                    confirm_password.delete(0, 'end')
                    confirm_password.insert(0, 'Confirm Password')
                    return
            
                r[username1]=password1

                with open(file_path,'w') as file:
                    file.write(str(r))

            messagebox.showinfo('Signup', 'Successfully signed up')
            show_frame(login_frame)

        except Exception as e:
            print(f"An error occured : {e}")
            messagebox.showerror('Error','An error occured during sign-up')
    else:
        messagebox.showerror('Invalid', "Both Passwords don't match")
    user1.delete(0, 'end')
    user1.insert(0, 'Username')
    code1.delete(0, 'end')
    code1.insert(0, 'Password')
    confirm_password.delete(0, 'end')
    confirm_password.insert(0, 'Confirm Password')

# Create a container frame for all pages
container = Frame(root, bg='#fff')
container.place(x=0, y=0, width=925, height=500)

# Create two frames (Login and Signup)
login_frame = Frame(container, bg='white')
signup_frame = Frame(container, bg='white')

for frame in (login_frame, signup_frame):
    frame.place(x=0, y=0, width=925, height=500)

# --- Login Page ---
img = PhotoImage(file='loginpage/login.png')
Label(login_frame, image=img, bg='white').place(x=50, y=50)

frame = Frame(login_frame, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=130, y=0)

subheading = Label(frame, text='Email', fg='#57a1f8', font=('Microsoft YaHei UI Light', 15))
subheading.place(x=80, y=70)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=80, y=120)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=205, height=2, bg='black').place(x=80, y=144)

# Password field
subheading1 = Label(frame, text='Password', fg='#57a1f8', font=('Microsoft YaHei UI Light', 15))
subheading1.place(x=80, y=170)

def on_enter(e):
    if code.get()=='Password':
        code.delete(0, 'end')
        code.config(show='*')

def on_leave(e):
    if code.get() == '':
        code.config(show='')
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=80, y=220)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=205, height=2, bg='black').place(x=80, y=244)

# Sign in button
Button(frame, width=30, text='Sign in', bg='#57a1f8', fg='white', command=signin).place(x=80, y=270)

# Switch to signup page
label = Label(frame, text="Don't have an Account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=95, y=310)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', 
                 command=lambda: show_frame(signup_frame))
sign_up.place(x=231, y=310)

# --- Signup Page ---
img1 = PhotoImage(file='loginpage/login2.png')
Label(signup_frame, image=img1, bg='white').place(x=50, y=90)

frame1 = Frame(signup_frame, width=350, height=390, bg='white')
frame1.place(x=480, y=50)

heading1 = Label(frame1, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23))
heading1.place(x=130, y=0)

subheading2 = Label(frame1, text='Email', fg='#57a1f8', font=('Microsoft YaHei UI Light', 15))
subheading2.place(x=80, y=60)

def on_enter(e):
    user1.delete(0, 'end')

def on_leave(e):
    name = user1.get()
    if name == '':
        user1.insert(0, 'Username')

user1 = Entry(frame1, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user1.place(x=80, y=100)
user1.insert(0, 'Username')
user1.bind('<FocusIn>', on_enter)
user1.bind('<FocusOut>', on_leave)

Frame(frame1, width=205, height=2, bg='black').place(x=80, y=124)

# Password field
subheading2 = Label(frame1, text='Password', fg='#57a1f8', font=('Microsoft YaHei UI Light', 15))
subheading2.place(x=80, y=140)

def on_enter(e):
    if code1.get()=='Password':
        code1.delete(0, 'end')
        code1.config(show='*')

def on_leave(e):
    if code1.get() == '':
        code1.config(show='')
        code1.insert(0, 'Password')

code1 = Entry(frame1, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code1.place(x=80, y=180)
code1.insert(0, 'Password')
code1.bind('<FocusIn>', on_enter)
code1.bind('<FocusOut>', on_leave)

Frame(frame1, width=205, height=2, bg='black').place(x=80, y=204)

# Confirm Password field
subheading3 = Label(frame1, text='Confirm Password', fg='#57a1f8', font=('Microsoft YaHei UI Light', 15))
subheading3.place(x=80, y=220)

def on_enter(e):
    if confirm_password.get()=='Confirm Password':
        confirm_password.delete(0, 'end')
        confirm_password.config(show='*')

def on_leave(e):
    if confirm_password.get() == '':
        confirm_password.config(show='')
        confirm_password.insert(0, 'Confirm Password')

confirm_password = Entry(frame1, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_password.place(x=80, y=260)
confirm_password.insert(0, 'Confirm Password')
confirm_password.bind('<FocusIn>', on_enter)
confirm_password.bind('<FocusOut>', on_leave)

Frame(frame1, width=205, height=2, bg='black').place(x=80, y=284)

# Signup button
Button(frame1, width=30, text='Sign Up', bg='#57a1f8', fg='white', command=signup).place(x=80, y=310)

# Switch back to login page
label1 = Label(frame1, text="Already have an Account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label1.place(x=76, y=350)
back_to_login = Button(frame1, text='Back to Login', fg='#57a1f8', bg='white', border=0, cursor='hand2', 
                        font=('Microsoft YaHei UI Light', 9), command=lambda: show_frame(login_frame))
back_to_login.place(x=224, y=350)

# Show the login frame first
show_frame(login_frame)

root.mainloop()