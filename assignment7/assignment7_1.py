##
# 1. Write a recursive program which display below pattern.
# Input : 5
# Output : * * * * *
##


def DisplayPattern(no):
  if(no<=0):
    return
  print("*", end=" ")
  no = no - 1
  DisplayPattern(no)

def main():
  print("Enter the numnber of * to print : ")
  no = int(input())

  DisplayPattern(no)

if __name__ == "__main__":
  main()