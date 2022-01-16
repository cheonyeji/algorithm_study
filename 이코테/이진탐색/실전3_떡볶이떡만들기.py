# 2022-01-16
# 이코테 ch7 이진 탐색 실전 문제 3 떡볶이 떡 만들기
# https://www.acmicpc.net/problem/2805 (위 문제와 동일)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

answer = 0
while start <= end:
    mid = (start + end) // 2

    cutted = sum((i - mid) if (i - mid) >= 0 else 0 for i in data)

    if cutted == m:
        answer = mid
        break
    elif cutted < m:  # 적게 잘라서 더 많이 잘라야 함 (왼쪽 부분 탐색)
        end = mid - 1
    else:  # 너무 많이 자른 것. 더 적게 잘라야 하므로 오른쪽에서 보기
        answer = mid  # 이 경우에는 답이 될 수도 있으니까 저장
        start = mid + 1

print(answer)


# 약간... 알고리즘에 매몰되서 잘못 푼 풀이 ㅠㅠ
# 벌목기의 높이를 무조건 입력받은 배열 안의 값으로만 설정할 필요가 없다
# 중간값을 기준으로 +1 -1 해주면서 보기만 하면 되는 문제였는데 엄청나게 꼬아서 생각함;
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()


# def binary_search(array, target, start, end):
#     if start > end:
#         # array[start] ~ array[end] 사이에서 값 찾아야 함
#         if array[start] <= array[end]:
#             arr = [array[start], array[end]]
#         else:
#             arr = [array[end], array[start]]
#         return arr
#     mid = (start + end) // 2
#     cutted = sum((i - array[mid]) if (i - array[mid]) >= 0 else 0 for i in array)

#     if cutted == target:
#         return array[mid]  # int형 return인 경우 바로 값 출력
#     elif cutted > target:  # 너무 많이 자른 것. 더 긴 기준으로 다시 잘라보기
#         return binary_search(array, target, mid + 1, end)
#     else:  # 너무 적게 자른 것. 더 짧은 기준으로 다시 잘라보기
#         return binary_search(array, target, start, mid - 1)


# result = binary_search(data, m, 0, n - 1)

# if type(result) == int:
#     answer = result
# else:  # 리스트가 돌아온 경우
#     answer = 0
#     for i in range(result[0], result[1]):
#         cutted = sum((j - i) if (j - i) >= 0 else 0 for j in data)
#         answer = i
#         if cutted == m:
#             break
#         elif cutted < m:  # 작아지면 더이상 볼 필요가 없음
#             answer = i + 1
#             break


# print(answer)

"""
TC 1 -> 결과 : 15
4 6
19 15 10 17
TC 2 -> 결과 : 16
4 3
19 15 10 17
"""
