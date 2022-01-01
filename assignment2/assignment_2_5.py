# #
# 
# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number
# 
# #



def isPrime(no):
  i = 2
  while(i<no):
    if(no % i == 0):
      return False
    i = i + 1
  
  return True

def main():
  print("Enter the number")
  no = int(input())

  result = isPrime(no)

  if(result):
    print("It is prime number")
  else:
    print("It is not prime number")

if __name__ == "__main__":
  main()