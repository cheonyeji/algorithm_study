# # 2021-01-26
# 이코테 ch12 구현 문제 Q9 문자열 압축
# https://programmers.co.kr/learn/courses/5/lessons/60057

INF = int(1e9)


def cut_str(s, num):
    i = 0
    length = len(s)
    result = ""
    while i < length:
        str1 = s[i : i + num]
        count = 1
        for j in range(i + num, length, num):
            if str1 == s[j : j + num]:
                count += 1
            else:
                break

        # 입출력예시 5번에서 제일 앞에서부터 정해진 길이만큼 잘라야한다고 나와있으므로 이 부분은 X
        # if count == 1:
        #     result += s[i]
        #     i += 1
        if count == 1:
            result += str1
        else:
            result += str(count) + str1
        i += num * count

    return len(result)


def solution(s):
    result = [INF] * (len(s) + 1)

    # 문자열 길이가 1일때 for문을 안 돌아서 예외처리
    if len(s) == 1:
        result[1] = 1

    for i in range(1, len(s)) // 2 + 1:  # N/2까지의 모든 수만 살펴보면 됨
        result[i] = cut_str(s, i)

    return min(result)


"""
TC  result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
"""
