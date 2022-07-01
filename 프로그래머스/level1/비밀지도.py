# 2022-07-01
# 프로그래머스 lv1 - 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 소요 시간 : 23:30 ~ 00:00 (30m)

# 진법(base)를 입력받아 변환해주는 코드~
def convert(num, base):
    result = ""
    while num > 0:
        num, mod = divmod(num, base)
        result += str(mod)

    return result[::-1]


def convert10to2(num, n):
    map_data = ""
    while True:
        map_data += str(num % 2)
        num = num // 2
        if (num // 2) == 0:
            map_data += str(num % 2)
            break

    if len(map_data) != n:
        return "0" * (n - len(map_data)) + map_data[::-1]
    else:
        return map_data[::-1]


def solution(n, arr1, arr2):
    answer = []
    map1 = []
    for a in arr1:
        map1.append(convert10to2(a, n))

    map2 = []
    for b in arr2:
        map2.append(convert10to2(b, n))

    for i in range(len(map1)):
        # map1[i]는 문자열
        result = ""
        for j in range(len(map1[i])):
            # map1[i][j]는 문자
            if map1[i][j] == "0" and map2[i][j] == "0":
                result += " "
            else:
                result += "#"
        answer.append(result)
    return answer
