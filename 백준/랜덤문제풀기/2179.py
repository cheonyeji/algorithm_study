# 2023-10-05
# 백준 2179 비슷한 단어 https://www.acmicpc.net/problem/2179
# 지나치게 코드가 길어진다 싶으면 로직이 꼬인것
# 다시 처음으로 돌아가서 생각해보기 (코드아까워하지말고)

from sys import stdin

input = stdin.readline

N = int(input())
input_ = [input().rstrip() for _ in range(N)]

arr = list(enumerate(input_))
arr.sort(key=lambda x: x[1])

"""
계속 인덱스를 업데이트해주는 식으로 갔는데 전체 개수가 20,000이니까
글자간 비교해서 같은 글자개수를 모두 저장해준 다음
제일 긴 같은 글자개수 가진 글자 출력, 그 접두사를 갖고있는 다음 등장 글자출력 해주면 될것같은데 시간이없어서 그만... 
"""


def checkSame(a, b):
    same = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            same += 1
        else:
            break
    return same


lengs = [0 for _ in range(N)]
max_len = 0
for i in range(N - 1):
    same = checkSame(arr[i][1], arr[i + 1][1])
    max_len = max(same, max_len)

    lengs[arr[i][0]] = max(lengs[arr[i][0]], same)
    lengs[arr[i + 1][0]] = max(lengs[arr[i + 1][0]], same)

ans1 = 0
ans2 = 0
for i in range(len(lengs)):
    if lengs[i] == max_len and ans1 == 0:
        ans1 = input_[i]
        prefix = ans1[:max_len]
        continue
    if lengs[i] == max_len and input_[i][:max_len] == prefix:
        ans2 = input_[i]
        break

if max_len == 0:
    print(arr[0], arr[1])
else:
    print(ans1, ans2)
