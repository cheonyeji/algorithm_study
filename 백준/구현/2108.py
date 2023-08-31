# 2023-08-29 (소요시간 : 35m)
# 구현 실버3. 백준 2108 통계학 https://www.acmicpc.net/problem/2108

from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

# 산술평균 : N개의 수들의 합을 N으로 나눈 값. 소수점 이하 첫째 자리에서 반올림한 값
print(round((sum(nums) / N)))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
nums.sort()
print(nums[N // 2])

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
c_nums = Counter(nums).most_common()
most_common_arr = []
first = True

for i in range(len(c_nums)):
    if first:
        most_common_arr.append(c_nums[i][0])
    if i + 1 < len(c_nums) and c_nums[i][1] == c_nums[i + 1][1]:
        most_common_arr.append(c_nums[i + 1][0])
    else:
        first = False
        break


# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
if len(most_common_arr) == 1:
    print(most_common_arr[0])
else:
    most_common_arr.sort()
    print(most_common_arr[1])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(nums) - min(nums))
