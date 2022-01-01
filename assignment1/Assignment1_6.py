# #
# 
# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero
# 
# 
# #


def ChkNum(val):
  if(val>0):
    print("Positive Number")
  elif(val<0):
    print("Negative Number")
  else:
    print("Zero")

def main():
  print("Enter the number : ")
  no = int(input())

  ChkNum(no)

if __name__ == "__main__":
  main()