n, m = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수 찾기
# 금액 i를 만들 수 있는 최소한의 화폐개수를 a(i), 화폐단위를 k라고 할 때, 점화식은 다음과 같다.
# 1. a(i-k)를 만드는 방법이 존재하는 경우 : a(i) = min(a(i), a(i-k)+1)
# 2. 없는 경우 : a(i)= 10001

# 계산 결과 저장 배열
d = [10001] * (m + 1)  # 10001 : 계산 불가

d[0] = 0

for i in range(n):
    for j in range(coins[i], m + 1):
        d[j] = min(d[j], d[j - coins[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
