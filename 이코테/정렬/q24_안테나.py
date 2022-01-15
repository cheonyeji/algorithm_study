# 2022-01-15
# 이코테 ch14 정렬 문제 Q24 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())

data = list(map(int, input().split()))

data.sort()

index = len(data) // 2

if len(data) % 2 == 0:
    print(data[index - 1])
else:
    print(data[index])


# data[(n-1)//2] 를 출력함으로서 11~16번 코드를 한줄로 쓸 수도 있다

"""
TC 1 -> 결과 : 5
4
5 1 7 9 
TC 2 -> 결과 : 5
5
1 3 5 7 9
"""
