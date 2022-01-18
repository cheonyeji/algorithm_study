# 2022-01-18
# 이코테 ch8 다이나믹 프로그래밍 실전 문제 3 개미 전사

# 작은 것부터 차근차근 (앞에서부터 차근차근)

n = int(input())
food = list(map(int, input().split()))  # 0번 칸부터 음식이 있음

d = [0] * 101

d[0] = food[0]  # 첫번째 식량창고 스틸
d[1] = max(food[0], food[1])  # 첫번째 칸, 두번째 칸 중 더 큰 값 획득!
# d[2] = max(food[2] + food[0], food[1])
# d[i] = max(food[i] + d[i-2], d[i-1]) # 점화식 도출 가능!!!
for i in range(2, n):
    d[i] = max(d[i - 2] + food[i], d[i - 1])

print(d[n - 1])

"""
TC -> 8
4
1 3 1 5
"""
