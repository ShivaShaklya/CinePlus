import mysql.connector as mycon
mycon=mycon.connect(host="localhost",username="root",passwd="payal",database="project1")
if mycon.is_connected():
 print("database opened successfully")
else:
 print("error opening database")



cur=mycon.cursor()

def deletemovie():
    #enter movie to be deleted: name
    name=input("enter movie to be deleted")
    query="DELETE from movie where mname='{}'".format(name)
    cur.execute(query)
    mycon.commit()
deletemovie()
