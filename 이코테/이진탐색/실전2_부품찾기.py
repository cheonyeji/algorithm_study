# 2022-01-16
# 이코테 ch7 이진 탐색 실전 문제 2 부품 찾기

# Ver1. 이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:  # 중간값 기분 왼쪽을 봐야함
        return binary_search(array, target, start, mid - 1)
    else:  # 중간값 기준 오른쪽 보기
        return binary_search(array, target, mid + 1, end)


import sys

input = sys.stdin.readline

n = int(input())  # 입력범위 1~1000만

data = list(map(int, input().split()))
# 이진탐색을 위해 데이터 정렬
data.sort()

m = int(input())

target = list(map(int, input().split()))

for i in target:
    result = binary_search(data, i, 0, n - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

"""
TC
5
8 3 7 9 2
3
5 7 9
"""

#############################################################
# Ver2. 계수 정렬 (하나하나 찾기)
n = int(input())
array = [0] * 1000001  # 입력값인 m의 크기만큼 저장

for i in input().split():
    array[int(i)] = 1

m = int(input())
target = list(map(int, input().split()))

for i in target:
    if array[i] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")
#############################################################
# Ver3. 집합 자료형 이용
# 단순히 해당 값이 한번이라도 등장하는지를 검사하면 되므로
n = int(input())
data = set(map(int, input().split()))  # 준복을 허용하지 않는 집합 자료형 set사용

m = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in data:
        print("yes", end=" ")
    else:
        print("no", end=" ")
