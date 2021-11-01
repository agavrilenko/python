
from time import time

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
