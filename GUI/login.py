from tkinter import *
from tkinter import messagebox
import ast
import os
import pacemaker

main = Tk()
main.title("Login")
main.geometry('950x500+300+150')
main.configure(bg='#737CA1')
main.resizable(False, False)

img = PhotoImage(file='health.png')
Label(main, image=img, bg='#737CA1').place(x=50, y=50)

frame1 = Frame(main, width=500, height=950, bg='white')
frame1.place(x=480, y=0)
frame = Frame(main, width=500, height=950, bg='white')
frame.place(x=480, y=70)

heading1 = Label(text='Welcome to the Pacemaker Controller', fg='white', bg='#737CA1',
                 font=('Microsoft YaHei UI Light', 16, 'bold'))
heading1.place(x=35, y=10)

heading = Label(frame, text='Login', fg='#737CA1', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=175, y=5)

## LOGIN INFORMATION
def signin():
    username=user.get()
    password=pw.get()
    try:
        file = open('database.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        # print(r.keys())
        # print(r.values())
        if username in r.keys() and password==r[username]:
            main.destroy()
            pacemaker.launchApp()
        else:
            messagebox.showerror("Invalid Entry","Invalid username or password!")
    except:
        messagebox.showerror("Error", "No users found, please register first!")


## SIGN UP POP-UP
def registerPopup():
    window=Toplevel(main)
##00000000000000000000000000000000000000000000
    window.title("Register")
    window.geometry('300x400+850+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    Label(window, text='Register', fg='#737CA1', bg='white', font=('Microsoft YaHei UI', 24)).place(x=75, y=20)

    ## REGISTER
    def register():
        username = user.get()
        password = pw.get()
        passwordConfirm = pwConfirm.get()

        if password == passwordConfirm:
            if username != '' and username != 'Username':
                try:
                    file = open('database.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)
                    dict1 = {username: password}
                    if username in r.keys():
                        messagebox.showerror('Error','User Already Exists!')
                        window.destroy()
                    else:
                        if len(r) <= 10:
                            r.update(dict1)
                            file.truncate(0)
                            file.close()
                            file = open('database.txt', 'w')
                            w = file.write(str(r))
                            messagebox.showinfo('Success', 'Registered Successfully!')
                            window.destroy()
                        else:
                            messagebox.showerror('Error', 'User Capacity Reached!')
                except:
                    file = open('database.txt', 'w')
                    pp = str({'Username': 'password'})
                    file.write(pp)
                    file.close()
                    #created file^ now add user:
                    file = open('database.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)
                    dict1 = {username: password}
                    if len(r) <= 10:
                        r.update(dict1)
                        file.truncate(0)
                        file.close()
                        file = open('database.txt', 'w')
                        w = file.write(str(r))
                        messagebox.showinfo('Success', 'Registered Successfully!')
                        window.destroy()
                    else:
                        messagebox.showerror('Error', 'User Capacity Reached!')
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

    Button(window, text="X", bg='white', fg='#E5E4E2', border=0, command=deleteDatabase).place(x=0, y=380)

    ## USERNAME FIELD
    def onEnter(e):
        user.delete(0, 'end')

    def onExit(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=110)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", onEnter)
    user.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=137)

    ## PASSWORD FIELD
    def onEnter(e):
        pw.delete(0, 'end')

    def onExit(e):
        if pw.get() == '':
            pw.insert(0, 'Password')

    pw = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    pw.place(x=30, y=170)
    pw.insert(0, 'Password')
    pw.bind("<FocusIn>", onEnter)
    pw.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=197)

    ## CONFIRM PASSWORD FIELD
    def onEnter(e):
        pwConfirm.delete(0, 'end')

    def onExit(e):
        if pwConfirm.get() == '':
            pwConfirm.insert(0, 'Confirm Password')

    pwConfirm = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    pwConfirm.place(x=30, y=230)
    pwConfirm.insert(0, 'Confirm Password')
    pwConfirm.bind("<FocusIn>", onEnter)
    pwConfirm.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=257)

    ## SIGN UP BUTTON
    Button(window, width=30, pady=8, text="Sign Up", bg='#737CA1', fg='white', border=0, command=register).place(x=45,
                                                                                                                 y=310)

    window.mainloop()

##OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

## USERNAME BOX
def onEnter(e):
    user.delete(0, 'end')

def onExit(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=36, fg='#737CA1', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=75, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', onEnter)
user.bind('<FocusOut>', onExit)
Frame(frame, width=295, height=2, bg='#737CA1').place(x=70, y=110)


## PASSWORD BOX
def onEnter1(e):
    pw.delete(0, 'end')

def onExit1(e):
    if pw.get() == '':
        pw.insert(0, 'Password')

pw = Entry(frame, width=36, fg='#737CA1', border=0, bg='white', font=('Microsoft YaHei UI Light', 11),show='')
pw.place(x=75, y=150)
pw.insert(0, 'Password')
pw.bind('<FocusIn>', onEnter1)
pw.bind('<FocusOut>', onExit1)
Frame(frame, width=295, height=2, bg='#737CA1').place(x=70, y=180)
## PASSWORD HIDER
def hidePass():
    if pw.cget('show')=='*':
        pw.config(show='')
    else:
        pw.config(show='*')

checkButton = Checkbutton(main, text="Hide Password",bg='white',command=hidePass)
checkButton.place(x=550,y=260)
## SIGN IN BUTTON
Button(frame, width=30, pady=8, text='Sign in', bg='#737CA1', fg='white', border=0,command=signin).place(x=110, y=225)
# SIGN UP
Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 10)).place(x=120, y=265)
Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=registerPopup).place(x=270,y=267)

main.mainloop()
