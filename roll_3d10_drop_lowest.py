import random

def roll():
  d1 = random.randrange(1,11)
  d2 = random.randrange(1,11)
  d3 = random.randrange(1,11)
  if d1 <= d2:
    if d2 <= d3:
      result = d2 + d3
    elif d1 <= d3:
      result = d2 + d3
    else:
      result = d1 + d2
  elif d2 <= d3:
    result = d1 + d3
  else:
    result = d1 + d2
  print("roll {} result: {}".format(x,result))
  return result

x=0
total = 0
while x < 10000:
  total += roll()
  x += 1
print(total/10000)
