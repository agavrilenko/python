import random
rnd = random.randint(1,10)
while True:
  n = int(input('Enter number:'))
  if n == rnd:
    print('Congrats')
    break
print('Bye!')