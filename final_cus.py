import mysql.connector as MyConn

def validate_user(ATMNumber, PIN):
    mydb = MyConn.connect(host='localhost', user='root', password='#', database='admin')
    db_cursor = mydb.cursor()
    db_cursor.execute("SELECT * FROM customer WHERE ATMNumber = '{}' AND PIN = '{}'".format(ATMNumber.upper(), PIN.upper()))
    result = db_cursor.fetchone()
    if result:
        return True
    else:
        return False


def check_balance(ATMNumber):
    mydb = MyConn.connect(host='localhost', user='root', password='#', database='admin')
    db_cursor = mydb.cursor()
    db_cursor.execute("SELECT Balance FROM customer WHERE ATMNumber = '{}'".format(ATMNumber.upper()))
    result = db_cursor.fetchone()
    if result:
        Balance = result[0]
        return Balance
    else:
        return None


def withdraw_money(ATMNumber, Balance):
    mydb = MyConn.connect(host='localhost', user='root', password='#', database='admin')
    db_cursor = mydb.cursor()
    db_cursor.execute("UPDATE customer SET Balance = Balance - {} WHERE ATMNumber = '{}'".format(Balance, ATMNumber.upper()))
    mydb.commit()


def deposit_money(ATMNumber, Balance):
    mydb = MyConn.connect(host='localhost', user='root', password='#', database='admin')
    db_cursor = mydb.cursor()
    db_cursor.execute("UPDATE customer SET Balance = Balance + {} WHERE ATMNumber = '{}'".format(Balance, ATMNumber.upper()))
    mydb.commit()


#Function to change the PIN
def change_atm_pin(ATMNumber, old_atm_pin, new_atm_pin):
  connection = MyConn.connect(host="localhost", user="root", password="#", database="admin")
  cursor = connection.cursor()
  query = "UPDATE admin.customer SET PIN = %s WHERE ATMNumber = %s AND PIN = %s"
  cursor.execute(query, (new_atm_pin, ATMNumber, old_atm_pin))
  connection.commit()


def main():
    ATMNumber = input("Enter your ATM Number: ").upper()
    PIN = input("Enter your PIN: ").upper()

    is_valid_user = validate_user(ATMNumber, PIN)

    if is_valid_user:
        # print("Welcome! Your balance is:", check_balance(ATMNumber))
        print("\nWMWWMWMWMWMWMWMWMWMWMWMWMWMWMWMWM")
        print("WM                             WM")
        print("WM     Welcome to ____ ATM.    WM")
        print("WM                             WM")
        print("WMWWMWMWMWMWMWMWMWMWMWMWMWMWMWMWM\n")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">>     Select an Option:       >>")
        print(">>     1. Check Balance        >>")
        print(">>     2. Withdraw Money       >>")
        print(">>     3. Deposit Money        >>")
        print(">>     4. Change PIN           >>")
        print(">>     5. Log Out              >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

        choice = input("Select an option: ")

        if choice=="1":
            print("............................................")
            print("Your Current Balance is Rs.", check_balance(ATMNumber))
            print("............................................")
        elif choice == "2":
            print("............................................")
            Balance = int(input("Enter the amount you want to withdraw: "))
            withdraw_money(ATMNumber, Balance)
            print("Your balance is now Rs.", check_balance(ATMNumber))
            print("............................................")
        elif choice == "3":
            print("............................................")
            Balance = int(input("Enter the amount you want to deposit: "))
            deposit_money(ATMNumber, Balance)
            print("Your balance is now Rs.", check_balance(ATMNumber))
            print("............................................")
        elif choice=="4":
            print("..................................................")
            old_atm_pin=input("Enter your Old PIN: ")
            if PIN==old_atm_pin:
                new_atm_pin=input("Enter your New PIN: ")
                new1_pin=input("Enter your New PIN: ")
                change_atm_pin(ATMNumber, old_atm_pin, new_atm_pin)
                print("__________________________________________________\n")

                print("|  Your ATM PIN has been changed successfully.   |")
                print("|  Thank you for using our ATM. Visit     again. |")
                print("__________________________________________________")
            else:
                print("Wrong PIN entered.")
                print("Try again.")
            print("..............................................")
        elif choice=="5":
            print("\nThank you for using our ATM. Now you are Logged Out....\n\n")
        else:
            print("\nSome invalid option has been selected. Try Again.\n")
    else:
        print("Invalid account number or PIN.\n")


if __name__ == "__main__":
    main()