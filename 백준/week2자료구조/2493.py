# 2022-10-13, 10-14
# week2 - 자료구조. 탑
# https://www.acmicpc.net/problem/2493
# 소요시간 : 15:44 ~ 17:19 (75m, 틀림), 14:40 ~ 15:03 (25m, 솔!)

import sys

input = sys.stdin.readline

N = int(input())
Heights = list(map(int, input().split(" ")))

# 맨 앞 탑은 수신 불가능하므로 미리 저장하고 고려X
answer = [0]
available_tower = [(Heights[0], 1)]  # (높이, 탑번호)

for i in range(1, len(Heights)):
    now_h, now_i = Heights[i], i + 1

    received = False
    while len(available_tower) > 0:
        prev_h, prev_i = available_tower.pop()
        # 수신 가능한 탑 발견
        if prev_h > now_h:
            available_tower.append((prev_h, prev_i))
            answer.append(prev_i)
            available_tower.append((now_h, now_i))
            received = True
            break
        # 수신 가능한 탑 발견
        # 높이가 같은 경우 최신 탑이 더 우선이므로 최신 탑 데이터만 저장
        elif prev_h == now_h:
            answer.append(prev_i)
            available_tower.append((now_h, now_i))
            received = True
            break
        else:
            continue
    # 모든 탑이 다 수신 불가능한 경우
    if received == False:
        available_tower.append((now_h, now_i))
        answer.append(0)

print(" ".join(map(str, answer)))
