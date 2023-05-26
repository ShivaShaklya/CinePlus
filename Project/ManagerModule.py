from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")
cur=mycon.cursor()

from PIL import ImageTk,Image

def open_window3():
     global window3
     window3=Toplevel()
     window3.title("Movie Booking Dashboard-Manager")
     window3.geometry("1300x800")

     #Background
     Back=ImageTk.PhotoImage(Image.open(r"AD.jpg"))
     img_B=Label(window3,image=Back,border=0)
     img_B.place(x=0,y=0)

     #Sign In Button
     img1=PhotoImage(file=r"Booking.png")
     B1=Button(window3,image=img1, bd=0 , bg="#000000" , activebackground="#000000",command=booking_details)
     B1.place(x=535,y=175)
     
     img2=PhotoImage(file=r"update.png")
     B2=Button(window3,image=img2, bd=0 , bg="#000000" , activebackground="#000000",command=update_poster)
     B2.place(x=550,y=275)
     
     img3=PhotoImage(file=r"db.png")
     B3=Button(window3,image=img3, bd=0, bg="#000000", activebackground="#000000",command=database_change)
     B3.place(x=535,y=375)

     window3.mainloop()
     
def booking_details():
     booking=Toplevel()
     booking.title("Booking Details")
     booking.geometry("790x320")
     booking['bg']="black"

     query="select * from booking_details"
     cur.execute(query)
     data=cur.fetchall()
     mycon.commit()
     #records=''
     #for record in data:
          #records+=str(list(record))+"\n"
     #print_records=Label(booking,text=records,bg="black",fg="white")
     #print_records.place(x=20,y=20)

     rec_display=ttk.Treeview(booking,height=15)
     rec_display["columns"]=("name","yob","mname","seats")
     rec_display.column("#0",width=120)
     rec_display.column("name",width=190)
     rec_display.column("yob",width=200)
     rec_display.column("mname",width=160)
     rec_display.column("seats",width=120)

     rec_display.heading("#0",text="Sno.")
     rec_display.heading("name",text="Customer Name")
     rec_display.heading("yob",text="Year Of Birth")
     rec_display.heading("mname",text="Movie Name")
     rec_display.heading("seats",text="Seats Booked")
     
     print(len(data))

     scrollbar=ttk.Scrollbar(booking,orient=VERTICAL,command=rec_display.yview)
     rec_display.configure(yscroll=scrollbar.set)
     scrollbar.place(x=1260,y=0)

     for i in range(0,len(data)):
          rec_display.insert(parent='',index='end',iid=i,text=i+1,values=data[i])
          
     rec_display.place(x=0,y=0)

     A=Label(booking,text="SELECT AND SCROLL...",bg="black",fg="white",font=(90))
     A.place(x=500,y=510)
     

def update_poster():
     global poster,n
     global GB,GL,genre
     poster=Toplevel()
     poster.title(r"Add\\Delete\\Update\\Poster")
     poster.geometry("1300x800")
     poster['bg']="black"

     load=Image.open(r"HOME.jpg")
     r=ImageTk.PhotoImage(load)
     img=Label(poster,image=r)
     img.place(x=0,y=0)

     n=StringVar()
     genre=ttk.Combobox(poster,textvariable=n)
     genre['values']=["Action","Adventure","Thriller","Comedy","Romance","Horror","Kids special"]
     genre.place(x=300,y=200)
     genre.current(0)
     
     GL=Label(poster,text="Choose a Genre")
     GL.place(x=200,y=200)
     GB=Button(poster,text="GO",cursor="hand2",command=lambda:show_poster(n))
     GB.place(x=500,y=200)

     poster.mainloop()


