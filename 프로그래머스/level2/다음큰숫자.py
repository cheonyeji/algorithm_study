# 2022-08-04
# 프로그래머스 Lv2 - 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 소요 시간 : 16:00 ~ 16:15 (15m)


# 이 함수 대신 bin메소드를 사용해도 된다
def convert10to2AndCountOne(n):
    cnt_one = 0
    result = ''
    
    q, r = divmod(n, 2)
    while True:
        result += str(r)
        if r==1:
            cnt_one += 1
        q, r = divmod(q, 2)
        
        if q==0:
            result += str(r)
            if r==1:
                cnt_one += 1
            break
    
    return cnt_one

def solution(n):
    answer = 0
    
    # count로 한번 더 연산했더니 테케2 시간초과나서 바로 함수내에서 1의개수 리턴
    cnt_one_n = convert10to2AndCountOne(n)
    
    while True:
        n += 1
        cnt_one_answer = convert10to2AndCountOne(n)
        
        if cnt_one_answer == cnt_one_n:
            answer = n
            break
    
    return answer
