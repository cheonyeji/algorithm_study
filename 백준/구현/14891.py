# 2023-08-28 (소요시간 : )
# 구현 골드5. 백준 14891 톱니바퀴 https://www.acmicpc.net/problem/14891

from sys import stdin
from collections import deque

input = stdin.readline

gear = [[]]

for _ in range(4):
    gear.append(deque(list(input().rstrip())))

K = int(input())

# 1 : 시계(right), -1 : 반시계(left)
for _ in range(K):
    idx, dir_ = map(int, input().split(" "))

    gear_idx2 = gear[idx][2]
    gear_idx6 = gear[idx][6]
    # 본인만 돌리기
    if dir_ == 1:
        gear[idx].rotate(1)
    else:
        gear[idx].rotate(-1)

    # 회전시키면서 변경될 데이터(기준이 되는 인덱스, 방향 저장용) copy_ 생성
    copy_idx = idx
    copy_dir_ = dir_
    # 왼쪽에 기어 존재
    while copy_idx - 1 >= 1:
        # 반대 방향 회전
        if gear_idx6 != gear[copy_idx - 1][2]:
            gear_idx6 = gear[copy_idx - 1][6]
            if copy_dir_ == 1:
                gear[copy_idx - 1].rotate(-1)
                copy_dir_ = -1
            else:
                gear[copy_idx - 1].rotate(1)
                copy_dir_ = 1
            copy_idx -= 1
        # 더이상 살펴볼 필요 없음
        else:
            break

    copy_idx = idx
    copy_dir_ = dir_
    # 오른쪽에 기어 존재
    while copy_idx + 1 <= 4:
        # 반대 방향 회전
        if gear_idx2 != gear[copy_idx + 1][6]:
            gear_idx2 = gear[copy_idx + 1][2]
            if copy_dir_ == 1:
                gear[copy_idx + 1].rotate(-1)
                copy_dir_ = -1
            else:
                gear[copy_idx + 1].rotate(1)
                copy_dir_ = 1
            copy_idx += 1
        # 더이상 살펴볼 필요 없음
        else:
            break

answer = 0
for i in range(1, 5):
    if gear[i][0] == "1":
        answer += 2 ** (i - 1)

print(answer)
