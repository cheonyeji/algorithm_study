def solution(mylist):
    answer = []
    for i in mylist:
        for idx, val in enumerate(i):
            answer.append(val)
    return answer


print(solution([["A", "B"], ["X", "Y"], ["1"]]))
