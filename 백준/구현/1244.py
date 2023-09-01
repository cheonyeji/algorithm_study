# 2023-09-01 (소요시간 : 30m)
# 구현 [실버4. 백준 1244 스위치 켜고 끄기] (https://www.acmicpc.net/problem/1244)

from sys import stdin

input = stdin.readline

N = int(input())
switches = [-1]
switches += list(map(int, input().split(" ")))

students = int(input())


def male(idx):
    for i in range(idx, N + 1, idx):
        if switches[i] == 0:
            switches[i] = 1
        else:
            switches[i] = 0


def female(idx):
    before = idx - 1
    after = idx + 1
    is_symmetry_exist = False
    while True:
        if 1 <= before < idx and idx < after <= N:
            if switches[before] == switches[after]:
                is_symmetry_exist = True
                before -= 1
                after += 1
            else:
                before += 1
                after -= 1
                break
        else:
            before += 1
            after -= 1
            break

    if not is_symmetry_exist:
        if switches[idx] == 0:
            switches[idx] = 1
        else:
            switches[idx] = 0
    else:
        for i in range(before, after + 1):
            if switches[i] == 0:
                switches[i] = 1
            else:
                switches[i] = 0


for _ in range(students):
    gender, idx = map(int, input().split(" "))
    if gender == 1:
        male(idx)
    else:
        female(idx)


for i in range(1, N + 1):
    if i % 20 == 1 and i != 1:
        print()
    print(switches[i], end=" ")
