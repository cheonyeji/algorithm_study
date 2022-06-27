# 2022-06-27
# 프로그래머스 고득점 kit - 정렬 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 소요 시간 : 14:25 ~ 15:15 (시간초과 못잡아서 타 코드 참고)


# 시간 초과 코드
"""
def solution(numbers):
    answer = ''
    
    
    while len(numbers) > 0:
        max_num = -1
        for i in range(len(numbers)):
            if str(max_num)*3 < str(numbers[i])*3:
                max_num = numbers[i]
        
        numbers.remove(max_num)
        answer += str(max_num)
            
    
    
    
    return str(int(answer))
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))
