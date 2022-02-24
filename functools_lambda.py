# functools.reduce

import functools

def plus(a, b):
    return a+b

result = functools.reduce(plus, [5, 10, 15])

print(result)

result2 = functools.reduce(lambda x, y: x+y, [5, 10, 15])

print(result2)

# 리스트
list1 = [i for i in range(0, 10) if i > 4]
# set
set1 = {i for i in range(0, 10) if i > 4}
# 딕셔너리
dict1 = {i: i for i in range(0, 10) if i > 4}

print(list1)
set1.add(3)
set1.add(7)
print(set1)
print(dict1)