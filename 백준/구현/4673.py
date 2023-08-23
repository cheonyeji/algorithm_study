# 2023-08-23 (소요시간 : 20m)
# 구현 https://www.acmicpc.net/problem/4673


"""
문제 조건대로 쭉 진행하면 되는 문제
1) 첫번째 셀프넘버인 1 출력 후 1을 기준으로 쭉 D(n)을 진행한 뒤 등장한 숫자는 전부 True 표시
2) 다음 False인 숫자는 셀프 넘버이므로 출력 후 D(n) 진행
10000 이하까지 2) 과정 반복
"""


def D(num):
    result = num
    str_num = str(num)
    for n in str_num:
        result += int(n)

    return result


table = [False] * 10001

table[0] = True

for i in range(1, 10001):
    if not table[i]:
        print(i)
        next_num = D(i)
        while next_num < 10001:
            table[next_num] = True
            next_num = D(next_num)
