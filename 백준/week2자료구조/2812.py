# 2022-10-17
# week2 - 자료구조. 크게 만들기
# https://www.acmicpc.net/problem/2812
# 소요시간 : 10:40 ~ 12:00, 14:30 ~ 14:48 (100m, 못 풀어서 해설 참고)

"""
너무 어렵게 생각했던 문제
가장 큰 숫자를 앞에 위치하게 하려면 입력받은 숫자를 하나씩 stack에 넣고
다음 숫자와 비교해주면 된다
만약 다음 숫자가 stack에 있는 숫자보다 크면, stack.pop()해주면서
가장 큰 숫자를 앞에 위치하게 한다

K개 숫자까지만 지워야 하므로 K>0 조건이 필요하며
만약 K개보다 덜 지운 경우 뒤에서부터 남은 K개를 빼고 출력해주면 된다.

인덱스를 하나하나 따져가면서 해줄 필요 없이 stack 자료구조를 사용하면
쉽게 풀리는 문제였다..
"""


import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))
str_num = input()[:-1]  # \n 제거

stack = []

for num in str_num:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    print("".join(stack[:-K]))
else:
    print("".join(stack))
