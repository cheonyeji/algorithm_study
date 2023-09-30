# 2023-09-30
# 백준 트럭 https://www.acmicpc.net/problem/13335
from sys import stdin
from collections import deque

input = stdin.readline

N, W, L = map(int, input().split(" "))
data = deque(list(map(int, input().split(" "))))

bridge = deque([])

b_total = 0
time = 0

while len(data) != 0 or len(bridge) != 0:
    time += 1
    # 다리 위의 트럭 전부 1씩 이동
    if len(bridge) != 0:
        for i in range(len(bridge)):
            bridge[i][1] += 1
        # 다리를 빠져나갈 수 있는 트럭이 있다면
        while len(bridge) > 0 and bridge[0][1] > W:
            pop_w, pop_t = bridge.popleft()
            b_total -= pop_w

    # 진입가능한 트럭 1대만 다리 위로
    if len(data) > 0 and b_total + data[0] <= L:
        # 대기열에서 뽑아서 다리위로
        t_weight = data.popleft()
        b_total += t_weight
        bridge.append([t_weight, 1])

print(time)
