# 2022-06-30
# 프로그래머스 lv1 - 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334
# 소요 시간 : 22:50 ~ 23:00 (10m)


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    # 유저별 신고당한 횟수 저장
    bad_count = [0 for _ in range(len(id_list))]
    # 유저별 신고한 유저 저장 (중복 체크를 위해)
    who_reported = [[] for _ in range(len(id_list))]

    for r in report:
        user_id, bad_id = r.split(" ")
        target = id_list.index(bad_id)

        # 첫번째 신고인 경우에만 count
        if not user_id in who_reported[target]:
            bad_count[target] += 1
            who_reported[target].append(user_id)

    for i in range(len(bad_count)):
        # k번 이상 신고당한 경우, 그 유저를 신고한 유저에게 이메일 발송
        if bad_count[i] >= k:
            for user_id in who_reported[i]:
                answer[id_list.index(user_id)] += 1

    return answer
