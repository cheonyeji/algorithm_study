# 2022-01-18
# 이코테 ch15 이진 탐색 문제 Q29 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

# 해당 거리를 유지하며 공유기를 몇대까지 설치 가능한지
def router_setting(dist):
    count = 1
    cur_house = house[0]  # 시작점 (공유기 설치)
    for i in range(1, n):  # 집 모두를 순회
        # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
        if cur_house + dist <= house[i]:
            count += 1  # 공유기 설치
            cur_house = house[i]  # 공유기 설치된 집 갱신

    return count


start = 1
end = house[-1] - house[0]  #
answer = 0

while start <= end:
    mid = (start + end) // 2
    if router_setting(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