def show_poster(n):
     global img1,img2,img3

     if n.get()=="Adventure":
          GB.destroy()
          GL.destroy()
          genre.destroy()
          
          load1=Image.open("ADVENTURE.jpg")
          r1=ImageTk.PhotoImage(load1)
          img12=Label(poster,image=r1)
          img12.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)

          
          #poster1
          query1="select * from displayed_movies where genre='Adventure' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()
    
          #poster2
          query1="select * from displayed_movies where genre='Adventure' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()

          #poster3
          query1="select * from displayed_movies where genre='Adventure' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()
          
     elif n.get()=="Action":

          loadAC=Image.open("ACTION.jpg")
          rAC=ImageTk.PhotoImage(loadAC)
          img12AC=Label(poster,image=rAC)
          img12AC.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Action' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Action' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Action' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()
          

     elif n.get()=="Thriller":

          loadT=Image.open("THRILLER.jpg")
          rT=ImageTk.PhotoImage(loadT)
          imgT=Label(poster,image=rT)
          imgT.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Thriller' and position=1;"
          
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Thriller' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Thriller' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()
          
     elif n.get()=="Comedy":
          
          loada=Image.open("COMEDY.jpg")
          ra=ImageTk.PhotoImage(loada)
          img125=Label(poster,image=ra)
          img125.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Comedy' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Comedy' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Comedy' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()
     
     elif n.get()=="Romance":
          loadR=Image.open("ROMANCE.jpg")
          rR=ImageTk.PhotoImage(loadR)
          img126=Label(poster,image=rR)
          img126.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Romance' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Romance' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Romance' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()

     elif n.get()=="Kids special":
          loadK=Image.open("KIDS.jpg")
          rK=ImageTk.PhotoImage(loadK)
          img124=Label(poster,image=rK)
          img124.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540) 
          
          #poster1
          query1="select * from displayed_movies where genre='Kids' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Kids' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Kids' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()

     elif n.get()=="Horror":
          loadh=Image.open("HORROR.jpg")
          rh=ImageTk.PhotoImage(loadh)
          img123=Label(poster,image=rh)
          img123.place(x=0,y=0)

          imageB=PhotoImage(file="button.png")
          B=Button(poster,image=imageB, bd=0 ,cursor="hand2",command=destroy_poster)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies where genre='Horror' and position=1;"
          c=1
          cur.execute(query1)
          data=list(cur.fetchall())
          n1=data[0][0]
          location=data[0][-2]
          img1=ImageTk.PhotoImage(Image.open(location))
          p1=Button(poster,image=img1,cursor="hand2",command=lambda:open_poster(n1,1))
          p1.place(x=290,y=180)
          mycon.commit()

          #poster2
          query1="select * from displayed_movies where genre='Horror' and position=2;"
          c=2
          cur.execute(query1)
          data=list(cur.fetchall())
          n2=data[0][0]
          location=data[0][-2]
          img2=ImageTk.PhotoImage(Image.open(location))
          p2=Button(poster,image=img2,cursor="hand2",command=lambda:open_poster(n2,2))
          p2.place(x=540,y=180)
          mycon.commit()
          
          #poster3
          query1="select * from displayed_movies where genre='Horror' and position=3;"
          c=3
          cur.execute(query1)
          data=list(cur.fetchall())
          n3=data[0][0]
          location=data[0][-2]
          img3=ImageTk.PhotoImage(Image.open(location))
          p3=Button(poster,image=img3,cursor="hand2",command=lambda:open_poster(n3,3))
          p3.place(x=790,y=180)
          mycon.commit()
     
     poster.mainloop()

def open_poster(N,c):
     global update
     update=Toplevel()
     update.title("Booking Details")
     update['bg']="#003399"
     update.geometry("500x400")

     mnameL=Label(update,text="Enter New Movie Name",font=("Copperplate gothic",10),bg="#003399",fg="white")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(update,width=20)
     mnameT.place(x=200,y=20)

     Enter=Button(update,text="Enter",font=("Copperplate gothic",10),bg="#003399",fg="white",command=lambda:click_enter(mnameT,c))
     Enter.place(x=170,y=40)

     update.mainloop()
     
     
