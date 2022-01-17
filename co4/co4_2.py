class bank:
 bal=0
 def __init__(self,accno,name,ac_type,bal):
  self.accno=accno
  self.name=name
  self.ac_type=ac_type
  self.bal=bal

 def display(self):
  print("\nAccount Info:")
  print("Account Number:",self.accno)
  print("Account Name:",self.name)
  print("Account Type:",self.ac_type)
  print("Account Balance:",self.bal)

 def deposit(self):
  dep=int(input("Enter the amount to deposit:"))
  self.bal=self.bal+dep

 def withdraw(self):
   w=int(input("Enter the amount to withdraw:"))
   if w > self.bal:
     print("Insufficient Balance")
   else:
     self.bal=self.bal-w
     print("RS-",w,"Withdrawn successfully")

acc_no=int(input("Enter the Account Number:"))
acc_name=input("Enter the name:")
acc_type=input("Enter the account type-(savings/current):")
balance=int(input("Enter the initial balance:"))
b1=bank(acc_no,acc_name,acc_type,balance)

while(1):
 print("\n1.Account Info\n2.Deposit\n3.Withdraw\n4.Exit")
 opt=int(input("Select your option:"))
 if opt == 1:
  b1.display()
 elif opt == 2:
  b1.deposit()
 elif opt == 3:
  b1.withdraw()
 elif opt == 4:
  print("Exited")
  break
 else:
  print("Invalid Option")



