# 2021-01-26
# 이코테 ch4 구현 실전 문제 2 왕실의 나이트

now = input()  # 열행

x = int(now[1])  # row
y = ord(now[0]) - 96  # column

# 파이썬 알파벳->아스키코드 변환 문법 : ord() / 반대는 chr()

dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

count = 0

for i in range(len(dx)):
    if 1 <= x + dx[i] <= 8 and 1 <= y + dy[i] <= 8:
        count += 1

print(count)

"""
TC 1 -> 2
a1
TC 2 -> 6
c2
"""
