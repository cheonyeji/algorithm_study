# 2022-10-16
# week2 - 자료구조. AC
# https://www.acmicpc.net/problem/5430
# 소요시간 : 21:09 ~ 21:58 (50m)

"""
문제에서 시키는대로 순순히 reverse() 함수 실행하고 있다간 시간초과난다.
reverse 함수의 시간 복잡도는 O(N)이다. 남발해서는 X
따라서 reverse모드가 켜져있으면 맨 뒤에서 제거해주고
꺼져있으면 맨 앞에서 제거해주면 된다.
마지막으로 출력할 때도 reverse인지 아닌지 체크해서 출력해주면 OK
"""

from collections import deque
import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    P = input()
    N = int(input())
    data = input()

    if len(data) != 3:  # [] 인 경우 제외
        nums = list(map(int, data[1:-2].split(",")))
        q = deque(nums)
    else:
        q = deque()

    ERROR = False
    REVERSE = False
    for p in P:
        if p == "R":
            REVERSE = not REVERSE
        elif p == "D":
            if len(q) == 0:
                ERROR = True
                break
            else:
                if REVERSE:
                    q.pop()
                else:
                    q.popleft()
        else:
            continue
    if ERROR:
        print("error")
    else:
        if REVERSE:
            print("[" + ",".join(map(str, list(q)[::-1])) + "]")
        else:
            print("[" + ",".join(map(str, list(q))) + "]")
