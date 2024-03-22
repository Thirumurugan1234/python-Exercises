from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Thirumurugan@1307",database="work")
def insert(id,name,age,city):
    res=con.cursor()
    sql="insert into web (id,name,age,city) values (%s,%s,%s,%s)"
    web=(id,name,age,city)
    res.execute(sql,web)
    con.commit()
    print("Data Insert success")
def update(id,name,age,city):
    res=con.cursor()
    sql="update web set  id=%s,name=%s,age=%s,city=%s where id=%s"
    web=(id,name,age,city,id)
    res.execute(sql,web)
    con.commit()
    print("Data UPDATE success")
    
def select():
    res=con.cursor()
    sql="SELECT id,name,age,city from web"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["id","name","age","city"]))
def delete(id):
    res=con.cursor()
    sql="delete from web where id=%s"
    web=(id,)
    res.execute(sql,web)
    con.commit()
    print("Data DELETE success")
    
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("enter your choice :"))
    if choice ==1:
        id=int(input("enter the id: "))
        name=input("enter name :")
        age=int(input("enter the age :"))
        city=input("enter the city :")
        insert(id,name,age,city)
    elif choice ==2:
        id=int(input("enter the id :"))
        name=input("enter name :")
        age=int(input("enter the age :"))
        city=input("enter the city :")
        update(id,name,age,city)

    elif choice == 3:
        select()

    elif choice ==4:
        id =input("enter the ID to delete :")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid selection select again!")