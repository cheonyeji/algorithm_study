# 모든 멤버의 type 변환하기
def solution(mylist):
    # 일반적인 방법
    # answer = []
    # for i in mylist:
    #     answer.append(int(i))

    # 파이썬을 파이썬답게
    answer = list(map(int, mylist))
    return answer
