# 2022-01-18
# 이코테 ch15 이진 탐색 문제 Q30 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

# 효율성테스트 1,2번 통과 X


def solution(words, queries):
    answer = []
    sorted_words = sorted(words)
    sorted_byLen_words = sorted(words, key=len)

    for i in queries:
        if i[0] != "?":  # 접미사에 ?
            answer.append(find_keyword_EndQuestionmark(sorted_words, i))
        elif i[-1] != "?":  # 접두사에 ?
            answer.append(find_keyword_StartQuesstionmark(sorted_byLen_words, i))
        else:  # 모두 ?
            answer.append(find_keyword_AllQuesstionmark(sorted_byLen_words, i))

    return answer


def first_keyword(array, target, start, end):
    target_textLen = len(target)
    if start > end:
        return None
    mid = (start + end) // 2
    # 특정 문자열을 포함하는 가장 첫번째 인덱스 찾기
    if (
        mid == 0 or array[mid - 1][0:target_textLen] != target[0:target_textLen]
    ) and array[mid][0:target_textLen] == target[0:target_textLen]:
        return mid
    elif array[mid][0:target_textLen] >= target[0:target_textLen]:  # 왼쪽에서 문자열 찾기
        return first_keyword(array, target, start, mid - 1)
    else:
        return first_keyword(array, target, mid + 1, end)


def last_keyword(array, target, start, end):
    target_textLen = len(target)
    if start > end:
        return None
    mid = (start + end) // 2
    # 특정 문자열을 포함하는 가장 마지막 인덱스 찾기
    if (
        mid == len(array) - 1
        or array[mid + 1][0:target_textLen] != target[0:target_textLen]
    ) and array[mid][0:target_textLen] == target[0:target_textLen]:
        return mid
    elif array[mid][0:target_textLen] > target[0:target_textLen]:
        return last_keyword(array, target, start, mid - 1)
    else:
        return last_keyword(array, target, mid + 1, end)


def first_range(array, target, start, end):
    # target : 글자 수
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or len(array[mid - 1]) != target) and len(array[mid]) == target:
        return mid
    elif len(array[mid]) >= target:  # 왼쪽으로
        return first_range(array, target, start, mid - 1)
    else:
        return first_range(array, target, mid + 1, end)


def last_range(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == len(array) - 1 or len(array[mid + 1]) != target) and len(
        array[mid]
    ) == target:
        return mid
    elif len(array[mid]) > target:  # 왼쪽으로
        return last_range(array, target, start, mid - 1)
    else:
        return last_range(array, target, mid + 1, end)


def find_keyword_EndQuestionmark(array, target):
    # ?가 접미사로 붙는 경우
    n = len(array)
    target_notQuestionmark = ""
    for i in target:
        if i != "?":
            target_notQuestionmark += i

    first_idx = first_keyword(array, target_notQuestionmark, 0, n - 1)

    if first_idx == None:
        return 0  # 매치되는 단어 0

    last_idx = last_keyword(array, target_notQuestionmark, 0, n - 1)

    count = 0
    for i in range(first_idx, last_idx + 1):
        if len(array[i]) == len(target):
            count += 1

    return count


def find_keyword_AllQuesstionmark(array, target):
    # 전부 ?인 경우, 글자수 기준으로 정렬된 배열 받아와서 하기
    n = len(array)
    first_idx = first_range(array, len(target), 0, n - 1)

    if first_idx == None:
        return 0  # target과 동일한 길이인 글자 0

    last_idx = last_range(array, len(target), 0, n - 1)

    return last_idx - first_idx + 1


def find_keyword_StartQuesstionmark(array, target):
    # ?가 접두사로 붙는 경우
    n = len(array)
    target_notQuestionmark = ""
    for i in target:
        if i != "?":
            target_notQuestionmark += i

    first_idx = first_range(array, len(target), 0, n - 1)
    if first_idx == None:
        return 0  # target과 동일한 길이인 글자 0

    last_idx = last_range(array, len(target), 0, n - 1)

    count = 0
    for i in range(first_idx, last_idx + 1):
        if (
            array[i][len(target) - len(target_notQuestionmark) :]
            == target_notQuestionmark
        ):  # 타겟 글자 포함
            count += 1

    return count


words = ["a", "bb", "frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
