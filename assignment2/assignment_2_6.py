# #
# 
# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
# * * * *
# * * *
# * *
# *
# #

def displayPattern(no):
  for i in range(no, 0, -1):
    for j in range(i):
      print("*", end=' ')
    print("\n")

def main():
  print("Enter the number")
  no = int(input())

  displayPattern(no)

if __name__ == "__main__":
  main()