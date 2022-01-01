# #
# 
# 2. Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# 
# #

def PrintPattern(no_of_stars):
  for i in range(no_of_stars):
    for j in range(no_of_stars):
      print("*", end= ' ')
    print()
  print()

def main():
  print("Enter the number: ")
  no_of_stars = int(input())

  PrintPattern(no_of_stars)

if __name__ == "__main__":
  main()