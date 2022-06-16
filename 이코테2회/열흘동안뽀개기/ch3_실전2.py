# 2022-06-16
# 이코테 열흘동안 뽀개기 프로젝트 1일차
# 그리디 실전 문제 2 큰 수의 법칙
# 소요 시간 : 10분

n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort(reverse=True)  # 내림차순 정렬

k_cnt = 0
m_cnt = 0
answer = 0

while m_cnt < m:
    if k_cnt < k:
        answer += num_list[0]
        m_cnt += 1
        k_cnt += 1
    else:
        k_cnt = 0
        answer += num_list[1]
        m_cnt += 1

print(answer)
