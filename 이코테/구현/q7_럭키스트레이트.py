# 2021-01-26
# 이코테 ch12 구현 문제 Q7 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

n = input()

left = 0
right = 0

for i in n[: len(n) // 2]:
    left += int(i)

for j in n[len(n) // 2 :]:
    right += int(j)

if left == right:
    print("LUCKY")
else:
    print("READY")

"""
TC 1 -> LUCKY
123402
TC 2 -> READY
7755
"""
