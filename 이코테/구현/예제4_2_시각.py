# 2021-01-26
# 이코테 ch4 구현 예제 4-2 시각

n = int(input())

count = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                count += 1

print(count)

"""
5 -> 11475
"""
