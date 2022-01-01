# #
# 
# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.# 
# 
# 
# #

from Arithmatic import *

def AcceptUserInformation():
  print("Enter first number: ")
  no1 = int(input())

  print("Enter second number: ")
  no2 = int(input())

  return no1, no2

def main():
  no1, no2 = AcceptUserInformation()

  print("Addition of numbers :", Add(no1, no2))
  print("Substraction of numbers :", Sub(no1, no2))
  print("Multiplication of numbers :", Mult(no1, no2))
  print("Division of numbers :", Div(no1, no2))


if __name__ == "__main__":
  main()