# 2023-09-27 (소요시간 : 25m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버2. https://www.acmicpc.net/problem/20006


"""
구현 + 시뮬레이션.
문제에 나온 그대로 풀면 OK
"""

from sys import stdin

input = stdin.readline

p, m = map(int, input().split(" "))

input_ = []
for _ in range(p):
    input_.append(list(input().rstrip().split(" ")))

room = []
for lv, id_ in input_:
    lv = int(lv)
    make_room = True
    if len(room) == 0:
        room.append((lv, [[lv, id_]]))
        continue

    # 방 돌면서 매칭가능방 체크
    for room_lv, room_arr in room:
        if -10 + room_lv <= lv <= 10 + room_lv and len(room_arr) < m:
            room_arr.append([lv, id_])
            make_room = False
            break

    # 방 다 돌았는데 매칭 방X
    if make_room:
        room.append((lv, [[lv, id_]]))

for room_lv, room_arr in room:
    if len(room_arr) == m:
        print("Started!")
        room_arr.sort(key=lambda x: x[1])
        for LV, ID in room_arr:
            print(LV, ID)
    else:
        print("Waiting!")
        room_arr.sort(key=lambda x: x[1])
        for LV, ID in room_arr:
            print(LV, ID)
