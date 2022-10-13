# 2022-10-13
# week2 - 자료구조. 쇠막대기
# https://www.acmicpc.net/problem/10799
# 소요시간 : 14:15 ~ 15:25 (60m)
import sys

input = sys.stdin.readline

data = input().replace("\n", "")

cutting_stick = 0
total_stick = 0
razor = []

i = 0
while i < len(data):
    if data[i] == "(":
        # 쇠막대기 등장
        if i != len(data) - 1 and data[i + 1] != ")":
            cutting_stick += 1
            total_stick += 1
        # 레이저 등장
        elif i != len(data) - 1 and data[i + 1] == ")":
            razor.append(cutting_stick) # 몇개의 막대기를 지나가는지 count
            i += 2
            continue
    # 쇠막대기 끝
    else:
        cutting_stick -= 1
    i += 1

print(sum(razor) + total_stick)
