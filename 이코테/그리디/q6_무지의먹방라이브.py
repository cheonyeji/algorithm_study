# 2021-01-31
# 이코테 ch11 그리디 문제 Q6 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891

# 해설 참고
# 시간이 적게 걸리는 음식부터 확인하는 Greedy 접근 방식으로 해결
# 모든 음식을 시간 기준으로 정렬한 뒤 시간이 적게 걸리는 음식부터 제거
# 우선순위 큐 사용

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        # 음식 시간, 음식 번호 형태로 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # 일단 가장 적게 걸리는 음식을 다 먹는다고 가정하고 빼보는데, 만약 가장 적게 먹는 음식도 다 못먹고
    # 시간이 끝날 수 있으니까 조건문 걸어두기

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 뽑아낸 음식 다 먹는 시간 (적게 걸리는 것부터 먼저 나옴)
        sum_value += (
            now - previous
        ) * length  # now - previous : 만약 이미 다 먹은 음식이 있으면 그 시간은 빼주기
        length -= 1  # 다 먹은 음식은 빼기
        previous = now  # 이전 음식 시간 재설정 (이전 음식을 먹을 때도 현재 음식을 먹기 때문)

    # 남은 음식 중에서 몇번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])  # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


print(solution([8, 6, 4], 15))


# 정확도는 전부 통과하고... 효율성 2번 빼고 다 통과못한... 코드 ㅠ
"""
def solution(food_times, k):
    answer = 0
    food_round = k // len(food_times)
    result = k % len(food_times)

    eaten_food_times = []

    overflow = []
    for i in range(len(food_times)):
        if i < result:
            value = food_times[i] - food_round - 1
        else:
            value = food_times[i] - food_round

        if value < 0:
            overflow.append([value, i])
        eaten_food_times.append(value)

    # 다음칸이 실행됬어야하는 경우
    for j in overflow:
        count = 0
        case = 0
        while count < -j[0]:
            if eaten_food_times[result] > 0:
                eaten_food_times[result] -= 1
                count += 1
                result = (result + 1) % len(food_times)
            else:
                # 음식 다 소비할 때까지 방송사고가 안 난 것
                if case > len(food_times)*2:
                    return -1
                case += 1
                result = (result + 1) % len(food_times)
                continue
        eaten_food_times[j[1]] = 0

    result %= len(food_times)

    # 만약 더 섭취해야 할 음식이 없다면 -1 반환
    cnt = 0
    # 만약 먹방시작시에 먹어야하는 음식번째에 음식이 없다면 증가
    while eaten_food_times[result] <= 0:
        if cnt == len(food_times):
            return -1
        result = (result + 1) % len(food_times)
        cnt += 1

    answer = result + 1

    return answer

"""
