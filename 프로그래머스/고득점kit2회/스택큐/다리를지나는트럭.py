# 2023-07-27 (소요시간 : 1h 30m)

"""
문제에 설명이 부족하여 헤맸음
트럭이 다리를 통과하려면 bridge_length만큼 지나가야함!
따라서 트럭이 얼마만큼 통과하였는지를 세어서 차례차례 지나가야함
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([])  # 다리에 올라간 트럭 무게
    trucks = deque(truck_weights)
    bridge_count = deque([])
    time = 0

    while True:
        time += 1
        if len(bridge) != 0:  # 1초가 지났으니 다리에 올라간 트럭들이 이동
            for i in range(len(bridge)):
                bridge_count[i] += 1

        # 나갈 트럭은 나가기
        while len(bridge) != 0 and bridge_count[0] > bridge_length:
            bridge.popleft()
            bridge_count.popleft()
        if (
            len(trucks) != 0
            and trucks[0] + sum(bridge) <= weight
            and len(bridge) + 1 <= bridge_length
        ):
            bridge.append(trucks[0])
            bridge_count.append(1)
            trucks.popleft()

        if len(trucks) == 0 and len(bridge) == 0:
            break
    return time


print(solution(2, 10, [7, 4, 5, 6]))
