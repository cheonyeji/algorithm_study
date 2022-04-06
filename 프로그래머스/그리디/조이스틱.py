# 2022-04-06
# 프로그래머스 고득점 kit 그리디 - 조이스틱 
# https://programmers.co.kr/learn/courses/30/lessons/42860

'''
A : 65
Z : 90

알파벳 바꿀 때 (어차피 A인 경우에는 0이므로 그냥 계산해주면 됨)
1) N(78) 이전 문자로 변경 시 위로 이동 -> 이동횟수 = 해당문자아스키값 - 65(A)
2) 이외에는 아래로 이동 -> 이동횟수 = 90(Z) - 해당문자아스키값 + 1 (+1은 A->Z 변경)
-> 더 작은 값으로 설정하기

좌우 이동 ** 풀이 참고 **
- 기본 최소 이동 횟수 : 길이 -1
- 연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하며 알파벳을 변경하는 것이 가장 효율적
(기존, 왼쪽시작, 오른쪽시작) 중 min값이 답
- 연속되는 A가 있는 곳에는 굳이 갈 필요 없음, 그 부분을 제외하고 수정하는 경우 계산
- 다만 연속되는 A가 여러 개인 경우, 가장 긴 부분을 안 가는 것이 효율적임

'''

def solution(name):
    answer = 0

    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, 연속된 A의 왼쪽 시작방식, 연속된 A의 오른쪽시작방식 비교 및 갱신
        min_move = min([min_move, 2*i+len(name)-next, i+2*(len(name) - next)])

    # 상하이동 횟수 + 좌우이동 횟수     
    answer += min_move
    return answer