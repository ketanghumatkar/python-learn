# #
# 
# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
# 
# 
# #

import functools

def Even(arr):
  return list(filter(lambda no: no % 2 == 0, arr))

def Square(arr):
  return list(map(lambda no: no * no, arr))

def Add(arr):
  return functools.reduce(lambda a,b: a + b, arr)

def main():
  arr = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    arr.append(int(input()))
  
  c = Even(arr)
  print("List after filter = ", c)

  i = Square(c)
  print("List after map = ", i)

  result = Add(i)
  print("Output of reduce = ", result)

if __name__ == "__main__":
  main()
  