# 2023-06-15
# 프로그래머스 lv2 - 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# 소요 시간 : 15:20 ~ 16:20 (60m)

def solution(msg):
    answer = []
    mydict = {chr(i + 64): i for i in range(1, 27)}
    w = ""
    c = ""
    i = 0

    while i < len(msg):
        w = msg[i]
        while mydict.get(w, 0) != 0:
            if i < len(msg) - 1:
                c = msg[i + 1]
            else:
                c = ""
            if mydict.get(w + c, 0) == 0:
                mydict[w + c] = len(mydict) + 1
                answer.append(mydict[w])
                i += 1
                break
            elif mydict.get(w + c, 0) != 0:
                i += 1
                w = w + c
                if i>= len(msg):
                    answer.append(mydict[w])
                    break

    return answer


solution("KAKAO")
