# #
# 
# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37
# 
# #

def additionOfDigits(no):
  sum = 0
  while(no>0):
    remainder = no%10
    sum = sum + remainder
    no = int(no/10)
  return sum

def main():
  print("Enter the number")
  no = int(float(input()))

  result = additionOfDigits(no)

  print(result)

if __name__ == "__main__":
  main()