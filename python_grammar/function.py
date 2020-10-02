def add(a,b):
  return a+b

print(add(3,7))

a=10
def func():
  global a
  a+=1

for i in range(10):
  func()

