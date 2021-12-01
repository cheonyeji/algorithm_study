# flag or else
import math

numbers = [int(input()) for _ in range(5)]
multifly = 1
flag = True

# 일반적인 방법 (flag 변수 사용)
# for num in numbers:
#     multifly *= num
#     if math.sqrt(multifly) == int(math.sqrt(multifly)):
#         flag = False
#         print("found")
#         break
# if flag:
#     print("not found")

# 파이썬을 파이썬답게 for-else문
for num in numbers:
    multifly *= num
    if math.sqrt(multifly) == int(math.sqrt(multifly)):
        print("found")
        break
else:
    print("not found")
