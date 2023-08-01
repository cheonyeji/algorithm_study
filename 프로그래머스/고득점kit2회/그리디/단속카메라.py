# 2023-08-01 (소요시간 : 1h 내에 못풀어서 풀이 참고)


# 삽질의 흔적... 진입을 기준으로 삼으면 안된다 엉엉
# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[0])

#     prev_start, prev_end = routes[0][0], routes[0][1]
#     camera = 30001

#     for i in range(1, len(routes)):
#         start, end = routes[i][0], routes[i][1]
#         if start <= prev_end:
#             if camera < prev_end and camera != 30001:  # 포함하지 않으므로 카메라 설치
#                 answer += 1
#                 camera = 30001
#             else:
#                 camera = prev_end  # 카메라 위치 업데이트
#         else:
#             answer += 1  # 포함하지 않으므로 카메라 설치
#             camera = start  # 카메라 위치 업데이트

#         prev_start, prev_end = start, end
#     if camera != 30001:
#         answer += 1

#     if len(routes) == 1:
#         answer = 1
#     return answer


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001  # -30001로 초기 데이터 설정

    for start, end in routes:
        if camera < start:
            answer += 1  # 단속할 수 없는 위치에 있는 것이므로 카메라 설치
            camera = end  # 최대한 뒤(진출 위치)에 카메라 설치
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2

print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
print(
    solution(
        [
            [0, 0],
        ]
    )
)  # 1
print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
