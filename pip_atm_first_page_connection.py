from subprocess import call

def main():
    print("\nWelcome to 5G BOYS Advance ATM Management System.\n")
    print("Select whether you are Admin or Customer.")
    print("*************************************")
    print("**         1. Admin                **")
    print("**         2. Regular Customer     **")
    print("**         3. Exit                 **")
    print("*************************************\n")
    choice=input("Enter your Choice: ")
    if choice=='1':
        def open_py_file():
            call(["python","pip_atm_admin.py"])
        open_py_file()
    elif choice=='2':
        def open_py_file():
            call(["python","pip_atm_4th_final_cus.py"])
        open_py_file()
    elif choice=='3':
        return
    else:
        print("Invalid Choice.")

main()