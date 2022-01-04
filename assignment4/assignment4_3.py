# #
# 
# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
# 
# 
# #

import functools

def Compare(arr):
  return list(filter(lambda no: (no > 70 and no <= 90), arr))

def IncreaseBy10(arr):
  return list(map(lambda no: no + 10, arr))

def Multi(arr):
  return functools.reduce(lambda a,b: a * b, arr)

def main():
  arr = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    arr.append(int(input()))
  
  c = Compare(arr)
  print("List after filter = ", c)

  i = IncreaseBy10(c)
  print("List after map = ", i)

  result = Multi(i)
  print("Output of reduce = ", result)

if __name__ == "__main__":
  main()
  