def click_enter(mnameT,c):
     try:
          query1="select * from all_movies where mname='{}';".format(mnameT.get())
          cur.execute(query1)
          i=cur.fetchone()
          print(i)
          mname=i[0]
          descp=i[1]
          show_timing=i[2]
          duration_min=i[3]
          seat_avail=i[4]
          cost_per_head=i[5]
          genre=i[6]
          location=i[7]
          position=c

          query2="""update displayed_movies set mname='{}',
                    descp='{}',
                    show_timing='{}',
                    duration_min={},
                    seat_avail={},
                    cost_per_head={},
                    location='{}'
                    where genre='{}' and position={}""".format(mname,descp,show_timing,duration_min,seat_avail,cost_per_head,location,genre,position)
          cur.execute(query2)
          mycon.commit()
          update.destroy()
          messagebox.showinfo(message="Poster Updated",parent=window3)
          destroy_poster()

     except:
          messagebox.showerror(message="Check whether the movie exists in the data base and try again",parent=database)
     

def database_change():
     global img1,img2,img3,img4
     global database
     
     database=Toplevel(window3)
     database.title("Database Changes")

     database.geometry("1300x800")
     
     load=Image.open("DC.jpg")
     r=ImageTk.PhotoImage(load)
     A=Label(database,image=r,border=0)
     A.place(x=0,y=0)

     
     img1=PhotoImage(file="view.png")
     B1=Button(database,image=img1, bd=0 , bg="#000000" , activebackground="#000000",command=show_movies)
     B1.place(x=535,y=175)
     
     img2=PhotoImage(file="change.png")
     B2=Button(database,image=img2, bd=0 , bg="#000000" , activebackground="#000000",command=change_details)
     B2.place(x=535,y=275)
     
     img3=PhotoImage(file="add.png")
     B3=Button(database,image=img3, bd=0, bg="#000000", activebackground="#000000",command=add_new)
     B3.place(x=535,y=375)

     img4=PhotoImage(file="delete.png")
     B4=Button(database,image=img4, bd=0, bg="#000000", activebackground="#000000",command=delete_movie)
     B4.place(x=535,y=475)

     database.mainloop()
     

def show_movies():
     
     all_movies=Toplevel()
     all_movies.title("Booking Details")
     all_movies.geometry("500x400")
     all_movies['bg']="black"

     query="select * from all_movies;"
     cur.execute(query)
     data=cur.fetchall()
     mycon.commit()
     #records=''
     #for record in data:
          #records+=str(list(record))+"\n"
     #print_records=Label(all_movies,text=records,bg="black",fg="white")
     #print_records.place(x=20,y=20)

     rec_display=ttk.Treeview(all_movies,height=20)
     rec_display["columns"]=("mname","description","show_timing","duration_min","seat_avail","cost_per_head","genre","location")
     rec_display.column("#0",width=120)
     rec_display.column("mname",width=190)
     rec_display.column("description",width=200)
     rec_display.column("show_timing",width=160)
     rec_display.column("duration_min",width=120)
     rec_display.column("seat_avail",width=120)
     rec_display.column("cost_per_head",width=120)
     rec_display.column("genre",width=120)
     rec_display.column("location",width=110)

     rec_display.heading("#0",text="Sno.")
     rec_display.heading("mname",text="Movie Name")
     rec_display.heading("description",text="Description")
     rec_display.heading("show_timing",text="Show Timing")
     rec_display.heading("duration_min",text="Duration(in min)")
     rec_display.heading("seat_avail",text="Seats Availaible")
     rec_display.heading("cost_per_head",text="Cost Per Seat")
     rec_display.heading("genre",text="Genre")
     rec_display.heading("location",text="Poster Location")
     print(len(data))

     scrollbar=ttk.Scrollbar(all_movies,orient=VERTICAL,command=rec_display.yview)
     rec_display.configure(yscroll=scrollbar.set)
     scrollbar.place(x=1260,y=0)
     

     for i in range(0,len(data)):
          rec_display.insert(parent='',index='end',iid=i,text=i+1,values=data[i])
          
     rec_display.place(x=0,y=0)

     A=Label(all_movies,text="SELECT AND SCROLL...",bg="black",fg="white",font=(90))
     A.place(x=500,y=510)

     all_movies.mainloop()
       
