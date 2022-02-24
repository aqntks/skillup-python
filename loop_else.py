

## break 문 걸리면 else 통과 안함
## 그 외에 통과

sum = 0
for i in range(0, 1000):
    sum += 0
    if i == 500:
        print("good")
        break
else:
    print("no")

sum2 = 0
while sum2 < 1000:
    sum2 += 1
    break
else:
    print("nono")