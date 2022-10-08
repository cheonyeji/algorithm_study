# 2022-10-08
# week1 - 수학. 로또
# https://www.acmicpc.net/problem/6603
# 소요시간 : 23:55~ 00:08 (20m)

from itertools import combinations

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0:
        break
    numList = data[1:]

    # 출력 형식 문제에서 원하는대로 정제
    for i in combinations(numList, 6):
        result = str(i)
        result = result.replace(",", "")
        print("".join(result[1:-1]))

    print()
