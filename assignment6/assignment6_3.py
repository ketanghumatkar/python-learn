# #
# 
# 
# 
# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.
# 
# #


import marvellous_num as Num

class Arithmatic:

  def __init__(self, value):
    self.value = value

  def check_prime(self):
    return Num.ChkPrime(self.value)

  def check_perfect(self):
    return Num.ChkPerfect(self.value)

  def factors(self):
    return Num.FindFactors(self.value)

  def sum_factors(self):
    return Num.Addition(self.factors())
  
  
def main():

  print("Enter the value")
  val = int(input())

  ar1 = Arithmatic(val)
  print("Is number prime : ", ar1.check_prime())
  print("Is number perfect : ", ar1.check_perfect())
  print("Factor of number : ", ar1.factors())
  print("sum of factors : ", ar1.sum_factors())

if __name__ == "__main__":
  main()
