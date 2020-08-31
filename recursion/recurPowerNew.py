def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)

print(recurPowerNew(2,7))
############
print("Test big O")
n = 5
print([val**n for val in range(n)])
print([2**(val**2) for val in range(n)])
##################
print('a')
a = [1, 2, 3, 4, 0]
print(a[a[0]])
print(a[a[1]])
print(a[a[2]])
print(a[a[3]])
print(a[a[4]])
#print('test',a[a[5]])
print('b')
b = [3, 0, 2, 4, 1]
print(b[b[0]])
print(b[b[1]])
print(b[b[2]])
print(b[b[3]])
print(b[b[4]])
print('test', a[b[2]])

import math
n = 50
print(math.log(n,2))
