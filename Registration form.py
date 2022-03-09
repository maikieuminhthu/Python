from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Creating Registration Form")
window.geometry("500x500")
window.config(bg="#e8c364")
#----------------------------------
variable = StringVar()
variable.set("Country")
countries = open("selectcountries.txt")

#------------------------------------
f=("Time",14)
def Submit():
    answer=messagebox.showinfo(title="Registration", message="Congratulation, you completed successfully")
    print(answer)
#------------------------------------

frame_form= Frame(window,bg="#CCCCCC", relief=SOLID,bd=2,padx=50,pady=5)
frame_form.pack()

label=Label(frame_form, text=" Registration Form", font=("Time", 14, "bold"), bg="#CCCCCC")

fullname=Label(frame_form,text="Full name", font=f,bg="#CCCCCC",pady=5,)
email=Label(frame_form,text="Email", font=f,bg="#CCCCCC",pady=5)
password=Label(frame_form,text="Password", font=f,bg="#CCCCCC",pady=5)
gender=Label(frame_form,text="Gender", font=f,bg="#CCCCCC",pady=5)
country=Label(frame_form,text="Select Country", font=f,bg="#CCCCCC",pady=5)

label.grid(row =0, columnspan= 2)
fullname.grid(row =1, column=0,sticky=W)
email.grid(row =2, column=0,sticky=W)
password.grid(row =3, column=0,sticky=W)
gender.grid(row =4, column=0,sticky=W)
country.grid(row =5, column=0,sticky=W)

fullname_entry= Entry(frame_form,width=25,font=("Time",13))
email_entry=Entry(frame_form,width=25,font=("Time",13))
password_entry=Entry(frame_form,show="*",width=25,font=("Time",13))

fullname_entry.grid(row =1, column=1,ipady=3)
email_entry.grid(row =2, column=1,ipady=3)
password_entry.grid(row =3, column=1,ipady=3)

nut= Button(frame_form,text="Submit", font=("Time", 11, "bold"),cursor="hand2", command= Submit)
nut.grid(row =6, columnspan=2,pady=5)

x= StringVar()
x.set(" ")
gender_frame= Label(frame_form, bg="#CCCCCC",relief=GROOVE,pady=5)

male_btn= Radiobutton(gender_frame,text="Male",bg="#CCCCCC",font=("Time",10), variable=x, value="male",pady=5)
female_btn= Radiobutton(gender_frame,text="Female",font=("Time",10),bg="#CCCCCC",variable=x, value="female",pady=5)
others_btn= Radiobutton(gender_frame,text="Others",font=("Time",10),bg="#CCCCCC",variable=x, value="others",pady=5)

gender_frame.grid(row=4, column=1)
male_btn.pack(expand=True, side=LEFT)
female_btn.pack(expand=True, side=LEFT)
others_btn.pack(expand=True, side=LEFT)

select_country = OptionMenu(frame_form,variable,*countries)
select_country.grid(row =5, columnspan=2,sticky=N+S)
window.mainloop()