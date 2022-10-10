# 2022-10-10
# week1 - 수학. 골드바흐 파티션
# https://www.acmicpc.net/problem/17103
# 소요시간 : 14:54~ 15:32 (40m)


def getPrimes(MAXCASE):
    erato = [True] * (MAXCASE + 1)
    erato[0], erato[1] = False, False

    for i in range(2, int(MAXCASE ** 0.5) + 1):
        if erato[i] == True:
            for j in range(i + i, MAXCASE + 1, i):
                erato[j] = False
    return erato


erato = getPrimes(1000001)
t = int(input())

for _ in range(t):
    num = int(input())
    cnt = 0
    for i in range(2, num // 2 + 1):
        if erato[i] and erato[num - i]:
            cnt += 1
    print(cnt)
