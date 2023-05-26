from tkinter import *

import ViewerModule

import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")
cur=mycon.cursor()

import ManagerModule

#Sign In window 
window1=Tk()
window1.title("Window 1")
window1["bg"]="Black"
window1.geometry("1550x800")

'''width=window1.winfo_screenwidth()
height=window1.winfo_screenheight()

l=Label(window1,text=f"width:{width} height:{height}")
l.pack()'''

def click_B1():
     global pop1
     global tname
     global tpassword
     pop1=Toplevel(window1)
     pop1.title("Viewer Sign In")
     pop1["bg"]="White"
     
     lname=Label(pop1,text="Enter Username",font=("Copperplate gothic",10),fg="black",bg="white")
     lname.place(x=50,y=25)
     tname=Entry(pop1,width=25)
     tname.place(x=200,y=25)

     lpassword=Label(pop1, text="Enter Password",font=("Copperplate gothic",10),fg="black",bg="white")
     lpassword.place(x=50,y=55)
     tpassword=Entry(pop1,width=25,show="*")
     tpassword.place(x=200,y=55)

     SignUp=Button(pop1,text="Sign Up",font=("Copperplate gothic",10),fg="black",bg="Orange",command=click_SignUp)
     SignUp.place(x=100,y=90)

     sign=Button(pop1,text="Sign In",font=("Copperplate gothic",10),fg="black",bg="light green",command=lambda:click_sign(B1))
     sign.place(x=175,y=90)

     back=Button(pop1,text="Back",font=("Copperplate gothic",10),fg="black",bg="red",command=click_back)
     back.place(x=245,y=90)


     pop1.geometry("550x200")
     pop1.mainloop()

def click_B2():
     global pop1
     global tname
     global tpassword
     pop1=Toplevel(window1)
     pop1.title("Viewer Sign In")
     pop1["bg"]="White"
     
     lname=Label(pop1,text="Enter Username",font=("Copperplate gothic",10),fg="black",bg="white")
     lname.place(x=50,y=25)
     tname=Entry(pop1,width=25)
     tname.place(x=200,y=25)

     lpassword=Label(pop1, text="Enter Password",font=("Copperplate gothic",10),fg="black",bg="white")
     lpassword.place(x=50,y=55)
     tpassword=Entry(pop1,width=25,show="*")
     tpassword.place(x=200,y=55)

     sign=Button(pop1,text="Sign In",font=("Copperplate gothic",10),fg="black",bg="light green",command=lambda:click_sign(B2))
     sign.place(x=175,y=90)

     back=Button(pop1,text="Back",font=("Copperplate gothic",10),fg="black",bg="red",command=click_back)
     back.place(x=245,y=90)


     pop1.geometry("550x200")
     pop1.mainloop()
     

def click_SignUp():
     username=tname.get()
     password=tpassword.get()

     if len(username)>0 and len(password)>0:
          query2=("insert into users (username,password) values(%s,%s);")
          data=(username,password)
          cur.execute(query2,data)
          mycon.commit()

          pop1.destroy()
          ViewerModule.open_window2()

     else:
          lalert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
          lalert.place(x=80,y=145)
     
     
def click_sign(b):
     username=tname.get()
     password=tpassword.get()
     if b==B1:
          if len(username)>0 and len(password)>0:
               cur.execute("use project1;")
               query2=("insert into users (username,password) values(%s,%s);")
               data=(username,password)
               cur.execute(query2,data)
               
               pop1.destroy()
               ViewerModule.open_window2()
          else:
               lalert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
               lalert.place(x=80,y=145)
     if b==B2:
          if len(username)>0 and len(password)>0:
                    cur.execute("use project1;")
                    query2=("insert into users (username,password) values(%s,%s);")
                    data=(username,password)
                    cur.execute(query2,data)
                    pop1.destroy()
                    ManagerModule.open_window3()
          else:
               lalert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
               lalert.place(x=80,y=145)


def click_back():
     pop1.destroy()

    
#Sign In Text
L1=Label(window1,text="Sign In As",font=("Copperplate gothic",25,"underline","bold"),fg="white",bg="black")
L1.place(x=500,y=150)

L2=Label(window1,text="OR",font=("Copperplate gothic",20,"bold"),fg="white",bg="black")
L2.place(x=550,y=230)

#Viewer Sign In
B1=Button(window1,text="Viewer",font=("Copperplate gothic",20,"bold"),fg="white",bg="dark blue",command=click_B1)
B1.place(x=375,y=220)

#Manager Sign In
B2=Button(window1,text="Manager",font=("Copperplate gothic",20,"bold"),fg="white",bg="dark blue",command=click_B2)
B2.place(x=650,y=220)


window1.mainloop()
