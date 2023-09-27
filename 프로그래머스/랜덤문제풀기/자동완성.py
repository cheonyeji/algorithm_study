def solution(words):
    N = len(words)
    words.sort()  # 단어를 사전순으로 정렬
    result = [0] * N  # 단어마다 입력해야 하는 문자 수

    for i in range(N - 1):
        # 인접하는 두 단어 비교
        now_word = words[i]
        next_word = words[i + 1]
        for j in range(min(len(now_word), len(next_word))):
            if now_word[j] != next_word[j]:
                j -= 1  # 일치하지 않으면 일치하는 최대 인덱스로 저장 후 break
                break

        # 일치하는 인덱스 + 1만큼 문자를 입력해야 찾을 수 있다 (j는 0부터 시작하니 +1)
        # 단, 입력하는 문자 수가 단어 길이를 넘으면 안됨
        result[i] = max(result[i], min(len(now_word), j + 2))
        result[i + 1] = max(result[i + 1], min(len(next_word), j + 2))

    # 합계가 검색결과 총 횟수
    return sum(result)
