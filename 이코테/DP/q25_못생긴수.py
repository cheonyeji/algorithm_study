# 2021-01-24
# 이코테 ch16 다이나믹 프로그래밍 Q35 못생긴 수

n = int(input())

arr = [1]
count = 1
x, y, z = 0, 0, 0
second = arr[x] * 2
third = arr[y] * 3
fifth = arr[z] * 5

# 최소공배수때문에 있는지 검사하고 넣는 코드
# while count < n:
#     result = min(second, third, fifth)
#     if result not in arr:
#         arr.append(result)
#         count += 1

#     if result == second:
#         x += 1
#         second = arr[x] * 2
#     elif result == third:
#         y += 1
#         third = arr[y] * 3
#     else:
#         z += 1
#         fifth = arr[z] * 5

# elif대신 if문으로 계속 걸리면 증가하도록 해주면 최소공배수 문제 해결 가능
while count < n:
    result = min(second, third, fifth)
    arr.append(result)
    count += 1
    if result == second:
        x += 1
        second = arr[x] * 2
    if result == third:
        y += 1
        third = arr[y] * 3
    if result == fifth:
        z += 1
        fifth = arr[z] * 5


print(arr[n - 1])

"""
TC 1 -> 12
10
TC 2 -> 4
4
"""
