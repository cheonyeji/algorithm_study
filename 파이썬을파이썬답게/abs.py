# i번째 원소와 i+1번째 원소
def solution(mylist):
    answer = []
    # 일반적인 방법
    # for i in range(len(mylist)):
    #     if i + 1 == len(mylist):
    #         break
    #     answer.append(abs(mylist[i] - mylist[i + 1]))

    # 파이썬을 파이썬답게
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


print(solution([83, 48, 13, 4, 71, 11]))
