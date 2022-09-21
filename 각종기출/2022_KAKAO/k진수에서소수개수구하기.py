# 2022-09-20
# 2022 카카오 테크 인턴십 기출 - k진수에서 소수 개수 구하기 (프로그래머스 lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 소요 시간 : 15:17 ~ 16:06, 16:21~16:31 (60m)

# 진법 변환
def convert(n, k):
    result = ""
    q, r = divmod(n, k)
    result += str(r)

    while q != 0:
        q, r = divmod(q, k)
        result += str(r)

    return result[::-1]


# 소수 판별 (제곱근까지만 판단)
def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # 소수 아님
            return False
    return True


def solution(n, k):
    answer = 0

    converted_n = convert(n, k)

    check_num = ""

    flag_0P0 = False
    flag_P0 = False
    flag_0P = False
    flag_P = False

    for i in range(len(converted_n)):
        # 맨 앞인 경우
        if i == 0:
            # P0, P 가능
            check_num += converted_n[i]
            flag_P, flag_P0 = True, True
            continue

        if converted_n[i] == "0":
            flag_P = False
            flag_0P = True
            # 만약 맨앞에서부터 보던 중이었다면
            if flag_P0:
                if isPrime(int(check_num)):
                    answer += 1
                check_num = ""
                flag_0P0, flag_P0 = True, False
                continue

            # 한번이라도 0이 등장한 적이 있다면
            elif flag_0P0 and check_num != "":
                if isPrime(int(check_num)):
                    answer += 1
                check_num = ""
        else:
            check_num += converted_n[i]

    # 맨 뒤까지 다 봤는데 0이 안나온 경우였다면, P 경우 체크
    if flag_P and check_num != "" and isPrime(int(check_num)):
        answer += 1
    # 맨 뒤까지 다 봤고 0P가 가능한 경우
    if flag_0P and check_num != "" and isPrime(int(check_num)):
        answer += 1

    return answer
