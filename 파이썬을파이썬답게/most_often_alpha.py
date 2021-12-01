# 가장 많이 등장하는 알파벳 찾기
# 일반적인 방식
# my_str = input().strip()

# letter_count = {}

# for i in my_str:
#     letter_count[i] = my_str.count(i)
# most_often = ""
# count = 0
# for k, v in letter_count.items():
#     if v > count:
#         count = v
#         most_often = k
#     elif v == count:
#         count = v
#         most_often += k

# answer = "".join(sorted(most_often))
# print(answer)

# 파이썬을 파이썬답게
# collections.Counter 클래스 사용하기
import collections

my_str = input().strip()
my_list = []
for i in my_str:
    my_list.append(i)

answer = collections.Counter(my_list)
most_often = ""
count = 0
for k, v in answer.items():
    if v > count:
        count = v
        most_often = k
    elif v == count:
        count = v
        most_often += k

result = "".join(sorted(most_often))
print(result)
