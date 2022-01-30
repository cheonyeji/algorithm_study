# 2021-01-30
# 이코테 ch12 구현 문제 Q14 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

# weak, dist의 길이가 매우 작다 -> 완탐 의심
from itertools import permutations


def solution(n, weak, dist):
    answer = 0
    length = len(weak)
    # 길이를 2배로 늘려서 원형->일자로 변경
    for i in range(length):
        weak.append(weak[i] + n)

    # 투입할 친구 수의 최솟값을 찾아야 하므로 가장 맥시멈 값으로 초기화
    answer = len(dist) + 1

    for start in range(length):
        # 친구들의 거리를 나열해놓은 순열에 대하여 모든 경우 훑어보기
        cases = list(permutations(dist, len(dist)))
        for frineds in cases:
            count = 1  # 투입할 친구 수
            # 해당 친구가 점검할 수 있는 마지막 위치 값 저장
            position = weak[start] + frineds[count - 1]
            # 모든 취약점을 돌면서 체크
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 넘어서는 값이 등장하는 경우
                if position < weak[index]:
                    # 새로운 친구 투입
                    count += 1
                    # 만ㄴ약 투입 불가능하면 종료
                    if count > len(dist):
                        break
                    # 해당 친구로 position 업데이트
                    position = weak[index] + frineds[count - 1]
            answer = min(answer, count)

    # 만약 투입 수가 최대 친구 수보다 더 많으면 불가능한 시나리오이므로 -1 리턴
    if answer > len(dist):
        return -1
    return answer


"""
12,[1, 5, 6, 10],[1, 2, 3, 4]
"""
