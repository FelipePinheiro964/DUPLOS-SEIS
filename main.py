import random
  ##
# teste de repositorio
 ##
d1 = random.Random()
d2 = random.Random()

rolls = []
double = 0
for i in range(10):
  a = d1.randrange(1, 7)
  b = d2.randrange(1, 7)
  rolls.append( (a,b) )
  print(f'{a}, {b}')
  if a + b == 12:
    print("DUPLO SEIS")
    double = double + 1



print(rolls)
print(double)