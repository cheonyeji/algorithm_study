# 2022-09-21
# 2022 KAKAO BLIND RECRUITMENT 기출 - 주차 요금 계산 (프로그래머스 lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 소요 시간 : 14:17 ~ 14:56 (39m)

import math


def solution(fees, records):
    carnum_fee = []  # (차량번호, 요금) 순 저장
    car_dict = {}

    for r in records:
        time, car_num, inout = r.split(" ")
        if car_num in car_dict:
            car_dict[car_num].append(time)
        else:
            car_dict[car_num] = [time]

    for k in car_dict.keys():
        # 출차 기록이 없는 경우
        if len(car_dict[k]) % 2 != 0:
            car_dict[k].append("23:59")

        # 시간 계산
        total_time = 0
        for i in range(0, len(car_dict[k]), 2):
            # OUT : i+1, IN : i
            out_h, out_m = map(int, car_dict[k][i + 1].split(":"))
            in_h, in_m = map(int, car_dict[k][i].split(":"))

            hour = out_h - in_h
            minute = out_m - in_m

            if minute < 0:
                hour -= 1
                minute += 60

            total_time += hour * 60 + minute

        # 요금 계산
        if total_time > fees[0]:
            carnum_fee.append(
                [k, fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]]
            )
        else:
            carnum_fee.append([k, fees[1]])

    carnum_fee.sort(key=lambda x: x[0])

    answer = [v[1] for v in carnum_fee]
    return answer
