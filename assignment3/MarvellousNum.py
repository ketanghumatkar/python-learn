def ChkPrime(no):
  i = 2
  while(i < no):
    if(no%i == 0):
      return False
    i = i + 1
  return True

def Addition(list):
  sum = 0
  for i in range(len(list)):
    sum =  sum + list[i]
  return sum
