##
# 3.Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1 
##


def DisplayNumberInReverse(no):
  if(no<=0):
    return
  print(no, end=" ")
  no = no - 1
  DisplayNumberInReverse(no)

def main():
  print("Enter the number in sequence : ")
  no = int(input())

  DisplayNumberInReverse(no)

if __name__ == "__main__":
  main()