# 2022-01-19
# 이코테 ch16 다이나믹 프로그래밍 Q33. 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())

# 앞에서부터 접근을 해야 한다는 고정관념에 사로 잡혀서 너무 오래걸렸던 문제였다

t = []  # 각 상담을 완료했을 때 걸리는 기간
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화

max_value = 0

for _ in range(m):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 매 상담에 대해 => 현재 상담 알자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤
        # 점화식에 맞게 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 일자를 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
