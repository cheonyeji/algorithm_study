# 2022-06-24
# 이코테 열흘동안 뽀개기 2일차
# 구현 예제 2 시각
# 소요 시간 : 15분

N = int(input())
cnt = 0

# 00시 00분 00초 ~ N시 59분 59초
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            # 문자열 안에 들어있는지 체크
            if "3" in str(s) + str(m) + str(h):
                cnt += 1

print(cnt)
