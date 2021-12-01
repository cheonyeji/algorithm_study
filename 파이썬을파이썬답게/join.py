# sequence 멤버를 하나로 이어붙이기
def solution(mylist):
    # 일반적인 방법
    # answer = ''
    # for i in mylist:
    #     answer += i

    # 파이썬을 파이썬답게
    answer = "".join(mylist)

    # join : 시퀀스의 멤버들을 하나의 string으로 이어붙여야 할 때 사용
    return answer
