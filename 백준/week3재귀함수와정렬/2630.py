# 2022-10-18
# week3 - 재귀함수와 정렬. 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 소요시간 : 14:14 ~ 14:47 (40m)

import sys

input = sys.stdin.readline

N = int(input())
data = []

for _ in range(N):
    data.append(list(map(int, input().split(" "))))

white = 0
blue = 0


def cutting(row, col, length):
    global white, blue
    # 1칸
    if length == 1:
        if data[row][col] == 0:
            white += 1
        elif data[row][col] == 1:
            blue += 1
    else:
        CUT = False
        check = data[row][col]

        # 전체 칸 훑기
        for i in range(row, row + length):
            if CUT:
                break
            for j in range(col, col + length):
                if data[i][j] != check:
                    CUT = True
                    break
        # 쪼개야 하는 경우
        if CUT:
            cutting(row, col, length // 2)
            cutting(row, col + length // 2, length // 2)
            cutting(row + length // 2, col, length // 2)
            cutting(row + length // 2, col + length // 2, length // 2)

        # 색종이가 될 수 있는 경우
        else:
            if check == 0:
                white += 1
            else:
                blue += 1


cutting(0, 0, N)
print(white)
print(blue)
