def ChkPrime(no):
  i = 2
  while(i < no):
    if(no%i == 0):
      return False
    i = i + 1
  return True