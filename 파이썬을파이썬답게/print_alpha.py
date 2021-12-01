num = int(input().strip())
result = ""
# 1: 대문자
if num:
    for i in range(65, 91):
        result += chr(i)
else:
    for i in range(97, 123):
        result += chr(i)

print(result)

# 파이썬을 파이썬답게
import string

num2 = int(input().strip())
result2 = ""
# 1: 대문자
if num2:
    print(string.ascii_uppercase)
else:
    print(string.ascii_lowercase)
