# #
# 
# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3
# 
# 
# #

def Frequency(list, search):
  j = 0
  for i in range(len(list)):
    if(list[i] == search):
      j = j + 1
  return j

def main():
  list = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    no = int(input())
    list.append(no)

  print("Element to search : ")
  search = int(input())

  result = Frequency(list, search)
  print("Output :", result)

if __name__ == "__main__":
  main()