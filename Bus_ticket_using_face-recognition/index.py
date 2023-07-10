from tkinter import *
import main
import verfiy

window = Tk()

window.title("Welcome to Bus Service")

window.geometry('1000x750')

hello_lab = Label(window, text="Hello",font=("Arial Bold", 50))
photo= Label(window, text="Use S to click the photo",font=("Arial Bold", 25))
hello_lab.place(relx=0.5,rely=0.05,anchor=CENTER)
photo.place(relx=0.5,rely=0.2,anchor=CENTER)


name_var=StringVar()

name_glob=""
def submit_reg():
    name=name_var.get()
    # name_glob=name
    print(name)
    main.reg_subp(name)
    print("The name is : " + name)
    
     
    name_var.set("")
   

def submit_ver():
    verfiy.verify()

name_label = Label(window, text = 'Enter Your Name', font=('calibre',20, 'bold'))
name_entry = Entry(window,textvariable = name_var, font=('calibre',20,'normal'))
reg_button=Button(window,text="Register",height=2,width=15,command=submit_reg)
verify_button=Button(window,text="Verify",height=2,width=15,command=submit_ver)


name_label.place(relx=0.5,rely=0.3,anchor=CENTER)
name_entry.place(relx=0.5,rely=0.4,anchor=CENTER)
reg_button.place(relx=0.5,rely=0.5,anchor=CENTER,)
verify_button.place(relx=0.5,rely=0.6,anchor=CENTER)

window.mainloop()

