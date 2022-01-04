# #
# 
# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18
# 
# 
# #

def Multi(val1, val2):
  m = lambda v1, v2: v1 * v2
  return m(val1, val2)

def main():
  print("Enter first number : ")
  no1 = int(input())
  print("Enter second number : ")
  no2 = int(input())
  
  result = Multi(no1, no2)
  print("Output : ", result)

if __name__ == "__main__":
  main()