def change_details():
     global cd
     
     cd=Toplevel()
     cd.title("Booking Details")
     cd['bg']="black"
     cd.geometry("500x400")

     img11=PhotoImage(file="seat.png")
     B1=Button(cd,image=img11, bd=0 , bg="#000000" , activebackground="#000000",command=change_seats)
     B1.place(x=90,y=75)
     
     img21=PhotoImage(file="st.png")
     B2=Button(cd,image=img21, bd=0 , bg="#000000" , activebackground="#000000",command=change_showtiming)
     B2.place(x=90,y=175)
     
     img31=PhotoImage(file="cost.png")
     B3=Button(cd,image=img31, bd=0, bg="#000000", activebackground="#000000",command=change_cost)
     B3.place(x=90,y=275)

     cd.mainloop()
     
def change_seats():
     cd.destroy()
     
     n1=Toplevel()
     n1.title("Booking Details")
     n1['bg']="black"
     n1.geometry("500x400")

     mnameL=Label(n1,text="Enter New Movie Name",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(n1,width=20)
     mnameT.place(x=300,y=20)

     seatsL=Label(n1,text="Enter Seats Availaible",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     seatsL.place(x=100,y=40)
     seatsT=ttk.Entry(n1,width=20)
     seatsT.place(x=300,y=40)

     img=PhotoImage(file="ENTER.png")
     e=Button(n1,image=img,bd=0, bg="#000000",activebackground="#000000",command=lambda:up1(seatsT,mnameT))
     e.place(x=190,y=80)

     n1.mainloop()

def up1(seatsT,mnameT):
     
     query1="UPDATE displayed_movies set seat_avail={} where mname='{}';".format(seatsT.get(),mnameT.get())
     cur.execute(query1)
     query2="UPDATE all_movies set seat_avail={} where mname='{}';".format(seatsT.get(),mnameT.get())
     cur.execute(query2)
     mycon.commit()
     
     messagebox.showinfo(title=None,message="DATABASE SUCCESSFULLY UPDATED",parent=database)
     n1.destroy()

def change_showtiming():
     global n2
     cd.destroy()
     
     n2=Toplevel()
     n2.title("Booking Details")
     n2['bg']="black"
     n2.geometry("500x400")

     mnameL=Label(n2,text="Enter New Movie Name",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(n2,width=20)
     mnameT.place(x=300,y=20)

     show_timingL=Label(n2,text="Enter new show timings",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     show_timingL.place(x=100,y=40)
     show_timingT=ttk.Entry(n2,width=20)
     show_timingT.place(x=300,y=40)

     img=PhotoImage(file="ENTER.png")
     e=Button(n2,image=img,bd=0, bg="#000000",activebackground="#000000",command=lambda:up2(show_timingT,mnameT))
     e.place(x=190,y=80)

     n2.mainloop()

     
def up2(show_timingT,mnameT):
     
     query1="UPDATE displayed_movies set show_timing='{}' where mname='{}';".format(show_timingT.get(),mnameT.get())
     cur.execute(query1)
     query2="UPDATE all_movies set show_timing='{}' where mname='{}';".format(show_timingT.get(),mnameT.get())
     cur.execute(query2)
     mycon.commit()
     messagebox.showinfo(title=None,message="DATABASE SUCCESSFULLY UPDATED",parent=database)
     n2.destroy()
     

def change_cost():
     cd.destroy()
     global n3
     
     n3=Toplevel()
     n3.title("Booking Details")
     n3['bg']="black"
     n3.geometry("500x400")

     mnameL=Label(n3,text="Enter New Movie Name",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(n3,width=20)
     mnameT.place(x=300,y=20)

     costL=Label(n3,text="Enter cost per seat",font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     costL.place(x=100,y=40)
     costT=ttk.Entry(n3,width=20)
     costT.place(x=300,y=40)

     img=PhotoImage(file="ENTER.png")
     e=Button(n3,image=img,bd=0, bg="#000000",activebackground="#000000",command=lambda:up3(costT,mnameT))
     e.place(x=190,y=80)

     n3.mainloop()
     
def up3(costT,mnameT):
     
     query1="UPDATE displayed_movies set cost_per_head={} where mname='{}';".format(costT.get(),mnameT.get())
     cur.execute(query1)
     query2="UPDATE all_movies set cost_per_head={} where mname='{}';".format(costT.get(),mnameT.get())
     cur.execute(query2)
     mycon.commit()
     messagebox.showinfo(title=None,message="DATABASE SUCCESSFULLY UPDATED",parent=database)
     n3.destroy()

     
    
def add_new():
     global new
     new=Toplevel()
     new.title("Booking Details")
     new['bg']="#003399"
     new.geometry("500x400")

     mnameL=Label(new,text="Enter New Movie Name",font=("Copperplate gothic",10),bg="#003399",fg="white")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(new,width=20)
     mnameT.place(x=300,y=20)

     descpL=Label(new,text="Enter Description",font=("Copperplate gothic",10),bg="#003399",fg="white")
     descpL.place(x=100,y=40)
     descpT=ttk.Entry(new,width=20)
     descpT.place(x=300,y=40)

     show_timingL=Label(new,text="Enter Show Time",font=("Copperplate gothic",10),bg="#003399",fg="white")
     show_timingL.place(x=100,y=60)
     show_timingT=ttk.Entry(new,width=20)
     show_timingT.place(x=300,y=60)

     durationL=Label(new,text="Enter Duration in Minutes",font=("Copperplate gothic",10),bg="#003399",fg="white")
     durationL.place(x=100,y=80)
     durationT=ttk.Entry(new,width=10)
     durationT.place(x=300,y=80)

     seat_availL=Label(new,text="Enter Seats Availaible",font=("Copperplate gothic",10),bg="#003399",fg="white")
     seat_availL.place(x=100,y=100)
     seat_availT=ttk.Entry(new,width=20)
     seat_availT.place(x=300,y=100)

     cost_per_headL=Label(new,text="Enter Cost Per Seat",font=("Copperplate gothic",10),bg="#003399",fg="white")
     cost_per_headL.place(x=100,y=120)
     cost_per_headT=ttk.Entry(new,width=20)
     cost_per_headT.place(x=300,y=120)

     genreL=Label(new,text="Enter Genre",font=("Copperplate gothic",10),bg="#003399",fg="white")
     genreL.place(x=100,y=140)
     genreT=ttk.Entry(new,width=20)
     genreT.place(x=300,y=140)

     locationL=Label(new,text="Enter Location of movie poster",font=("Copperplate gothic",10),bg="#003399",fg="white")
     locationL.place(x=100,y=160)
     locationT=ttk.Entry(new,width=20)
     locationT.place(x=300,y=160)

     img=PhotoImage(file="ENTER.png")
     Enter=Button(new,image=img, bd=0, bg="#003399", activebackground="#003399",command=lambda:enter_movie(mnameT,descpT,show_timingT,durationT,seat_availT,cost_per_headT,genreT,locationT))
     Enter.place(x=170,y=220)

     new.mainloop()

def enter_movie(mnameT,descpT,show_timingT,durationT,seat_availT,cost_per_headT,genreT,locationT):
     query="insert into all_movies values ('{}', '{}', '{}', {}, {}, {},'{}', '{}')".format(mnameT.get(), descpT.get(), show_timingT.get(), durationT.get(), seat_availT.get(), cost_per_headT.get(),genreT.get(),locationT.get())
     cur.execute(query)
     mycon.commit()

     messagebox.showinfo(title=None,message="MOVIE SUCCESSFULLY ADDED",parent=database)
     new.destroy()

def delete_movie():
     global update
     update=Toplevel()
     update.title("Delete Movie Record")
     update['bg']="#003399"
     update.geometry("500x400")

     mnameL=Label(update,text="Enter Movie To Be Deleted",font=("Copperplate gothic",10),bg="#003399",fg="white")
     mnameL.place(x=100,y=20)
     mnameT=ttk.Entry(update,width=20)
     mnameT.place(x=270,y=20)

     img=PhotoImage(file="ENTER.png")
     Enter=Button(update,image=img,bd=0, bg="#003399",activebackground="#003399",command=lambda:enter_delete(mnameT))
     Enter.place(x=190,y=60)

     update.mainloop()

def enter_delete(mnameT):
     query="DELETE from all_movies where mname='{}'".format(mnameT.get())
     cur.execute(query)
     mycon.commit()

     messagebox.showinfo(title=None,message="MOVIE SUCCESSFULLY DELETED",parent=database)
     update.destroy()
     
     
def destroy_poster():
     poster.destroy()
     update_poster()
