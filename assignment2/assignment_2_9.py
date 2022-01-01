# #
# 
# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7
# 
# #

def noOfDigits(no):
  i = 1
  while(no>10):
    no = int(no/10)
    i = i + 1
  return i

def main():
  print("Enter the number")
  no = int(float(input()))

  result = noOfDigits(no)

  print(result)

if __name__ == "__main__":
  main()