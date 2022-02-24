# 리스트 복사
a_list = [2, 3, 5]
b_list = a_list

# 리스트 항목 복사
my_list = [2, 3, 5]
new_list = my_list[:]


# 깊은 복사
import copy

a_list = [1, 2, [4, 10]]
c_list = copy.deepcopy(a_list)

# 하위 리스트 추가
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)

# 리스트 항목 추가
a.insert(8)