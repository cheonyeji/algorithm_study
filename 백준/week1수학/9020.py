# 2022-10-08
# week1 - 수학. 골드바흐의 추측
# https://www.acmicpc.net/problem/9020
# 소요시간 : 16:06 ~ : (m)

import math


def getPrimeNums(n):
    erato = [True] * (n)
    erato[0], erato[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if erato[i] == True:
            for j in range(i + i, n, i):
                erato[j] = False

    return [i for i in range(n) if erato[i] == True]


def getGoldP(target, nums):
    tmp = 0
    for i in range(len(nums)):
        if nums[i] > int(target / 2):
            break
        tmp = i

    for i in range(tmp, -1, -1):
        for j in range(tmp, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            if nums[i] + nums[j] > target:
                break


t = int(input())
for i in range(t):
    num = int(input())
    result = getGoldP(num, getPrimeNums(num + 1))
    print(result[0], result[1])
