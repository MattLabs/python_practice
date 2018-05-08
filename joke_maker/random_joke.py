import random
lines = open('random_joke.txt').read().splitlines()
myline =random.choice(lines)
print(myline)