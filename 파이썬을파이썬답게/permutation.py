import itertools


def solution(mylist):
    answer = list(map(list, itertools.permutations(mylist)))
    answer.sort()  # 사전순 정렬
    return answer


def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


print(solution([2, 1, 3]))
print(permute([2, 1, 3]))
