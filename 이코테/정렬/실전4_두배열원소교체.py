# 2022-1-15
# 이코테 ch6 정렬 실전 문제 4 두 배열의 원소 교체

# 배열 A의 가장 작은 원소와 배열 B의 가장 큰 원소를 교체하기

n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:  # 클 때만 바꿔치기
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:  # 바꿀 필요가 없어지면 반복문 그만
        break

sum = 0
for i in arr1:
    sum += i

# sum(arr1) # 이렇게 해도 결과 동일

print(sum)

"""
TC
5 3
1 2 5 4 3
5 5 6 6 5
"""
