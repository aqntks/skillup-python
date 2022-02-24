
dict = {}

for i in ['a', 'b', 'c', 'd']:
    dict[i] = dict.get(i, 0) + 1

print(dict)


setA = {1, 2, 3, 4}
setB = {3, 4, 5}
setUnion = setA | setB
setIntersect = setA & setB
setXOR = setA ^ setB
setSub = setA - setB

print(setUnion)
print(setIntersect)
print(setXOR)
print(setSub)