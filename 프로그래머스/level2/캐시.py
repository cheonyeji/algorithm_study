# 2023-06-14
# 프로그래머스 lv2 - 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 소요 시간 : 18:41 ~ 18:51 (10m)

from collections import deque


def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    c = deque([])
    for city in cities:
        city = city.lower()
        # miss
        if not city in c and len(c) < cacheSize:
            # 최초 삽입
            answer += 5
            c.append(city)
        elif not city in c:
            # 교체
            answer += 5
            c.popleft()
            c.append(city)
        # hit
        else:
            answer += 1
            c.remove(city)
            c.append(city)

    return answer
