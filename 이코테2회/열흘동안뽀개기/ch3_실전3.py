# 2022-06-16
# 이코테 열흘동안 뽀개기 프로젝트 1일차
# 그리디 실전 문제 3 숫자 카드 게임
# 소요 시간 : 20분

n, m = map(int, input().split())

min_val = -1
for i in range(n):
    data = list(map(int, input().split()))
    min_val = max(min_val, min(data))

print(min_val)
