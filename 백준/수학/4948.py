# 2022-10-07
# week1. 수학
# https://www.acmicpc.net/problem/4948
# 소요시간 : 18:34 ~ 19:01 (30m)

import math

# 에라토스테네스의 체 방식 사용
def cntPrimeNums(start, end):
    # 1~end까지
    erato = [True] * end

    # 1은 소수가 아니므로 체크
    erato[0] = False

    for i in range(2, int(math.sqrt(end)) + 1):
        if erato[i] == True:
            for i in range(i + i, end, i):
                erato[i] = False
    cnt = 0
    for i in range(start, end):
        if erato[i] == True:
            cnt += 1
    return cnt


n = -1
while True:
    n = int(input())
    if n == 0:
        break
    print(cntPrimeNums(n + 1, 2 * n + 1))
