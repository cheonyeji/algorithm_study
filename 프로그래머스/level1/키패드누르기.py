# 2022-07-01
# 프로그래머스 lv1 - 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# 소요 시간 : 22:35 ~ 22:54 (20m)


def moveHand(number, pos):
    dial = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

    for r in range(len(dial)):
        for c in range(len(dial[r])):
            if number == dial[r][c]:
                return [r, c]


def calculDist(number, pos):
    dial = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    dist = 0

    for r in range(len(dial)):
        for c in range(len(dial[r])):
            if number == dial[r][c]:
                dist = abs(pos[0] - r) + abs(pos[1] - c)
    return dist


def solution(numbers, hand):
    answer = ""

    # [row, col]
    l_p = [3, 0]
    r_p = [3, 2]

    for num in numbers:
        # 무조건 왼손
        if num == 1 or num == 4 or num == 7:
            l_p = moveHand(num, l_p)
            answer += "L"
        # 무조건 오른손
        elif num == 3 or num == 6 or num == 9:
            r_p = moveHand(num, r_p)
            answer += "R"
        # 양손 모두 고려
        else:
            l_dist = calculDist(num, l_p)
            r_dist = calculDist(num, r_p)
            # 왼손 움직이기
            if l_dist < r_dist:
                l_p = moveHand(num, l_p)
                answer += "L"
            # 오른손 움직이기
            elif l_dist > r_dist:
                r_p = moveHand(num, r_p)
                answer += "R"
            # 거리 똑같으므로 편한 손 움직이기
            else:
                if hand[0] == "l":
                    l_p = moveHand(num, l_p)
                    answer += "L"
                else:
                    r_p = moveHand(num, r_p)
                    answer += "R"
    return answer
