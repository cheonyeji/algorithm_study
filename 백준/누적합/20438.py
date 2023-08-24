# 2023-08-24 (소요시간 : 50m)
# 누적합 https://www.acmicpc.net/problem/20438

"""
매번 범위 안에 몇개의 1이 있는지 세다간 시간초과가 나는 문제
누적합을 사용하여 해당 범위 안에 몇명의 학생이 미출석상태인지를 계산해주는 누적합 방식을 사용해야 한다.
미출석 상태를 1로 처리, 출석 상태를 0으로 처리하여 1의 개수가 미출석된 학생의 수다.
"""


from sys import stdin

input = stdin.readline

# 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M
N, K, Q, M = map(int, input().split(" "))

# 졸고 있는 학생 번호
sleeping = list(map(int, input().split(" ")))

# 출석 코드를 받을 학생 번호
attend = list(map(int, input().split(" ")))

# 계산해야줘야 하는 구간 M개 받기
check = []
for _ in range(M):
    check.append(list(map(int, input().split(" "))))

arr = [1 for _ in range(N + 3)]  # 3 ~ N+2번째까지 사용, 1은 미출석


for a in attend:
    if a in sleeping:
        continue
    # 더 작은 배수를 훑어본 상태이므로 계산해줄 필요X
    if arr[a] == 0:
        continue
    # 출석 처리
    for i in range(a, N + 3, a):
        arr[i] = 0

# 조는 학생은 졸았으므로 미출석 처리
for s in sleeping:
    arr[s] = 1

# 누적합 계산
acc = [0 for _ in range(N + 3)]
for i in range(N + 3):
    if i == 0:
        acc[i] = arr[i]
    else:
        acc[i] = arr[i] + acc[i - 1]


for s, e in check:
    print(acc[e] - acc[s - 1])

"""
TC : 5
5 1 1 1
3
3
3 7

TC : 12 \n 13
50 4 5 2
24 15 27 43
3 4 6 20 25
3 25
26 52
"""
