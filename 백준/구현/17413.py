# 2023-08-23 (소요시간 : 18m)
# 구현 https://www.acmicpc.net/problem/17413


"""
문제에 주어진 조건대로 구현하면 되는 문제
체크할 부분
현재 살펴보는 문자(s)가
1) "<"인 경우 tag True표시, 그대로 문자(s) 입력
2) ">"인 경우 tag False표시, 그대로 문자(s) 입력
3) " "인 경우
    3-1) tag True인 경우, 그대로 문자(s) 입력
    3-2) tag False인 경우, 지금까지의 문자(tmp) 뒤집어서 입력, 그대로 문자(s) 입력
4) 그 외의 경우
    4-1) tag True인 경우, 그대로 문자(s) 입력
    4-2) tag False인 경우, 뒤집기 위한 임시문자열(tmp)에 입력

* 끝까지 살펴보았고 뒤집어줘야할 문자가 존재하는 경우 result에 마지막으로 뒤집어서 넣어주기
* 사용자가 입력한 엔터를 삭제하기 위해 input().rstrip() 사용
"""

from sys import stdin

input = stdin.readline

S = input().rstrip()

result = ""
tmp = ""
tag = False

for i, s in enumerate(S):
    if s == "<":
        if tmp != "":
            result += tmp[::-1]
        tmp = ""
        tag = True
        result += s
    elif tag and s != ">":
        result += s
    elif s == ">":
        tag = False
        result += s
    elif s == " " and tag:
        result += s
    elif s == " ":
        result += tmp[::-1]
        tmp = ""
        result += s
    else:
        tmp += s

    if i == len(S) - 1 and tmp != "":
        result += tmp[::-1]

print(result)
