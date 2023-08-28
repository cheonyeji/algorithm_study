# 2023-08-28 (소요시간 : 53m)
# 구현 실버2. 백준 2477 참외밭 https://www.acmicpc.net/problem/2477

from sys import stdin

input = stdin.readline

K = int(input())

x, y = 0, 0
max_x, max_y = -int(1e9), -int(1e9)
min_x, min_y = int(1e9), int(1e9)

data = []

# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
for _ in range(6):
    data.append(list(map(int, input().split(" "))))

pos = []
pos_x = []
pos_y = []
for dir_, len_ in data:
    # 동
    if dir_ == 1:
        x += len_
    # 서
    elif dir_ == 2:
        x -= len_
    # 남
    elif dir_ == 3:
        y -= len_
    # 북
    else:
        y += len_

    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

    pos.append([x, y])
    pos_x.append(x)
    pos_y.append(y)

pos_x = list(set(pos_x))
pos_y = list(set(pos_y))

pos_x.remove(max_x)
pos_x.remove(min_x)
pos_y.remove(max_y)
pos_y.remove(min_y)

middle_x = pos_x.pop()
middle_y = pos_y.pop()

w = max_x - min_x
h = max_y - min_y

inner_w = 0
inner_h = 0

# ㄴ자
if [max_x, max_y] not in pos:
    inner_w = max_x - middle_x
    inner_h = max_y - middle_y
# ㄱ자
elif [min_x, min_y] not in pos:
    inner_w = middle_x - min_x
    inner_h = middle_y - min_y
# 90도 회전 ㄴ자
elif [min_x, max_y] not in pos:
    inner_w = middle_x - min_x
    inner_h = max_y - middle_y
else:
    inner_w = max_x - middle_x
    inner_h = middle_y - min_y


print(K * (w * h - inner_w * inner_h))
