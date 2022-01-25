# 2021-01-24
# 이코테 ch16 다이나믹 프로그래밍 Q36 편집 거리
# https://www.acmicpc.net/problem/15483


def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 두 문자열이 같다면
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]


str1 = input()
str2 = input()

print(edit_dist(str1, str2))

# 첫번째 풀이 (일부 테스트케이스만 통과했음)
# count = 0

# index = 0
# cur_len = 0

# for i in range(len(str_a)):
#     if str_b[index] == str_a[i]:
#         index += 1
#         cur_len += 1
#         continue
#     else:
#         # 교체
#         if (len(str_b) - cur_len) == (len(str_a) - i):
#             count += 1
#             index += 1
#             cur_len += 1
#             continue
#         # 삽입
#         same = False
#         for j in range(i, len(str_b)):
#             if str_b[j] == str_a[i]:
#                 count += j - i
#                 index += j - i + 1
#                 same = True
#                 cur_len += j - i + 1

#                 break
#         # 삭제
#         if not same:
#             count += 1
#             index += 1


# print(count)

"""
TC 1 -> 1
cat
cut
TC 2 -> 3
sunday
saturday
"""
