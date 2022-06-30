# 2022-06-30
# 프로그래머스 lv1 - 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
# 소요 시간 : 16:48 ~ 17:00 (12m)

def studentOne(answers):
    count = 0
    for i in range(1, len(answers)+1):
        if i%5 == 0 and answers[i-1] == 5:
            count += 1
        elif i%5 == answers[i-1]:
            count += 1
    return count

def studentTwo(answers):
    arr = [2, 1, 2, 3, 2, 4, 2, 5]
    count = 0
    for i in range(1, len(answers)+1):
        if i%8 == 0 and arr[7] == answers[i-1]:
            count += 1
        elif arr[(i%8)-1] == answers[i-1]:
            count += 1
    
    return count

def studentThree(answers):
    arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = 0
    for i in range(1, len(answers)+1):
        if i%10 == 0 and arr[9] == answers[i-1]:
            count += 1
        elif arr[(i%10)-1] == answers[i-1]:
            count += 1
    
    return count

def solution(answers):
    answer = []
    result = []
    result.append(studentOne(answers))
    result.append(studentTwo(answers))
    result.append(studentThree(answers))
    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i+1)
    
    return answer