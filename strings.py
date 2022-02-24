
# 2진수 - > 10 진수
n = int("10001", 2)

print(n)


# 대소문자 구별 없이 비교

check = "taken".casefold() == "TaKEn".casefold()
print(check)

# 역방향

str = "show me the money"
str2 = str[::-1]
print(str2)

# join
str_list = []
for s in "show me the money":
    str_list.append(s)

print("".join(str_list))


# 함수들
str_test = "test"

len(str_test)
max(str_test)
min(str_test)
reversed(str_test)
sorted(str_test)
# bin(str_test)
# hex(str_test)
# oct(str_test)
str_test.isalnum()
str_test.isalpha()
str_test.isdecimal()
str_test.isdigit()
str_test.isidentifier()
str_test.islower()
str_test.isprintable()
str_test.isspace()
str_test.istitle()
str_test.isupper()


# 대소문자 서로 변환
str_test.swapcase()


# 검색 교체
# 앞이 맞으면
str_test.startswith("check")
# 뒤가 맞으면
str_test.endswith("check")

# 찾기
str_test.find("check")
# 뒤부터 찾기
str_test.rfind("check")

str_test.strip()
str_test.lstrip()
str_test.rstrip()

# 자리맞춤
str_test.ljust(5)
str_test.rjust(5)
str_test.center(5)
str_test.zfill(5)

