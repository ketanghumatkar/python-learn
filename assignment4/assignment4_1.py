# #
# 
# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64 
# 
# 
# #

def PowerOf2(no):
  p = lambda n: pow(n, 2)
  return p(no)

def main():
  print("Enter the element : ")
  no = int(input())
  result = PowerOf2(no)
  print("Output : ", result)

if __name__ == "__main__":
  main()