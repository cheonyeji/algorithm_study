# 2022-07-17
# 프로그래머스 Lv2 - 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 소요시간 : 18:04 ~ 19:01 (57m)

# key : uid
# value : [ 현재닉네임, [answer몇번째에 있는지 인덱스값들] ]
user_list = {}


def Change(uid, name, answer):
    # 이미 등장한 적이 있는 유저가 닉네임을 바꿀 것
    for idx in user_list[uid][1]:
        answer[idx] = answer[idx].replace(user_list[uid][0], name)

    user_list[uid][0] = name


def Enter(uid, name, answer):
    # 이미 입장했던 기록이 있는 유저라면
    if uid in user_list:
        # 나갔다가 닉 바꿔서 들어온거면 예전에 있던거 싹 다 닉네임 바꿔주기
        if user_list[uid][0] != name:
            Change(uid, name, answer)
        # 그러고 나서 입장처리
        user_list[uid][1].append(len(answer))

    # 첫번째 입장인 경우
    else:
        user_list[uid] = [name, [len(answer)]]

    answer.append(name + "님이 들어왔습니다.")


def Leave(uid, answer):
    # 무조건 등장한 적이 있는 유저가 떠날 것
    user_list[uid][1].append(len(answer))
    answer.append(user_list[uid][0] + "님이 나갔습니다.")


def solution(record):
    answer = []

    for r in record:
        data = r.split(" ")
        if data[0] == "Enter":
            Enter(data[1], data[2], answer)
        elif data[0] == "Leave":
            Leave(data[1], answer)
        else:
            Change(data[1], data[2], answer)

    return answer
