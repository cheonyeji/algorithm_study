s, n = input().strip().split(" ")
n = int(n)
result = ""
result += s + " " * (n - len(s)) + "\n"  # s.ljust(n)
result += (
    " " * ((n - len(s)) // 2) + s + " " * ((n - len(s)) // 2) + "\n"
)  # s.center(n)
result += " " * (n - len(s)) + s  # s.rjust(n)
print(result)
