# 2022-1-15
# 이코테 ch6 정렬 실전 문제 2 위에서 아래로

n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
array.reverse()

# array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")
