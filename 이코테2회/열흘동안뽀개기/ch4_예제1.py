# 2022-06-24
# 이코테 열흘동안 뽀개기 2일차
# 구현 예제 1 상하좌우
# 소요 시간 :

def move(r, c, case, N):
    if case == 'L' and c > 2:
        return (r, c-1)
    elif case == 'R' and c < N:
       return (r, c+1)
    elif case == 'U' and r > 2:
        return (r-1, c)
    elif case == 'D' and r < N:
        return (r+1, c)
    
    # 어떤 경우에도 안 걸리는 경우
    return (r, c) 

N = int(input())
move_data = list(input().split())

r = 1
c = 1

for m in move_data:
    r, c = move(r, c, m, N)


print(r, c)

