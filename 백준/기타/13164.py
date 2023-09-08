# 2023-04-18
# 백준 - 그리디
# https://www.acmicpc.net/problem/13164
# 소요 시간 : 18:10 ~ 18:30 (20m)

from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))  # 데이터는 오름차순으로 입력됨

tshirt = []  # 인접한 학생간의 키 차이 저장 배열
for i in range(N - 1):
    tshirt.append(data[i + 1] - data[i])

tshirt.sort()

print(sum(tshirt[0 : N - K]))
