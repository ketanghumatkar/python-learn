# #
# 
# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.
# 
# #

class Arithmatic:

  def __init__(self):
      self.value1 = 0 
      self.value2 = 0
  
  def accept(self):
    print("Please enter first number : ")
    self.value1 = int(input())

    print("Please enter second number : ")
    self.value2 = int(input())

  def addition(self):
    return self.value1 + self.value2

  def substraction(self):
    return self.value1 - self.value2

  def multiplication(self):
    return self.value1 * self.value2

  def division(self):
    try:
      result = self.value1 / self.value2
    except ZeroDivisionError:
      result = 0
    return result

  def display(self):
    print("Addition : ", self.addition())
    print("Substraction : ", self.multiplication())
    print("Multiplication : ", self.substraction())
    print("Division : ", self.division())

def main():
  c1 = Arithmatic()
  c1.display()

  c2 = Arithmatic()
  c2.accept()
  c2.display()

  # accessing instance methods
  c3 = Arithmatic()
  c3.accept()
  print("Addition : ", c3.addition())
  print("Substraction : ", c3.multiplication())
  print("Multiplication : ", c3.substraction())
  print("Division : ", c3.division())

  c4 = Arithmatic()
  c4.accept()
  c4.display()


if __name__ == "__main__":
  main()