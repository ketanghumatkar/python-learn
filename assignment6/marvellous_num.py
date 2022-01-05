def ChkPrime(no):
  i = 2
  while(i < no):
    if(no%i == 0):
      return False
    i = i + 1
  return True

def FindFactors(no):
  factors = []
  itr = 1
  while(no > itr):
    if(no % itr == 0):
      factors.insert(len(factors), itr)
    itr = itr + 1

  return factors

def ChkPerfect(n):
  sum = 0
  for i in range(1, n):
      if(n % i == 0):
          sum = sum + i
  if (sum == n):
    return True
  return False

def Addition(arr):
  sum = 0
  for x in arr:
    sum = sum + x
  return sum