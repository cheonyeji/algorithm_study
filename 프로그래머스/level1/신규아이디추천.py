# 2022-06-30
# 프로그래머스 lv1 - 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410
# # 23:15 ~ 00:38 (80m)
import re


def solution(new_id):
    answer = ""

    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)

    # 3단계
    cnt_point = new_id.count(".")
    for i in range(cnt_point, 1, -1):
        new_id = new_id.replace("." * i, ".")

    # 4단계
    if len(new_id) != 0:
        if new_id[0] == ".":
            new_id = new_id[1:]

    if len(new_id) != 0:
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # 5단계
    if len(new_id) == 0:
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while True:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break

    answer = new_id
    return answer
