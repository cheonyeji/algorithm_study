# 2022-10-11
# week2 - 자료구조. 후위 표기식2
# https://www.acmicpc.net/problem/1935
# 소요시간 : 14:00 ~ 16:00 (100m, 해설참고)

import sys

input = sys.stdin.readline

n = int(input())
data = input()
data = data.replace("\n", "")
nums = [int(input()) for _ in range(n)]

# nums인덱스 <- ord() - 65

tmp = []

num_list = []
for s in data:
    # 숫자
    if 65 <= ord(s) <= 90:
        num_list.append(nums[ord(s) - ord("A")])
    # 연산자
    else:
        back = num_list.pop()
        front = num_list.pop()
        if s == "+":
            num_list.append(front + back)
        elif s == "-":
            num_list.append(front - back)
        elif s == "*":
            num_list.append(front * back)
        else:
            num_list.append(front / back)


# 소숫점 두번째 자리까지 표기
print("{:.2f}".format(num_list[0]))
