from tkinter import *

from PIL import Image,ImageTk

from tkinter.font import Font

from tkinter import ttk

import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")
cur=mycon.cursor()

def click_book(N):
     pop2.destroy()
     book=Toplevel()
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
     
     query="select seat_avail from movie where mname='{}';".format(N)
     cur.execute(query)
     avail=cur.fetchall()
     for i in avail:
          a=int(i[0])
     seat_avail=Label(book,text="Seats availaible: {}".format(a),font=("Copperplate gothic",10),bg="#00CCCC",fg="black")
     seat_avail.place(x=290,y=140)

     confirm=Button(book,text="Confirm Booking",font=("Copperplate gothic",10),bg="dark blue",fg="white")
     confirm.place(x=170,y=200)

     #DATA
     name=name.get()
     yob=y.get()
     seats=seats.get()
     
     
          


def details(N):
     g="\n"
     query="select descp,cost_per_head,seat_avail,show_timing,duration_min,genre from movie where mname='{}';".format(N)
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
     global bg
     pop2=Toplevel()
     pop2.title("Book Movie")
     load=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\space.jpg")
     r=ImageTk.PhotoImage(load)
     bg=Label(pop2,image=r)
     bg.place(x=0,y=0)
     
     pop2['bg']="white"
     pop2.geometry("550x400")
     
     #Movie Title
     descp=Label(pop2,text=N,font=("Algerian Regular",20),bg="black",fg="white")
     descp.place(x=200,y=0)

     details(N)

     #Book Button
     book=Button(pop2,text="Book",bg="dark green",fg="white",font=("Copperplate gothic",10),cursor="hand2",command=lambda:click_book(N))
     book.place(x=200,y=300)
     
def destroy_window2():
     window2.destroy()
     open_window2()
     

def open_window2():
     global GB
     global GL
     global window2
     global genre

     window2=Toplevel()
     window2.title="Movie Booking Dashboard"
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
     GB.destroy()
     GL.destroy()
     genre.destroy()

     if n.get()=="Adventure":

          load1=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\ADVENTURE.jpg")
          r1=ImageTk.PhotoImage(load1)
          img12=Label(window2,image=r1)
          img12.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          query1="select * from displayed_movies; where genre='Adventure' and position=1"
          cur.execute(query1)
          data=list(cur.fetchall)
          print(data)
          n1=data[0]
          location=data[0]
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\in.gif"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
    
          #poster2
          n2="Avatar"
          img2=ImageTk.PhotoImage(Image.open("A.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)

          #poster3
          n3="Jumanji-Welcome to the Jungle"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\jumangi.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          
     elif n.get()=="Action":

          loadAC=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\ACTION.jpg")
          rAC=ImageTk.PhotoImage(loadAC)
          img12AC=Label(window2,image=rAC)
          img12AC.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          n1="Avatar"
          img1=ImageTk.PhotoImage(Image.open("A.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)

          #poster2
          n2="Justice League"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\JL.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          
          #poster3
          n3="Inception"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\Inception.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          

     elif n.get()=="Thriller":

          loadT=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\THRILLER.jpg")
          rT=ImageTk.PhotoImage(loadT)
          imgT=Label(window2,image=rT)
          imgT.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          n1="Gravity"
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\Gravity.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)
          
          #poster2
          n2="World War Z"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\WorldWarZ.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)

          #poster3
          n3="Extraction"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\extraction.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
          
     elif n.get()=="Comedy":
          
          loada=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\COMEDY.jpg")
          ra=ImageTk.PhotoImage(loada)
          img125=Label(window2,image=ra)
          img125.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          n1="Home Alone"
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\H.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)

          #poster2
          n2="Jab We Met"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\J.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          
          #poster3
          n3="3 Idiots"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\3Idiots.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)

     
     elif n.get()=="Romance":
          loadR=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\ROMANCE.jpg")
          rR=ImageTk.PhotoImage(loadR)
          img126=Label(window2,image=rR)
          img126.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          n1="Twilight"
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\twilight.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)

          #poster2
          n2="The Parent Trap"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\parenttrap.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          
          #poster3
          n3="The fault in our Stars"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\stars.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)

     elif n.get()=="Kids special":
          loadK=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\KIDS.jpg")
          rK=ImageTk.PhotoImage(loadK)
          img124=Label(window2,image=rK)
          img124.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540) 
          
          #poster1
          n1="Scooby Doo"
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\Scoob.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)

          #poster2
          n2="Tom and Jerry"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\TomJerry.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          
          #poster3
          n3="Phineas and Ferb"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\pf.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)

     elif n.get()=="Horror":
          loadh=Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\HORROR.jpg")
          rh=ImageTk.PhotoImage(loadh)
          img123=Label(window2,image=rh)
          img123.place(x=0,y=0)

          imageB=PhotoImage(file=r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\button.png")
          B=Button(window2,image=imageB, bd=0 ,cursor="hand2",command=destroy_window2)
          B.place(x=580,y=540)
          
          #poster1
          n1="Conjuring 2"
          img1=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\3Idiots.jpg"))
          p1=Button(window2,image=img1,cursor="hand2",command=lambda:open_pop2(n1))
          p1.place(x=290,y=180)

          #poster2
          n2="Annabelle"
          img2=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\annabelle.jpg"))
          p2=Button(window2,image=img2,cursor="hand2",command=lambda:open_pop2(n2))
          p2.place(x=540,y=180)
          
          #poster3
          n3="IT"
          img3=ImageTk.PhotoImage(Image.open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\Movie Posters\it.jpg"))
          p3=Button(window2,image=img3,cursor="hand2",command=lambda:open_pop2(n3))
          p3.place(x=790,y=180)
     
     window2.mainloop()


     

    

