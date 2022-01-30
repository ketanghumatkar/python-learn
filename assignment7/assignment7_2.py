##
# 2. Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5
# 
##


def DisplayNumberInReverse(no):
  if(no<2):
    return
  no = no - 1
  DisplayNumberInReverse(no)
  print(no, end=" ")

def main():
  print("Enter the number in sequence : ")
  no = int(input())

  DisplayNumberInReverse(no+1)

if __name__ == "__main__":
  main()