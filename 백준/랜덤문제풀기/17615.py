# 2023-09-28 (소요시간 : 40m+해설참고)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버1. https://www.acmicpc.net/problem/17615

"""
핵심포인트 : 최대한 뭉친 결과는 왼쪽이나 오른쪽에 몰려있는 것!!!
(가장 큰 뭉치로 움직여야한다고 생각해서 코드가 길어지고 로직 꼬임...)

여기서 그리디하게 움직이려면
왼쪽으로 몰때는 왼쪽 뭉텅이를 싹 날려주고 남은 공R/B 개수 세주면 됨
"""

from sys import stdin

input = stdin.readline

N = int(input())
data = input().rstrip()

cnt = []

# 오른쪽으로 R 보내기
# 오른쪽 R 뭉탱이 싹 날리고 남은 R의 갯수 카운트
redRight = data.rstrip("R")
cnt.append(redRight.count("R"))

# 왼쪽으로 R 보내기
redLeft = data.lstrip("R")
cnt.append(redLeft.count("R"))

# 오른쪽으로 B 보내기
blueRight = data.rstrip("B")
cnt.append(blueRight.count("B"))

# 왼쪽으로 B 보내기
blueLeft = data.lstrip("B")
cnt.append(blueLeft.count("B"))

print(min(cnt))
