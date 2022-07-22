# 2022-07-22
# 프로그래머스 Lv2 - 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584


# 효울성0점코드
def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in prices[i + 1 :]:
            if j < prices[i]:
                cnt += 1
                break
            else:
                cnt += 1

        answer.append(cnt)
    return answer
