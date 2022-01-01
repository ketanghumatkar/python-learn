# #
# 
# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5
# 
# 
# #

def Min(list):
  min = list[0]
  for i in range(len(list)):
    if(list[i]<min):
      min = list[i]
  return min

def main():
  list = []
  print("Number of elements : ")
  size = int(input())

  print("Input Elements : ")
  for i in range(size):
    no = int(input())
    list.append(no)

  result = Min(list)
  print("Output :", result)

if __name__ == "__main__":
  main()