# 2022-04-03
# 프로그래머스 고득점 kit 그리디 - 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 빌려줄 수 있음
# 체육복을 적당히 빌려 최대한 많은 학생이 체육수업을 들어야 함

"""
n명학생 -> [1,2,3,...,n] (0번 인덱스가 1번째 학생)
lost -> 체육복을 도난당한 학생 수 중복x
reserve -> 여벌의 체육복을 가져온 학생 수 중복x
여벌체육복을 가져온 학생이 도난당했을 수 있고, 그 학생은 이제 빌려줄 수 없음

n+1명의 학생 배열을 만들고, 1로 값 초기화
reserve 배열을 돌면서 해당 값-1번째에 해당하는 인덱스에 +1
lost 배열을 돌면서 해당 값-1번째에 해당하는 인덱스에 -1 해주기

가장 많은 학생들이 체육 수업을 들으려면 겹치지 않게! 값을 줘야함
학생 배열을 돌면서 i번째 학생이 체육복이 없는 경우(값=0) 앞뒤로 보면서
체육복이 2벌인 학생으로부터 가져와야함

가져오면서 수업을 들을 수 있는 학생 수를 세는게 더 효율적인지
마지막에 배열.count(1) 값을 리턴하는게 더 효율적인지는 추후 생각

"""


def solution(n, lost, reserve):
    answer = 0

    students = [1 for _ in range(n + 1)]  # 0번째 인덱스는 사용x
    students[0] = 0

    for i in reserve:
        students[i] += 1

    for i in lost:
        students[i] -= 1

    for i in range(1, len(students)):
        if students[i] == 0:
            # 앞뒤로 체크
            if students[i - 1] == 2:
                students[i - 1], students[i] = 1, 1
            elif i != len(students) - 1 and students[i + 1] == 2:
                students[i + 1], students[i] = 1, 1
            else:
                continue

    for i in students:
        if i > 0:
            answer += 1

    return answer


print(solution(5, [2, 4, 5], [1, 3]))
