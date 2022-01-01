# #
# 
# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)
# 
# 
# #

from MarvellousNum import ChkPrime, Addition

def ListPrime(list):
  plist = []
  for i in range(len(list)):
    isPrime = ChkPrime(list[i])
    if(isPrime):
      plist.append(list[i])
  return plist

def main():
  list = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    no = int(input())
    list.append(no)

  plist = ListPrime(list)
  print("Output : ", Addition(plist))

if __name__ == "__main__":
  main()