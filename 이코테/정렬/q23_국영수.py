# 2022-01-15
# 이코테 ch14 정렬 문제 Q23 국영수
# https://www.acmicpc.net/problem/10825

n = int(input())

data = []

for _ in range(n):
    name, lang, eng, math = input().split()  # 국, 영, 수 순서로 입력
    lang = int(lang)
    eng = int(eng)
    math = int(math)
    data.append((name, lang, eng, math))

# +:오름차순, -: 내림차순
# 정렬 람다식의 경우 입력된 인자대로 정렬을 수행
data = sorted(data, key=lambda data: (-data[1], data[2], -data[3], data[0]))

for i in data:
    print(i[0])

"""
TC
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""
