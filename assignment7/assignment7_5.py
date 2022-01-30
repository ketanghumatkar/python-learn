##
# 5. Write a recursive program which accept number from user and return its
# factorial.
# Input : 5
# Output : 120
##


def factorial(no):
  if(no==1):
    return 1
  return no * factorial(no-1)

def main():
  print("Enter the number : ")
  n = int(input())

  print("Factorial of number is : ", factorial(n))

if __name__ == "__main__":
  main()