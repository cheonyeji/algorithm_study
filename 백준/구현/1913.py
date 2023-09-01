# 2023-09-01 (소요시간 : 30m)
# 구현 [실버3. 백준 1913 달팽이] (https://www.acmicpc.net/problem/1913)

from sys import stdin

input = stdin.readline

N = int(input())

target = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
start = N // 2
count = N // 2

x = start
y = start
num = 1


def up(count):
    global num, x, y
    for _ in range(count):
        x -= 1
        num += 1
        graph[x][y] = num


def right(count):
    global num, x, y
    for _ in range(count):
        y += 1
        num += 1
        graph[x][y] = num


def down(count):
    global num, x, y
    for _ in range(count):
        x += 1
        num += 1
        graph[x][y] = num


def left(count):
    global num, x, y
    for _ in range(count):
        y -= 1
        num += 1
        graph[x][y] = num


for i in range(count):
    graph[x][y] = num

    up(1)
    right(1 + (i * 2))
    down(1 + (i * 2) + 1)
    left(1 + (i * 2) + 1)
    up(1 + (i * 2) + 1)


target_r, target_c = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == target:
            target_r = i + 1
            target_c = j + 1
        print(graph[i][j], end=" ")
    print()

print(target_r, target_c)
