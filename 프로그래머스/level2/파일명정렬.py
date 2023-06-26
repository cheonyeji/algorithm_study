# 2023-06-15
# 프로그래머스 lv2 - 파일명정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# 소요 시간 : 18:22 ~ 18:49 (27m)


def solution(files):
    answer = []
    arr = [["", "", ""] for _ in range(len(files))]

    for i in range(len(files)):
        headEnd = False
        numEnd = False
        for j, f in enumerate(files[i]):
            if (not headEnd and not numEnd) and not (48 <= ord(f) <= 57):
                arr[i][0] += f
            elif (not numEnd) and 48 <= ord(f) <= 57:
                arr[i][1] += f
                headEnd = True
            else:
                numEnd = True
                arr[i][2] += files[i][j:]
                break
    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for item in arr:
        answer.append("".join(map(str, item)))
    return answer
