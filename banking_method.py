

import sys
import random
from account import Account

class Banking():

    def _init_(self):
        print("Welcome To Online Banking.....\n"
              "Press 1 to login to account.\n"
              "Press 2 for create new account.\n"
              "Press 3 to exit this page.")
        n1=int(input('enter your choice :'))
        if n1==1:
            x=int(input("enter your  pin :"))
            y=input("enter your Password :")
            self.username = x
            self.password = y
            self.login()
        elif n1==2:
            self.new()
        elif n1 == 3:
            print("THANK YOU ",{Account[self.username]['user']})
            sys.exit()
        else:
            print("EEROR.. Enter the correct Option")
            self._init_()


    def login(self):
        if self.username in Account and self.password in Account[self.username]['Password']:
            self.home_page()
        else:
            print("Invalid username or password")
            self._init_()

    def home_page(self):
        print("welcome to ICIC Banking.... ",Account[self.username]['user'])
        print("1.Check Account Balance.\n"
              "2.Deposit Money\n"
              "3.Withdraw Money\n"
              "4.Exit")
        n2=int(input("Enter the choice :"))
        if n2 == 1:
            self.balance()
        elif n2 == 2 :
            self.deposit()
        elif n2 == 3 :
            self.withdraw()
        elif n2 == 4:
            print("Thank You...")
            self._init_()
        else:
            print("EEROR.. Enter the correct Option")
            self.home_page()


    def balance(self):
        print("your account balance is",Account[self.username]["Balance"])
        self.home_page()

    def deposit(self):
        dep_amt=int(input('Enter the depositing amount :'))
        print("deposit successful ")
        print("current balance :",Account[self.username]["Balance"]+dep_amt)
        with open("account.py","r") as f1:
           dp = f1.read().replace(f"{Account[self.username]['Balance']}",
                                  f"{Account[self.username]['Balance'] + dep_amt}")
        with open("account.py", "w") as f1:
            f1.write(dp)
        self.home_page()

    def withdraw(self):
        withdraw_amt=int(input("Enter the withdraw amount :"))
        if withdraw_amt <=Account[self.username]["Balance"]:
            print("Amount of ",withdraw_amt,"depited from your account.\n"
            "Current account balance:",Account[self.username]["Balance"]-withdraw_amt)
            with open("account.py","r") as f:
                wi = f.read().replace(f"{Account[self.username]['Balance']}",f"{Account[self.username]['Balance'] - withdraw_amt}")
            with open("account.py","w") as f:
                f.write(wi)
            self.home_page()
        else:
            print(" ERROR.....Insufficient balance")
            self.withdraw()



    def new(self):
        print("create  username & password for your account")
        user =input("enter the username :")
        pas =input(" create password :")
        repass = input("conform password :")
        pin = random.randint(1000,9999)
        if pas == repass:
            phone_no = int(input("Enter your number :"))
            bal = int(input("Depositing amount :"))
            if pin not in Account:
                Account[pin] = {'user':user,'Password':repass,'pin':pin,'Balance':bal,'Phone':phone_no}
                with open("account.py","w") as file:
                    file.write(f"Account ={Account}\n")
                print(f"Account created Login Again ......")
                print("Your 4 digit login pin is :",f"{Account[pin]['pin']}")
                self._init_()
            else:
                print('Account alredy exit')
                self.new()
        else:
            print("enter the correct passowrd")
            self.new()

a1=Banking()
a1._init_()