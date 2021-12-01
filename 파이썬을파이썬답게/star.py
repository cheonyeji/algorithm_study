n = int(input().strip())
answer = ""
for i in range(n):
    answer += "*" * (i + 1)
    if i + 1 == n:
        break
    answer += "\n"

print(answer)
