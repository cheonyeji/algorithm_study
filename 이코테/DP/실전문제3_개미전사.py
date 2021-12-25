n = int(input())

food = list(map(int, input().split()))

d = [0] * 101
d[0] = food[0]
d[1] = max(d[0], food[1])

for i in range(2, n):
    # 바로 전 창고를 터는 경우, 현재 창고와 전전 창고를 터는 경우 중 더 큰 값 저장
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(max(d))
