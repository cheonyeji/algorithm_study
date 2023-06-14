from sys import stdin

input = stdin.readline

# arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr = [
    3,
    2,
    4,
    4,
    2,
    5,
    2,
    5,
    5,
]


def solution1(arr):
    # set_arr = set(arr)  # Set 자료형은 순서보장X
    ordered_set_arr = list(dict.fromkeys(arr))  # 순서보장방법
    my_dict = {i: arr.count(i) for i in ordered_set_arr}

    answer = []
    for key in my_dict:
        if my_dict[key] == 1:
            continue
        answer.append(my_dict[key])

    if len(answer) == 0:
        return [-1]
    else:
        return answer


from collections import Counter


def solution2(arr):
    my_dict = dict(Counter(arr))
    print(list(my_dict.values()))
    # print(my_dict)


# print(solution1(arr))
solution2(arr)
