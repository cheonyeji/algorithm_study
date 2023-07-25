# 2023-07-25 (소요시간 : 1h)
'''
자릿수 맞춰서 풀어주면 되는 문제
TC 11번은 아마도 0만 등장하는 것 같은데 문자열 -> 숫자 -> 문자열 재 변환해주는 것을 추가하니까 OK
'''
def solution(numbers):
    answer = ''
    temp = list(map(str, numbers))
    data = []
    for i, num in enumerate(temp):
        data.append([("".join(num*(5-len(num))))[:4], i])

    data.sort(reverse=True, key=lambda x : (x[0]))
    for item in data:
        answer += str(numbers[item[1]])
    return str(int(answer))

print(solution([9,8,99,90,98,989]))