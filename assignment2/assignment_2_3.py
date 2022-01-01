# #
# 
# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120
# 
# #
def Factorial(no):
  sum = 1
  for i in range(1, no+1):
    sum = sum * i
  return sum

def main():
  print("Enter the number: ")
  no = int(input())

  print("Factorial is :", Factorial(no))

if __name__ == "__main__":
  main()