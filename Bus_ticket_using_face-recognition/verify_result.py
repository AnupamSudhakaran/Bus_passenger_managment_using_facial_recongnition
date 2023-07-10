from tkinter import *


def verify_res(name):
    if name=="False":
        window=Tk()
        window.title("Bus_service")
        window.geometry("500x500")
        lab=Label(window, text="Sorry you are not part of the System",font=("Arial Bold", 15))
        lab.place(relx=0.5,rely=0.2,anchor=CENTER)
        window.mainloop()
        return

        
    window = Tk()

    window.title("Bus Service")

    window.geometry('500x500')

    hello_lab = Label(window, text=f"Hi {name}",font=("Arial Bold", 50))
    photo= Label(window, text="Welcome to the Bus,",font=("Arial Bold", 25))
    ticket= Label(window, text="Ticket Expiry-month_end ",font=("Arial Bold", 25))

    hello_lab.place(relx=0.5,rely=0.1,anchor=CENTER)
    photo.place(relx=0.5,rely=0.25,anchor=CENTER)
    ticket.place(relx=0.5,rely=0.35,anchor=CENTER)
   

    window.mainloop()


# verify_res("False")
verify_res("Anupam")