# #
# 
# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62
# 
# 
# #

import functools
from MarvellousNum import ChkPrime

def Prime(arr):
  return list(filter(ChkPrime, arr))

def Multi(arr, multiplier):
  return list(map(lambda no: no * multiplier, arr))

def Max(arr):
  return functools.reduce(max, arr)

def main():
  arr = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    arr.append(int(input()))
  
  c = Prime(arr)
  print("List after filter = ", c)

  i = Multi(c, 2)
  print("List after map = ", i)

  result = Max(i)
  print("Output of reduce = ", result)

if __name__ == "__main__":
  main()
  