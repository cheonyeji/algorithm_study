# 2022-10-07
# 백준 기본 입출력 문제
# https://www.acmicpc.net/problem/1924
# 소요 시간 : 14:00 ~ 14:17 (17m)

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())

dates = 0
for i in range(x):
    dates += month[i]

dates += y - 1

print(day[dates % 7])
