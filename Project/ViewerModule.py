from tkinter import *

from PIL import Image,ImageTk

from tkinter.font import Font

from tkinter import ttk

from tkinter import messagebox

import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")
cur=mycon.cursor()

def click_book(N):
     global book
     pop2.destroy()
     book=Toplevel(window2)
     book.title("Enter Details")
     book['bg']="#00CCCC"
     book.geometry("500x400")

     nameL=Label(book,text="Enter Name",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     nameL.place(x=100,y=20)
     name=ttk.Entry(book,width=20)
     name.place(x=180,y=20)

     dobL=Label(book,text="Select Year of Birth",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     dobL.place(x=100,y=80)
     
     #creating birth year list
     year=[]
     for i in range(2021,1920,-1):
          year+=[i]
     #
     y=IntVar()
     dob=ttk.Combobox(book,textvariable=y)
     dob['values']=year
     dob.place(x=240,y=80)
     dob.current(0)

     seatsL=Label(book,text="No. of Seats to be Booked",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     seatsL.place(x=100,y=140)
     
     seats=ttk.Entry(book,width=5)
     seats.place(x=260,y=140)
     
     query="select seat_avail from displayed_movies where mname='{}';".format(N)
     cur.execute(query)
     avail=cur.fetchall()
     for i in avail:
          a=int(i[0])
     seat_avail=Label(book,text="Seats availaible: {}".format(a),font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     seat_avail.place(x=290,y=140)

     confirm=Button(book,text="Confirm Booking",font=("Copperplate gothic",10),bg="dark blue",fg="white",command=lambda:BookingDetails_toSQL(name,seats,y,N))
     confirm.place(x=170,y=200)

     book.mainloop()


def BookingDetails_toSQL(name,seats,y,N):
     #ADD DATE TIME STAMP
     try:
          query="create table booking_details (name varchar(25),yob int,mname varchar(40),seats_booked int);"
          cur.execute(query)
    
          query="insert into booking_details VALUES('{}',{},'{}',{})".format(name.get(),y.get(),N,seats.get())
          cur.execute(query)
     except:
          query="insert into booking_details VALUES('{}',{},'{}',{})".format(name.get(),y.get(),N,seats.get())
          cur.execute(query)
          

     #
     query="select seat_avail from displayed_movies where mname='{}';".format(N)
     cur.execute(query)
     avail=cur.fetchall()
     for i in avail:
          a=int(i[0])
     new_seats=a-int(seats.get())
     query1="update displayed_movies set seat_avail={} where mname='{}';".format(new_seats,N)
     cur.execute(query1)
     query2="update all_movies set seat_avail={} where mname='{}';".format(new_seats,N)
     cur.execute(query2)
     mycon.commit()

     #CREATE INVOICE
     book.destroy()
     messagebox.showinfo(message="BOOKING CONFIRMED",parent=window2)
     

def details(N):
     global s
     g="\n"
     query="select descp,cost_per_head,seat_avail,show_timing,duration_min,genre from displayed_movies where mname='{}';".format(N)
     cur.execute(query)
     data=cur.fetchall()
     print(data)
     for i in data:
          i=list(i)
          s="Description: {}".format(i[0])+g+"Cost per seat: {}".format(i[1])+g+"Seats Availaible: {}".format(i[2])+g+"Show Timings: {}".format(i[3])+g+"Duration: {}".format(i[4])+"min"+g+"genre: {}".format(i[5])
          print(s)
     descp=Label(pop2,text=s,font=("Copperplate gothic",15),bg="black",fg="white")
     descp.place(x=100,y=50)


def open_pop2(N):
     global pop2
     pop2=Toplevel(window2)
     pop2.title("Book Movie")
     pop2['bg']="black"
     pop2.geometry("550x400")
     
     #Movie Title
     descp=Label(pop2,text=N,font=("Algerian Regular",20),bg="black",fg="white")
     descp.place(x=200,y=0)

     details(N)

     #Book Button
     img=ImageTk.PhotoImage(Image.open("book.png"))
     book=Button(pop2,image=img,bg="black",activebackground="black",border=0,cursor="hand2",command=lambda:click_book(N))
     book.place(x=200,y=250)

     pop2.mainloop()
     
def destroy_window2():
     window2.destroy()
     open_window2()
     

def open_window2():
     global GB
     global GL
     global window2
     global genre

     window2=Toplevel()
     window2.title("Movie Booking Dashboard")
     window2.geometry("1300x800")
     load=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\H12.jpg")
     r=ImageTk.PhotoImage(load)
     img=Label(window2,image=r)
     img.place(x=0,y=0)
     
     #genre Combobox
     n=StringVar()
     genre=ttk.Combobox(window2,textvariable=n)
     genre['values']=["Action","Adventure","Thriller","Comedy","Romance","Horror","Kids special"]
     genre.place(x=300,y=200)
     genre.current(0)
     
     GL=Label(window2,text="Choose a Genre")
     GL.place(x=200,y=200)
     GB=Button(window2,text="GO",cursor="hand2",command=lambda:choice(n))
     GB.place(x=500,y=200)
     
     window2.mainloop()

def choice(n):
     global img1,img2,img3

     if n.get()=="Adventure":
          GB.destroy()
          GL.destroy()
          genre.destroy()
          
          load1=Image.open("ADVENTURE.jpg")
          r1=ImageTk.PhotoImage(load1)
          img12=Label(window2,image=r1)
          img12.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)

          
          #poster1
          query1="select * from displayed_movies where genre='Adventure' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()
    
          #poster2
          query1="select * from displayed_movies where genre='Adventure' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()

          #poster3
          query1="select * from displayed_movies where genre='Adventure' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()
          
     elif n.get()=="Action":

          loadAC=Image.open("ACTION.jpg")
          rAC=ImageTk.PhotoImage(loadAC)
          img12AC=Label(window2,image=rAC)
          img12AC.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Action' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Action' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Action' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()
          

     elif n.get()=="Thriller":

          loadT=Image.open("THRILLER.jpg")
          rT=ImageTk.PhotoImage(loadT)
          imgT=Label(window2,image=rT)
          imgT.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Thriller' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Thriller' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Thriller' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()
          
     elif n.get()=="Comedy":
          
          loada=Image.open("COMEDY.jpg")
          ra=ImageTk.PhotoImage(loada)
          img125=Label(window2,image=ra)
          img125.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Comedy' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Comedy' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Comedy' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()
     
     elif n.get()=="Romance":
          loadR=Image.open("ROMANCE.jpg")
          rR=ImageTk.PhotoImage(loadR)
          img126=Label(window2,image=rR)
          img126.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Romance' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Romance' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Romance' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()

     elif n.get()=="Kids special":
          loadK=Image.open("KIDS.jpg")
          rK=ImageTk.PhotoImage(loadK)
          img124=Label(window2,image=rK)
          img124.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540) 
          
          #poster1
          query1="select * from displayed_movies where genre='Kids' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Kids' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Kids' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()

     elif n.get()=="Horror":
          loadh=Image.open("HORROR.jpg")
          rh=ImageTk.PhotoImage(loadh)
          img123=Label(window2,image=rh)
          img123.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Horror' and position=1;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Horror' and position=2;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Horror' and position=3;"
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          mycon.commit()
     
     window2.mainloop()
     

    

