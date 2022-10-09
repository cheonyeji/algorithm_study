# 2022-10-08
# week1 - 수학. N과 M(2)
# https://www.acmicpc.net/problem/15650
# 소요시간 : 00:40~ 1:00 (20m)

n, m = map(int, input().split())


result = []

answer = []


def back():
    if len(result) == m:
        tmp = sorted(result)
        if tmp not in answer:
            answer.append(tmp)
        return

    for i in range(1, n + 1):
        if i not in result:
            result.append(i)
            back()
            result.pop()


back()

for i in answer:
    print(" ".join(map(str, i)))
