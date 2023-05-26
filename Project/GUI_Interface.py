

from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import ViewerModule

import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")
cur=mycon.cursor()

from PIL import Image,ImageTk

from tkinter.font import Font

import ManagerModule

#Sign In window 
window1=Tk()
window1.title("Window 1")
window1.geometry("1300x800")
load=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Bg.jpg")
render=ImageTk.PhotoImage(load)
img=Label(window1,image=render)
img.place(x=0,y=0)


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

     register=Button(pop1,text="Register",font=("Copperplate gothic",10),fg="black",bg="Orange",cursor="hand2",command=click_register)
     register.place(x=100,y=90)

     sign=Button(pop1,text="Sign In",font=("Copperplate gothic",10),fg="black",bg="light green",cursor="hand2",command=lambda:click_sign(B1))
     sign.place(x=175,y=90)

     back=Button(pop1,text="Back",font=("Copperplate gothic",10),fg="black",bg="red",cursor="hand2",command=click_back)
     back.place(x=245,y=90)


     pop1.geometry("550x200")
     pop1.mainloop()

def click_B2():
     global pop1
     global tname
     global tpassword
     pop1=Toplevel(window1)
     pop1.title("Manager Sign In")
     pop1["bg"]="White"
     
     lname=Label(pop1,text="Enter Username",font=("Copperplate gothic",10),fg="black",bg="white")
     lname.place(x=50,y=25)
     tname=Entry(pop1,width=25)
     tname.place(x=200,y=25)

     lpassword=Label(pop1, text="Enter Password",font=("Copperplate gothic",10),fg="black",bg="white")
     lpassword.place(x=50,y=55)
     tpassword=Entry(pop1,width=25,show="*")
     tpassword.place(x=200,y=55)

     sign=Button(pop1,text="Sign In",font=("Copperplate gothic",10),fg="black",bg="light green",cursor="hand2",command=lambda:click_sign(B2))
     sign.place(x=100,y=90)

     change=Button(pop1,text="Change Password",font=("Copperplate gothic",10),fg="black",bg="Orange",cursor="hand2",command=lambda:change_password(tname.get()))
     change.place(x=168,y=90)
     
     back=Button(pop1,text="Back",font=("Copperplate gothic",10),fg="black",bg="red",cursor="hand2",command=click_back)
     back.place(x=300,y=90)


     pop1.geometry("550x200")
     pop1.mainloop()
     

def click_register():
     global l1alert
     username=tname.get()
     
     password=tpassword.get()

     if len(username)>0 and len(password)>0:
           cur.execute("use project1;")
           query2=("select username from users;")
           cur.execute(query2)
           data=cur.fetchall()
           try:
                if username not in data:
                    query2=("insert into users (username,password) values(%s,%s);")
                    data=(username,password)
                    cur.execute(query2,data)
                    mycon.commit()

                    pop1.destroy()
                    ViewerModule.open_window2()
                
           except:
                l1alert.destroy()
                l1alert=Label(pop1,text="username already exists, kindly try another username",font=("Copperplate gothic",10),bg="#3399FF",fg="white")
                l1alert.place(x=80,y=145)

     else:
          l1alert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
          l1alert.place(x=80,y=145)
     
     
def click_sign(b):
     username=tname.get()
     password=tpassword.get()
     global l1alert
     if b==B1:
          if len(username)>0 and len(password)>0:
               cur.execute("use project1;")
               query2=("select username,password from users;")
               cur.execute(query2)
               data=cur.fetchall()

               if (username,password) in data:
                    pop1.destroy()
                    ViewerModule.open_window2()
               else:
                    l1alert.destroy()
                    l1alert=Label(pop1,text="Incorrect username or password",font=("Copperplate gothic",10),bg="orange",fg="white")
                    l1alert.place(x=80,y=145)
                    
          else:
               l1alert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
               l1alert.place(x=80,y=145)
     if b==B2:
          if len(username)>0 and len(password)>0:
               query2=("select username,password from managers;")
               cur.execute(query2)
               data=cur.fetchall()
               if (username,password) in data:
                    pop1.destroy()
                    ManagerModule.open_window3()
                      
               else:
                    l2alert=Label(pop1,text="Incorrect username or password",font=("Copperplate gothic",10),bg="orange",fg="white")
                    l2alert.place(x=80,y=145)
                         
          else:
               lalert=Label(pop1,text="Check if data has been inserted correctly and try again",font=("Copperplate gothic",10),bg="dark red",fg="white")
               lalert.place(x=80,y=145)


