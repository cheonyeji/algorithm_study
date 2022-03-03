# 2022-03-03
# 삼성 기출 문제 - 백준 13458 시험 감독
# https://www.acmicpc.net/problem/13458

n = int(input())
students = list(map(int, input().split()))
b, c= map(int, input().split())

total = 0

# if b<=c:
#     for i in students:
#         if i > c:
#             total += (i // c + math.ceil(i%c))
#         # 부감독관 한명으로 충분
#         else:
#             total += 1
# else:
#     for i in students:
#         if i > b:
#             total += (1 + (i-b)//c + math.ceil((i-b)%c))

#         # 총감독관 한명으로 충분
#         else:
#             total += 1

# 무조건 총감독관은 한명 박아둬야함
for i in students:
    if i>b:
        total += (1 + (i-b)//c + (1 if (i-b)%c != 0 else 0))
    else:
        total += 1

print(total)