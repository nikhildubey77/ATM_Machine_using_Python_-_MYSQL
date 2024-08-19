import random
import mysql.connector as MyConn

def insert_data():
    mydb=MyConn.connect(host='localhost',user='root',password='#', database="Admin")
    db_cursor=mydb.cursor()
    a=input("Enter Customer Name: ")
    a1=input("Enter Customer Aadhar Card Number: ")
    b=input("Enter Customer Account Number: ")
    c=int(input("Enter ATM Number: "))
    d=int(input("Enter ATM Pin: "))
    db_insert="insert into Customer(Name,Id,ATMNumber,PIN) values(%s,%s,%s,%s)"
    db_list=[(a,b,c,d)]
    db_cursor.executemany(db_insert,db_list)
    mydb.commit()
    print(db_cursor.rowcount, "Record inserted")

def check_record():
    mydb=MyConn.connect(host='localhost',user='root',password='#', database="Admin")
    db_cursor = mydb.cursor()
    user_input = input("Enter Customer ATM Number: ")
    user_input1 = input("Enter Customer PIN: ")
    db_cursor.execute("SELECT * FROM customer WHERE PIN = '{}'".format(user_input1))
    result = db_cursor.fetchone()
    if result:
        print("ATM PIN is valid.",result[3])
        a=result[3]
    else:
        print("ATM PIN is not valid.")
    db_cursor.execute("SELECT * FROM customer WHERE ATMNumber = '{}'".format(user_input))
    result = db_cursor.fetchone()
    if result:
        print("Customer ATM Card validated.")
        b=result[4]
        c=result[2]
    else:
        print("Some missmatch has been recorded.")

def update_data():
    mydb=MyConn.connect(host='localhost',user='root',password='#', database="Admin")
    db_cursor=mydb.cursor()
    print("\n||||||||||||||||||||||||||||||||||||||||||")
    print("|| What do you want to Update....       ||")
    print("||     Select an Option                 ||")
    print("||     1. Name                          ||")
    print("||     2. ATM Number                    ||")
    print("||     3. ATM PIN                       ||")
    print("||     4. Add Balance                   ||")
    print("||||||||||||||||||||||||||||||||||||||||||\n")

    choice = input("Enter your choice: ")

    if choice=="1":
        a=input("Enter the Updated ATM Number of the Customer: ")
        b=input("Enter Customer Name: ")
        db_Updatedata="update Admin.Customer set Name=%s where ATMNumber=%s"
        db_value=(b,a)
    elif choice == "2":
        a=input("Enter the Updated ATM Number of the Customer: ")
        b=input("Enter Customer ID Number: ")
        db_Updatedata="update Admin.Customer set ATMNumber=%s where ID=%s"
        db_value=(a,b)
    elif choice=="3":
        b=input("Enter the Customer ATM Number: ")
        a=input("Enter Updated ATM Pin of the Customer: ")
        db_Updatedata="update Admin.Customer set PIN=%s where ATMNumber=%s"
        db_value=(a,b)
    elif choice=='4':
        b=input("Enter the Customer ATM Number: ")
        a=input("Enter Balance: ")
        db_Updatedata="update Admin.Customer set Balance=%s where ATMNumber=%s"
        db_value=(a,b)
    else:
        print("Invalid choice.")

    db_cursor.execute(db_Updatedata,db_value)
    mydb.commit()
    print(db_cursor.rowcount,"Data Updated.")
    

def delete_data():
    mydb=MyConn.connect(host='localhost',user='root',password='#', database="Admin")
    db_cursor=mydb.cursor()
    delete_record="delete from Admin.Customer where ID=%s"
    a=input("Enter Customer ID Number: ")
    db_value=(a,)
    db_cursor.execute(delete_record,db_value)
    mydb.commit()
    print(db_cursor.rowcount,"Data Removed.")


Admin_ID={
    "123456789":{"password":"1234"},
    "987654321":{"password":"4321"}
}

def main():
    admin_number=input("Enter your Admin ID Number: ")
    password=input("Enter the Password: ")

    #Check if the Admin is validated or not
    if admin_number not in Admin_ID or password!=Admin_ID[admin_number]["password"]:
        print("You are not Validated.....Some missmatch has been recorded.")
        return
    print("--------------------------------------------------")
    print("Your Most Welcome to the Manager Portal....")
    print("Let's Begin....")
    print("--------------------------------------------------")
    print("You are logged into the Admin PowerShell.")
    print("Now you can add new or remove existing Customer.\n")
    print("------------------------------------------")
    print("..  Select an Option                    ..")
    print("..  1. Add Data of New Customer         ..")
    print("..  2. Check the record of Customers    ..")
    print("..  3. Update existing Customer data    ..")
    print("..  4. Delete existing Customer data    ..")
    print("..  5. Press 5 to LogOut                ..")
    print("------------------------------------------")

    choice=input("Enter your choice: ")
    if choice=='1':
        insert_data()
    elif choice=='2':
        check_record()
    elif choice=='3':
        update_data()
    elif choice=='4':
        delete_data()
    elif choice=='5':
        print("You are Successfully Logged Out.")
        return
    else:
        print("Invalid choice.")
main()