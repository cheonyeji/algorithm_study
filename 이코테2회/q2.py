# 2022-03-06
# 이코테 2회차 그리디 Q2 곱하기 혹은 더하기

# 등장하는 숫자가 0이거나 1인 경우 더하고 나머지는 곱해줘야 가장 큰 수 만들기 가능

str_a = input()

answer = 0

if int(str_a[0]) == 0 or int(str_a[0]) == 1:
    answer = int(str_a[0]) + int(str_a[1])

for i in range(2, len(str_a)):
    if int(str_a[i]) == 0 or int(str_a[i]) == 1:
        answer += int(str_a[i])
    else:
        answer *= int(str_a[i])

print(answer)
        

'''
TC 1 -> 576
02984
TC 2 -> 210
567
TC 3 -> 12
01123
'''