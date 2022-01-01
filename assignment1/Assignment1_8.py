# #
# 
# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *
#  
# 
# #

def PrintNoOfStars(no):
  while(no>0):  
    print("*", end=' ')
    no = no - 1
    
def main():
  print("Enter the number: ")
  no = int(input())

  PrintNoOfStars(no)


if __name__ == "__main__":
  main()