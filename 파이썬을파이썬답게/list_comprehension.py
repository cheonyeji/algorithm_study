# for 문과 if문을 한번에
def solution(mylist):
    # 일반적인 방식
    # answer = []
    # for i in mylist:
    #     if i % 2 == 0:
    #         answer.append(i ** 2)

    # 파이썬을 파이썬답게
    answer = [num ** 2 for num in mylist if num % 2 == 0]
    return answer


print(solution([3, 4, 5, 6]))
