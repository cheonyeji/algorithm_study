# 2022-06-26
# 이코테 열흘동안 뽀개기 프로젝트 3일차
# 구현 실전 2 왕실의 나이트
# 소요 시간 : 10분

# L자로 움직일 수 있는 경우의 수를 모두 저장
steps = [(-2, 1), (2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

data = input()
row = int(data[1])
col = int(ord(data[0]) - ord("a")) + 1  # 파이썬 ord('a') -> 97 반환

answer = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    # 이동 가능하다면
    if next_row >= 1 and next_col <= 8 and next_col >= 1 and next_row <= 8:
        answer += 1


print(answer)
