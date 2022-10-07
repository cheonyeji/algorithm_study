# 2445
n = int(input())

for i in range(1, n + 1):
    print("*" * i + " " * 2 * (n - i) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * 2 * (n - i) + "*" * i)

# 2522
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * i)

# 2446
n = int(input())

for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * (1 + 2 * (n - i)))

for i in range(n - 1, 0, -1):
    print(" " * (i - 1) + "*" * (1 + 2 * (n - i)))

# 10991
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" + " *" * (i - 1))

# 10992
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("*" * (1 + 2 * (n - 1)))
    else:
        print(" " * (n - i) + "*" + " " * (1 + 2 * (i - 2)) + "*")
