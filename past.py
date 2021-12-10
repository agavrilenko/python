from utility import *
from time import time
import random


#Exception handling
while True:
  try:
    age = 10# int(input('tell me your age: '))
    10/age
  except ValueError as err:
    print(err)
    continue
  except ZeroDivisionError as err1:
    print(err1)
    raise err1
  else:
    print(f'we are good age is {age}')  
  finally:
    print('I\'m done')  
  print ('Bye!')  
  break


#decorator - interseptor
def another_dec_func(func):
  def wrapper(*args, **kwargs):
    start = time()
    print('****WRAPPING*****')
    result = func(*args,**kwargs)
    print('****END WRAPPING*****')
    print(f'took {time() - start}')
    return result
  return wrapper

@another_dec_func
def hello(msg):
  print(msg)

hello('yahoo')


def decorator_function(func):
  def wrapper():
    print('******')
    func()
    print('*****')
  return wrapper

@decorator_function
def hey():
    print('hello')

hey()

dup_list = ['a','b','c','c','b','d','e']
duplicates = list( {v for v in dup_list if dup_list.count(v)>1 })
print(duplicates)



basket = [1,2,3,4,5,5]
s = set(basket)
print(type({1,2,3}))
if True :
  print("he")
else: 
  print("ho")
count=0
while count<1:
  count+=1
  print("up")

def by_two(item):
  return item*2

print(list(map(by_two, [1,2,3,4])))
print(list(map(lambda item: item**2,[1,2,3,4,5])))

a = [(0,1), (4,6), (-10,5)]
a.sort(key = lambda key: key[1])
print(a)

even_list = [item**2 for item in range(0,100) 
if item %2 == 0]
print(even_list)
# same idea for set but use {} instead of []
# dictionary
my_dict = {'a': 2, 'b':5}
new_dict = {k:v**2 for k,v in my_dict.items() if v%2==1}
print(new_dict)
new_dict = {str(k):k*2 for k in [1,2,3,4,5]}
print(new_dict)

#Generators

class MyGen():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __next__(self):
    if MyGen.current <= self.last :
      num = MyGen.current
      MyGen.current += 1
      return num;    
    raise StopIteration  

  def __iter__(self):
    return self

gen = MyGen(1,100)
for i in gen:
  print(i)


def generator_func(num):
  for i in range(num):
    yield i*3

g = generator_func(5)
print(next(g))
print(next(g))
print(next(g))


def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    tmp = a
    a = b
    b = tmp + b

for x in fib(1):
  print(x)


def multiply(*args):
  tmp = 1
  for i in args:
    tmp=tmp*i;
  return tmp

print(multiply(1,2,3,4,5,6,7,9))

def factorial(number):
  tmp = 1
  for i in range(1,number):
    tmp = tmp*i;
  return tmp

print(factorial(100))
print(__name__)
## de duplication
data = [1,2,3,4,4.5,3,4.5,6,1,2]
dups = {}
for x in data:
  if dups.get(x) is None:
    dups[x] = 0
  dups[x] = dups.get(x) + 1
for dup in dups.items():
  if dup[1] > 1:
    print(dup)

rnd = random.randint(1,10)
while True:
  n = int(input('Enter number:'))
  if n == rnd:
    print('Congrats')
    break
print('Bye!')
