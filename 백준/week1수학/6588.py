# 2022-10-08
# week1 - 수학. 골드바흐의 추측 (난이도 실버 1)
# https://www.acmicpc.net/problem/6588
# 소요시간 : 22:42 ~ 23:44 (60m)

erato = [True] * 1000001
erato[0], erato[1] = False, False
for i in range(2, 1001):
    if erato[i]:
        for j in range(i + i, 1000001, i):
            erato[j] = False

# n 미만의 수 중 홀수인 소수 리스트 리턴
def getPrimeNums(n):
    return [i for i in range(n) if erato[i] == True and i % 2 != 0]


def getGoldB(target, nums):
    middleIdx = -1
    for i in range(len(nums)):
        if nums[i] > int(target / 2):
            break
        middleIdx = i

    for i in range(middleIdx + 1):
        for j in range(len(nums) - 1, middleIdx, -1):
            if nums[i] + nums[j] < target:
                break
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return False


while True:
    n = int(input())
    wrongFlag = True
    if n == 0:
        break

    for i in range(3, n):
        if erato[i] == True:
            if erato[n - i] == True:
                wrongFlag = False
                print(n, "=", i, "+", n - i)
                break
    if wrongFlag:
        print("Goldbach's conjecture is wrong.")
