# 2022-10-12
# week2 - 자료구조. 스택 수열
# https://www.acmicpc.net/problem/1874
# 소요시간 : 16:25 ~ 17:35 (70m, 시간초과), 집가서 추가로 더 보기 (m)
import sys

input = sys.stdin.readline

N = int(input())
DATA = [int(input()) for _ in range(N)]

nums = []
answer = []

isPopped = [False] * (N)


def calcul():
    for num in DATA:
        # 스택 안에 수가 없다면
        if num not in nums:
            ### 여기부터
            if len(nums) == 0:
                for i in range(1, num + 1):
                    nums.append(i)
                    answer.append("+")
            else:
                for i in range(nums[-1], num + 1):
                    if i not in nums and isPopped[i - 1] == False:
                        nums.append(i)
                        answer.append("+")
            ### 여기까지 for문 수 줄여야함
            nums.pop()
            isPopped[i - 1] = True
            answer.append("-")
        # 스택 안에 수가 있다면
        else:
            top = nums[-1]
            if isPopped[top - 1]:
                return []
            else:
                if top == num:
                    nums.pop()
                    isPopped[top - 1] = True
                    answer.append("-")
                else:
                    return []
    return answer


result = calcul()
if len(result) == 0:
    print("NO")
else:
    for i in result:
        print(i)
