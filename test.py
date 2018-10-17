import random


g = [7, 10, 12, 11, 19]

g = str(g)
g = g.replace('[', '')
g = g.replace(']', '')
g = g.replace(' ', '')
print(g)
g = g.split(',')
print(g)
h = []
for i in g:
    h.append(int(i))
g = h
print(g)

