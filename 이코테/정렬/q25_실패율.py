# 2022-01-15, 소요시간 : 25분
# 이코테 ch14 정렬 문제 Q25 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

n = int(input())
stages = list(map(int, input().split(",")))

answer = []

stages.sort()
fail_rates = []

total = len(stages)
for i in range(1, n + 1):
    player = stages.count(i)
    if total == 0:
        fail_rates.append((0, i))
    else:
        fail_rates.append((player / total, i))
    total -= player

result = sorted(fail_rates, key=lambda data: (-data[0], data[1]))

for i in result:
    answer.append(i[1])

# answer = [i[1] for i in answer] # 24~25번 줄

print(answer)

"""
TC 1 -> [3,4,2,1,5]
5
2,1,2,6,2,4,3,3
TC 2 -> [4,1,2,3]
4
4,4,4,4
"""

"""
프로그래머스 제출 답
def solution(N, stages):
    answer = []
    
    stages.sort()
    fail_rates = []
    
    total = len(stages)
    for i in range(1, N+1):
        player = stages.count(i)
        if total == 0:
            fail_rates.append((0, i))
        else:
            fail_rates.append((player / total, i))
        total -= player
    
    result = sorted(fail_rates, key=lambda data: (-data[0], data[1]))
    for i in result:
        answer.append(i[1])
    return answer
"""
