# 2022-06-16
# 이코테 열흘동안 뽀개기 프로젝트 1일차
# 그리디 예제 3-1

"""
500, 100, 50, 10원짜리 동전이 무한히 존재한다. 
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하여라.
"""

n = int(input())
money_list = [500, 100, 50, 10]
answer = 0

# 시간 복잡도 : O(화폐종류 K)
for money in money_list:
    answer += n // money
    n %= money

print(answer)
