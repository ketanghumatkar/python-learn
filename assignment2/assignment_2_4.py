# #
# 
# 
# 4.Write a program which accept one number fromm user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)
# 
# 
# #

def FindFactors(no):
  factors = []
  itr = 1
  while(no > itr):
    if(no % itr == 0):
      factors.insert(len(factors), itr)
    itr = itr + 1

  return factors

def Addition(arr):
  sum = 0
  for x in arr:
    sum = sum + x
  return sum

def main():
  print("Enter the number: ")
  no = int(input())
  print("Factors are : ", FindFactors(no))
  print("Addition of factors is :", Addition(FindFactors(no)))


if __name__ == "__main__":
  main()