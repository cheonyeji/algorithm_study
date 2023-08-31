# 2023-08-31 (소요시간 : 못 풀어서 해설 참고)
# 구현 실버2. 백준 18111 마인크래프트 https://www.acmicpc.net/problem/18111

from sys import stdin

input = stdin.readline

N, M, B = map(int, input().split(" "))
heights = {}

for _ in range(N):
    data = list(map(int, input().split(" ")))
    # 해당 높이의 블록 갯수 세기
    for i in data:
        heights[i] = heights.get(i, 0) + 1

answer = int(1e9)
ground_height = 0

# 깎아서 저장한 블록의 수 : save
# 인벤에서 가져와 쌓은 블록의 수 : use
for curr_h in range(257):
    save = 0
    use = 0
    for height in heights:
        # 블록 쌓기
        if height < curr_h:
            use += (curr_h - height) * heights[height]
        # 블록 깎기
        else:
            save += (height - curr_h) * heights[height]

    # 깎은 블록의 수가 사용 가능한 블록의 수보다 크다면 고려X
    if use > save + B:
        continue

    time = save * 2 + use
    if time <= answer:
        answer = time
        ground_height = curr_h

print(answer, ground_height)
