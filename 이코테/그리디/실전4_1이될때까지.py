# 2021-01-30
# 이코테 ch3 그리디 실전 문제 4 1이 될 때까지

n, k = map(int, input().split())

count = 0

while n > 1:
    if n % k == 0:
        n //= k  # // 써야 int형으로 반환
    else:
        n -= 1
    count += 1

print(count)

# n의 범위가 100억 이상의 큰 수가 되어도 작동하려면
# n이 k의 배수가 되도록 효율적으로 한번에 뺴는 방식으로 소스코드 작성
result = 0
while True:
    # n이 k로 나누어떨어지는 수가 될때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # n이 k보다 작을 때(더이상 나눌수X) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n - 1
