import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    # return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return


def solution(numbers):
    n = map(str, numbers)
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int("".join(n)))
    return answer
