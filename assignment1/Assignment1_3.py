# #
# 
# 3. Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16# 
# 
# 
# #


def Add(val1, val2):
  return val1 + val2

def main():
  print("Please give first number: ")
  no1 = int(input())
  print("Please give second number: ")
  no2 = int(input())
  
  sum = Add(no1, no2)
  print("Addition is: ", sum)


if __name__ == "__main__":
  main()