# 2022-10-12, 2022-10-13
# week2 - 자료구조. 스택 수열
# https://www.acmicpc.net/problem/1874
# 소요시간 : 16:25 ~ 17:35 (70m, 시간초과), 12:47 ~ 14:00 (70m, 해설 진짜 조금 참고)
import sys

input = sys.stdin.readline

N = int(input())
DATA = [int(input()) for _ in range(N)]

count = 0
answer = []
nums = []
for num in DATA:
    while count < num:
        answer.append("+")
        count += 1
        nums.append(count)
    top = nums.pop()
    if top == num:
        answer.append("-")
    else:
        answer.clear()
        break

if len(answer) == 0:
    print("NO")
else:
    for i in answer:
        print(i)


"""
# 삽질 1. 왜 그리 꼬아 생각하는지..! 코드를 범용적으로 써야지
max_top = 0
answer = []
nums = []
for num in DATA:
    if len(nums) == 0:
        for i in range(max_top, num + 1):
            if i == 0:
                continue
            nums.append(i)
            answer.append("+")
        nums.pop()
        answer.append("-")
        max_top = num
    else:
        top = nums.pop()
        if top == num:
            answer.append("-")
        elif top < num:
            nums.append(top)
            for i in range(max_top + 1, num + 1):
                nums.append(i)
                answer.append("+")
            nums.pop()
            answer.append("-")
            max_top = num
        else:
            answer = []
            break

if len(answer) == 0:
    print("NO")
else:
    for i in answer:
        print(i)
"""

"""
# 삽질 2. 경우의 수를 나눌 필요가 없었다. count라는 변수를 선언하여 해결.
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
"""
