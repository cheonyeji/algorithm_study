# 2022-03-06
# 이코테 2회차 그리디 Q3 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

# 연속된 0의 개수, 연속된 1의 개수 중 더 적은 숫자만큼 뒤집어야 최소한으로 뒤집는 것

data = input()

str0 = 0
str1 = 0

def count(val):
    global str1, str0
    if val == 0:
        str0 += 1
    else:
        str1 += 1

for i in range(len(data)-1):
    # 연속일떄
    if data[i] == data[i+1]:
        # 다음숫자가 마지막인 경우
        if (i+1) == len(data)-1:
            count(int(data[i]))
        continue
    # 불연속일때
    else:
        # 다음숫자가 마지막인경우
        if (i+1) == len(data)-1:
            # 마지막 숫자도 count
            count(int(data[i+1]))
        # 현재 숫자 count
        count(int(data[i]))


print(min(str1, str0))


    