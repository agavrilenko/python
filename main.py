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

