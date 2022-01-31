# 2021-01-31
# 이코테 ch11 그리디 문제 Q1 모험가 길드

n = int(input())
data = list(map(int, input().split()))

data.sort()

# 그룹 수의 최댓값을 구하기
# 앞에서부터 컷해야함

fear = 0
count = 0
party = 0
for i in range(len(data)):
    fear = max(data[i], fear)
    count += 1
    if fear <= count:
        party += 1
        count = 0

print(party)

"""
TC 1 -> 2
5 
2 3 1 2 2
"""
