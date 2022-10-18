from tkinter import *
from tkinter import messagebox
import ast
import os

window = Tk()
window.title("Register")
window.geometry('300x400+850+200')
window.configure(bg='#fff')
window.resizable(False, False)

Label(window, text='Register', fg='#737CA1', bg='white', font=('Microsoft YaHei UI', 24)).place(x=75, y=20)
## REGISTER
def register():
    username=user.get()
    password=pw.get()
    passwordConfirm=pwConfirm.get()

    if password==passwordConfirm:
        if username!='' and username!='Username':
            try:
                file=open('database.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                dict1={username:password}
                if len(r)<=10:
                    r.update(dict1)
                    file.truncate(0)
                    file.close()
                    file=open('database.txt','w')
                    w=file.write(str(r))
                    messagebox.showinfo('Success', 'Registered Successfully!')
                else:
                    messagebox.showerror('Error','User Capacity Reached!')
            except:
                file=open('database.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
                messagebox.showwarning('Error','Please try again!')
        else:
            messagebox.showerror('Error', 'Username cannot be blank!')
    else:
        messagebox.showerror('Error', 'Passwords do not match!')
## CLEAR DATABASE
def deleteDatabase():
    try:
        os.remove('database.txt')
        file = open('database.txt', 'w')
        pp = str({'Username': 'password'})
        file.write(pp)
        file.close()
    except:
        messagebox.showinfo('Info', 'Database has been removed.')

Button(window, text="X",bg='white',fg='#E5E4E2',border=0,command=deleteDatabase).place(x=0,y=380)

## USERNAME FIELD
def onEnter(e):
    user.delete(0,'end')
def onExit(e):
    if user.get() == '':
        user.insert(0,'Username')

user=Entry(window,width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=110)
user.insert(0,'Username')
user.bind("<FocusIn>", onEnter)
user.bind("<FocusOut>", onExit)
Frame(window,width=250, height=2, bg='#737CA1').place(x=25, y=137)

## PASSWORD FIELD
def onEnter(e):
    pw.delete(0,'end')
def onExit(e):
    if pw.get() == '':
        pw.insert(0,'Password')

pw=Entry(window,width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
pw.place(x=30, y=170)
pw.insert(0,'Password')
pw.bind("<FocusIn>", onEnter)
pw.bind("<FocusOut>", onExit)
Frame(window,width=250, height=2, bg='#737CA1').place(x=25, y=197)

## CONFIRM PASSWORD FIELD
def onEnter(e):
    pwConfirm.delete(0,'end')
def onExit(e):
    if pwConfirm.get() == '':
        pwConfirm.insert(0,'Confirm Password')

pwConfirm=Entry(window,width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
pwConfirm.place(x=30, y=230)
pwConfirm.insert(0,'Confirm Password')
pwConfirm.bind("<FocusIn>", onEnter)
pwConfirm.bind("<FocusOut>", onExit)
Frame(window,width=250, height=2, bg='#737CA1').place(x=25, y=257)

## SIGN UP BUTTON
Button(window,width=30,pady=8,text="Sign Up",bg='#737CA1',fg='white',border=0,command=register).place(x=45,y=310)

window.mainloop()
