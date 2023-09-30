# 2023-09-30
# 백준 문자열폭발 https://www.acmicpc.net/problem/9935
# 스택

from sys import stdin

input = stdin.readline

input_s = input().rstrip()
bomb = input().rstrip()

stack = []

for s in input_s:
    if len(stack) >= len(bomb):
        if "".join(stack[len(stack) - len(bomb) :]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
    stack.append(s)

# 마지막 원소 넣은 후에는 반복문에서 체크 못해주니까 한번더
if len(stack) >= len(bomb):
    if "".join(stack[len(stack) - len(bomb) :]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
