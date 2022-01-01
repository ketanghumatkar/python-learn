# #
# 
# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56 
# 
# #

def Max(list):
  max = list[0]
  for i in range(len(list)):
    if(list[i]>max):
      max = list[i]
  return max

def main():
  list = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    no = int(input())
    list.append(no)

  result = Max(list)
  print("Output :", result)

if __name__ == "__main__":
  main()