def click_back():
     pop1.destroy()

def new_password(user,recent,new):

     print(user)
      
     query="select password from managers where username='{}'".format(user)
     cur.execute(query)
     data=cur.fetchall()

     for i in data:
          if list(i)==[recent]:
               query="update managers set password='{}' where username='{}'".format(new,user)
               cur.execute(query)
               mycon.commit()

               messagebox.showinfo(title="Change Password",message="Password changed Successfully")
               change.destroy()
               print("Password updated")
   
          else:
               change.destroy()
               messagebox.showerror(title="Change Password", message="Password Incorrect")
               print("Incorrect Password")


def change_password(username):
     global change 

     pop1.destroy()

     change=Toplevel(window1)
     change.title("Change Password")
     change["bg"]="White"
     change.geometry("550x200")
     
     userL=Label(change,text="Enter current username: ",font=("Copperplate gothic",10),fg="black",bg="white")
     userL.place(x=50,y=25)

     userT=ttk.Entry(change,width=25)
     userT.place(x=200,y=25)

     recentL=Label(change,text="Enter current password: ",font=("Copperplate gothic",10),fg="black",bg="white")
     recentL.place(x=50,y=50)

     recentT=ttk.Entry(change,width=25)
     recentT.place(x=200,y=50)

     newL=Label(change,text="Enter new password: ",font=("Copperplate gothic",10),fg="black",bg="white")
     newL.place(x=60,y=75)
              
     newT=ttk.Entry(change,width=25)
     newT.place(x=210,y=75)

     
     C=Button(change,text="Enter",font=("Copperplate gothic",10),fg="black", bg="blue",command=lambda:new_password(userT.get(),recentT.get(),newT.get()))
     C.place(x=150,y=100)
     

          
     
def csv_write():
     import csv
     
     #Movie
     f=open("Movie_Details.csv","w",newline="")
     w=csv.writer(f)
     q=("select * from movie")
     cur.execute(q)
     d=cur.fetchall()
     w.writerows(d)

     #users
     f=open("User_Details.csv","w",newline="")
     w=csv.writer(f)
     q=("select * from users")
     cur.execute(q)
     d=cur.fetchall()
     w.writerows(d)

     #Managers
     f=open("Manager_Details.csv","w",newline="")
     w=csv.writer(f)
     q=("select * from managers")
     cur.execute(q)
     d=cur.fetchall()
     w.writerows(d)
     print("data inserted")

     #Displayed movies
     import csv
     f=open("Displayed_movies.csv","w",newline="")
     w=csv.writer(f)
     q=("select * from movies")
     cur.execute(q)
     d=cur.fetchall()
     w.writerows(d)
     print("data inserted")
     
    
#Sign In Text

f=Font(family="Craftsman PERSONAL USE",size="62")
img=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\T.png")
L=Label(window1,image=img,bg="black")
L.place(x=400,y=60)

'''L2=Label(window1,text="OR",font=("Copperplate gothic",20,"bold"),fg="white",bg="black")
L2.place(x=550,y=230)'''

#Viewer Sign In
img1=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\viewer.png")
B1=Button(window1,image=img1, bd=0,bg="black",activebackground="#000000",cursor="hand2",command=click_B1)
B1.place(x=400,y=237)

#Manager Sign In
img2=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\manager.png")
B2=Button(window1,image=img2,bd=0,bg="#000000",activebackground="#000000",cursor="hand2",command=click_B2)
B2.place(x=660,y=237)

#csvfile_write()

window1.mainloop()
