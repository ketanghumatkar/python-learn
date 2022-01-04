# #
# 
# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects.
# 
# #

class Circle:
  PI = 3.14

  def __init__(self, radius=0.0):
      self.radius = radius
      self.area = 0.0
      self.circumference = 0.0
  
  def accept(self):
    print("Please enter the radius of circle : ")
    self.radius = float(input())

  def calculate_area(self):
    self.area = 2 * Circle.PI * pow(self.radius, 2)

  def calculate_circumference(self):
    self.circumference = 2 * Circle.PI * self.radius

  def display(self):
    print("Radius of circle : ", self.radius)
    print("Circumference of circle : ", self.circumference)
    print("Area of circle : ", self.area)

  def calculate_and_display(self):
    self.calculate_area()
    self.calculate_circumference()
    self.display()

def main():
  
  c1 = Circle()
  c1.display()

  c2 = Circle()
  c2.accept()
  c2.display()

  # accessing instance methods
  c3 = Circle()
  c3.accept()
  c3.calculate_circumference()
  c3.calculate_area()
  c3.display()

  c4 = Circle()
  c4.accept()
  c4.calculate_and_display()

  c4 = Circle()
  c4.accept()
  c4.calculate_and_display()

  # accessing instance variables
  c5 = Circle()
  print("Radius of circle : ", c5.radius)
  print("Circumference of circle : ", c5.circumference)
  print("Area of circle : ", c5.area)

  # intializing value in constructor
  print("Please enter the radius of circle : ")
  radius = float(input(0))
  c5 = Circle(radius)
  c5.calculate_and_display()

if __name__ == "__main__":
  main()