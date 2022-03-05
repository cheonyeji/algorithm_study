# 2022-03-06
# 이코테 2회차 그리디 Q1 모험가 길드

# 적은 인원이 필요한 경우부터 매칭해줘야 최대 그룹 수가 가능

n = int(input())
people = list(map(int, input().split()))

people.sort()

answer = 0

party = []
for i in range(len(people)):
    party.append(people[i])

    if max(party) > len(party):
        continue
    
    answer += 1
    party = []
    

print(answer)
    

''' 
TC 1 -> 2 
5
2 3 1 2 2
'''
