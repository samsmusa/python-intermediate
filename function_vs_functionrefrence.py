"""
THis script tell us about function and funciton uses
as we know, function can be call directly or refrences
beacuse why?
"""

def sum(a, b):
  return a + b

def mul(c, d):
  return c * d

def arrySum(func, arry):
  sum = 0
  for i in range(0,len(arry), 2):
    sum += func(arry[i], arry[i+1])

  return sum

print(arrySum(sum, [1,2,3,4,5,6]))