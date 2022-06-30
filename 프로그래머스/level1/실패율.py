# 2022-06-30
# 프로그래머스 lv1 - 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 소요 시간 : 17:49 ~ 18:17 (30m)


def countUser(N, stages):
    # 0번째 스테이지 ~ N+1번째 스테이지 (0번지 사용X)
    left_user = [0 for _ in range(N+2)]
    for i in stages:
        left_user[i] += 1
    return left_user

def solution(N, stages):
    answer = []
    left_user = countUser(N, stages)
    
    result = []
    total_user = len(stages)
    
    # 끝까지 깬 경우를 위해 N+2까지 고려했으므로 마지막은 살펴보지 않음
    for i in range(1, len(left_user)-1):
        # 스테이지에 도달한 유저가 없는 경우, 해당 스테이지 실패율 0
        if total_user == 0:
            result.append((0, i))
        else:
            result.append((left_user[i]/total_user, i))
        total_user -= left_user[i]
        
    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
    # item[0] : 실패율, item[1] : 스테이지 
    answer = sorted(result, key = lambda item : (- item[0], item[1]))    
    answer = [x[1] for x in answer]
    
    return answer
