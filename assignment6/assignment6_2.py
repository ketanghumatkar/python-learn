# #
# 
# #
# 
# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.
# 
# #


class BankAccount:
  ROI = 10.5;

  def __init__(self, name):
    self.name = name
    self.amount = 0

  def display(self):
    print("Name of Account: ", self.name)
    print("Amount of Account: ", self.amount)

  def deposit(self, amt):
    self.amount = self.amount + amt
    return amt

  def withdraw(self, amt):
    self.amount = self.amount - amt
    return amt

  def calculate_intrest(self):
    return self.amount * BankAccount.ROI/100

  
def main():

  print("Enter the first account details")
  print("Tell me account name: ")
  acc_name = input()

  ac1 = BankAccount(acc_name)
  ac1.display()
  print("How much you would like to deposit ")
  deposite_amt = int(input())
  ac1.deposit(deposite_amt)
  print("How much you would like to withdraw : ")
  withdraw_amt = int(input())
  ac1.withdraw(withdraw_amt)
  ac1.display()
  print("You would get {} interest on your account".format(ac1.calculate_intrest()))
  
  print("Enter the second account details")
  print("Tell me account name: ")
  acc_name = input()

  ac2 = BankAccount(acc_name)
  ac2.display()
  print("How much you would like to deposit ")
  deposite_amt = int(input())
  ac2.deposit(deposite_amt)
  print("How much you would like to withdraw : ")
  withdraw_amt = int(input())
  ac2.withdraw(withdraw_amt)
  ac2.display()
  print("You would get {} interest on your account".format(ac1.calculate_intrest()))


if __name__ == "__main__":
  main()
