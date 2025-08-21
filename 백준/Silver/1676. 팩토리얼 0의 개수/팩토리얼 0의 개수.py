import math
n = int(input())
fac = math.factorial(n)
print(len(str(fac)) - len(str(fac).rstrip('0')))