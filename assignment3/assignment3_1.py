# #
# 
# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130
# 
# 
# #

def Addition(list):
  sum = 0
  for i in range(len(list)):
    sum = sum + list[i]
  return sum

def main():
  list = []
  print("Enter the size of in list : ")
  size = int(input())

  print("Enter the elements of list: ")
  for i in range(size):
    no = int(input())
    list.append(no)

  result = Addition(list)
  print(result)

if __name__ == "__main__":
  main()