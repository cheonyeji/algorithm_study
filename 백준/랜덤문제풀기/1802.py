# 2023-09-30
from sys import stdin

input = stdin.readline

T = int(input())

data = [input().rstrip() for _ in range(T)]


answer = []


def solution(string):
    mid = len(string) // 2
    left = mid - 1
    right = mid + 1

    while left >= 0 and right <= len(string):
        if string[left] != string[right]:
            left -= 1
            right += 1
        else:
            return "NO"
    return "YES"


for string in data:
    answer.append(solution(string))

for a in answer:
    print(a)
