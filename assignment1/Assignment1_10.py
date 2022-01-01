# #
# 
# 
# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10
# 
# 
# #

def LengthOfStr(str):
  return len(str)

def main():
  print("Enter the name: ")
  str = input()
  
  result = LengthOfStr(str)
  print("Otuput : ", result)

if __name__ == "__main__":
  main()