import random

lbound = int(input("Enter Lower bound : "))
ubound = int(input("Enter Upper bound : "))

rand1 = random.randint(lbound,ubound)
rand2 = random.randrange(lbound, ubound + 1)

print(rand1)
print(rand2)