
# 제너레이터 예제

import sys
import time


def make_list():
    lists = []
    for i in range(0, 10000):
        lists.append(i)
    return lists


def generator():
    for i in range(0, 10000):
        yield i


list_time = time.time()
my_list = make_list()
for i in my_list:
    print(i)
list_finish_time = time.time() - list_time


gen_time = time.time()
my_gen = generator()
for i in my_gen:
    print(i)
gen_finish_time = time.time() - gen_time


list_com_time = time.time()
list_comprehension = [x for x in range(0, 10000)]
for i in list_comprehension:
    print(i)
list_com_finish_time = time.time() - list_com_time


gen_com_time = time.time()
gen_comprehension = (x for x in range(0, 10000))
for i in gen_comprehension:
    print(i)
gen_com_finish_time = time.time() - gen_com_time


print("list size {} Byte time {}".format(sys.getsizeof(my_list), list_finish_time))
print("generator size {} Byte time {}".format(sys.getsizeof(my_gen), gen_finish_time))
print("list comprehension size {} Byte time {}".format(sys.getsizeof(list_comprehension), list_com_finish_time))
print("generator comprehension size {} Byte time {}".format(sys.getsizeof(gen_comprehension), gen_com_finish_time))
