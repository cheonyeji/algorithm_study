# 2023-07-27 (소요시간 : 1h)

"""
Stack으로 풀이
주식 가격이 상승할때만 오름차순으로 stack에 넣어주기
stack에는 (가격, 순서)로 넣어주기
주식이 떨어지면 본인보다 큰 값은 다 쳐내기
"""


def solution(prices):
    answer = [0] * len(prices)
    increase = []
    for i in range(len(prices)):
        if len(increase) == 0:
            increase.append([prices[i], i])  # 가격, 순서
            continue
        if increase[-1][0] <= prices[i]:  # 주식가격 상승
            increase.append([prices[i], i])
        else:  # 가격 하락
            while len(increase) != 0 and increase[-1][0] > prices[i]:
                data = increase.pop()
                answer[data[1]] = i - data[1]
            increase.append([prices[i], i])

    while len(increase) != 0:
        data = increase.pop()
        # 끝까지 안 떨어진 것이므로 전체 길이에서 본인 index만큼 빼기
        answer[data[1]] = len(prices) - 1 - data[1]
    return answer


print(solution([1, 2, 3, 2, 3]))
