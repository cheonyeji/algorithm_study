# 2021-01-31
# 이코테 ch11 그리디 문제 Q3 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

str = input()

start = 0
arr_0 = []
arr_1 = []

for i in range(1, len(str) + 1):
    # 01010 입력의 경우 마지막 인덱스가 입력되지 않아 추가
    if i == len(str):
        if str[start] == "0":
            arr_0.append([start, i - 1])
        else:
            arr_1.append([start, i - 1])

    elif str[start] == str[i]:
        continue
    else:
        if str[start] == "0":
            arr_0.append([start, i - 1])
        else:
            arr_1.append([start, i - 1])
        start = i

print(min(len(arr_0), len(arr_1)))
