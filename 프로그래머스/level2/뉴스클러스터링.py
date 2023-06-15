# 2023-06-14
# 프로그래머스 lv2 - 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 소요 시간 : 18:52 ~ 19:11 (20m)


def makeArr(inputStr):
    arr = []
    for i in range(len(inputStr) - 1):
        if inputStr[i].isalpha() == True and inputStr[i + 1].isalpha() == True:
            arr.append(inputStr[i] + inputStr[i + 1])
    return arr


def solution(str1, str2):
    answer = 0
    # 대소문자 차이 무시를 위해 모두 소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()

    str1Arr = makeArr(str1)
    str2Arr = makeArr(str2)

    print(str1Arr)
    print(str2Arr)

    union = []
    intersect = []

    for s in str1Arr:
        if s in str2Arr:
            intersect.append(s)
            str2Arr.remove(s)
        else:
            union.append(s)

    union = union + str2Arr + intersect

    if len(union) == 0:
        return 65536
    else:
        answer = int((len(intersect) / len(union)) * 65536)
        return answer
