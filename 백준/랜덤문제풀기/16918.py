# 2023-09-27 (소요시간 : 1h)
# 문제집 https://www.acmicpc.net/workbook/view/4357
# 실버1. https://www.acmicpc.net/problem/16918

"""
전체 배열 다 훑는걸 두려워하지말자
"""

from sys import stdin

input = stdin.readline

R, C, N = map(int, input().split(" "))

graph = []  # 원본
calcul = []  # 시간계산용


def print_graph(arr):
    for row in arr:
        for v in row:
            print(v, end="")
        print()


def solution(R, C, N):
    for r in range(R):
        temp = list(input().rstrip())
        for c in range(C):
            if temp[c] == "O":
                temp[c] = 0
            else:
                temp[c] = 2
        calcul.append(temp)

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for t in range(3, N + 1):
        bomb = []
        for r in range(R):
            for c in range(C):
                if calcul[r][c] + 3 == t:
                    bomb.append((r, c))

        for br, bc in bomb:
            # 터트리고 폭탄설치
            calcul[br][bc] = t + 1
            for i in range(4):
                nr = br + dr[i]
                nc = bc + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    calcul[nr][nc] = t + 1

    for r in range(R):
        for c in range(C):
            if calcul[r][c] > N:
                calcul[r][c] = "."
            else:
                calcul[r][c] = "O"

    print_graph(calcul)


solution(R, C, N)
