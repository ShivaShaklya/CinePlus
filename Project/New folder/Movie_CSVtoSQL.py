import mysql.connector as con
mycon=con.connect(host="localhost",username="root",passwd="Shiva09@04",database="project1")#change password and database
cur=mycon.cursor()
if mycon.is_connected():
  print("connection successful")


import csv
#will work only of the table is created along with the columns defined
def CSV_to_SQL1():
    query="create table all_movies(mname varchar(30),descp varchar(100),show_timing varchar(40),duration_min int,seat_avail int,cost_per_head int,genre varchar(20),location varchar(30));"
    cur.execute(query)
    mycon.commit()
    with open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\New folder\movie_details.csv","r") as f: #change the name of the file accordingly
        ro=csv.reader(f)
        print(ro)
        for row in ro:
            l=list(row)
            mname=l[0]
            descp=l[1]
            show_timing=l[2]
            duration_min=l[3]
            seat_avail=l[4]
            cost_per_head=l[5]
            genre=l[6]
            location=l[7]
            
            query="INSERT into all_movies Values ('{}','{}','{}',{},{},{},'{}','{}');".format(mname,descp,show_timing,duration_min,seat_avail,cost_per_head,genre,location)
            cur.execute(query)
            mycon.commit()
#
def CSV_to_SQL2():
    query="create table displayed_movies(mname varchar(30),descp varchar(100),show_timing varchar(40),duration_min int,seat_avail int,cost_per_head int,genre varchar(20),location varchar(30),position int);"
    cur.execute(query)
    mycon.commit()
    with open(r"C:\Users\MALTI SHAKLYA\Desktop\Shiva\Python\Project\New folder\displayed.csv","r") as f: #change the name of the file accordingly
        ro=csv.reader(f)
        print(ro)
        for row in ro:
            l=list(row)
            mname=l[0]
            descp=l[1]
            show_timing=l[2]
            duration_min=l[3]
            seat_avail=l[4]
            cost_per_head=l[5]
            genre=l[6]
            location=l[7]
            position=l[8]
            
            query="INSERT into displayed_movies Values ('{}','{}','{}',{},{},{},'{}','{}',{});".format(mname,descp,show_timing,duration_min,seat_avail,cost_per_head,genre,location,position)
            cur.execute(query)
            mycon.commit()
CSV_to_SQL2()        
        
    
