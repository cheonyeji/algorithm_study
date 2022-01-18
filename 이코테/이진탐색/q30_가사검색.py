# 2022-01-18
# 이코테 ch15 이진 탐색 문제 Q30 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

# 효율성때문에 글자수를 인덱스로 배열에 저장하니까 통과...!!!!!!!
# 카카오 레벨 4를 어찌저찌 풀다니 감격이다 정말

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])  # 뒤집어서 넣기

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for i in queries:
        if i[0] != "?":  # 접미사에 ?
            answer.append(find_keyword_EndQuestionmark(array[len(i)], i))
        elif i[-1] != "?":  # 접두사에 ?
            answer.append(find_keyword_StartQuesstionmark(reversed_array[len(i)], i))
        else:  # 모두 ?
            answer.append(find_keyword_AllQuesstionmark(reversed_array[len(i)], i))

    return answer


# 특정 문자열을 포함하는 가장 첫번째 인덱스 찾기
def first_keyword(array, target, start, end):
    target_textLen = len(target)
    if start > end:
        return None
    mid = (start + end) // 2
    # 여기에서 find메서드를 사용해서는 안되고 정확한 익덱스번쨰에 있는지를 체크해야 한다!
    # find메서드 사용시 문자열에 존재하기만 하면 true (원래는 find써서 테스트케이스 통과 실패)
    if (
        mid == 0 or array[mid - 1][0:target_textLen] != target[0:target_textLen]
    ) and array[mid][0:target_textLen] == target[0:target_textLen]:
        return mid
    elif array[mid][0:target_textLen] >= target[0:target_textLen]:  # 왼쪽에서 문자열 찾기
        return first_keyword(array, target, start, mid - 1)
    else:
        return first_keyword(array, target, mid + 1, end)


# 특정 문자열을 포함하는 가장 마지막 인덱스 찾기
def last_keyword(array, target, start, end):
    target_textLen = len(target)
    if start > end:
        return None
    mid = (start + end) // 2
    if (
        mid == len(array) - 1
        or array[mid + 1][0:target_textLen] != target[0:target_textLen]
    ) and array[mid][0:target_textLen] == target[0:target_textLen]:
        return mid
    elif array[mid][0:target_textLen] > target[0:target_textLen]:
        return last_keyword(array, target, start, mid - 1)
    else:
        return last_keyword(array, target, mid + 1, end)


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

    return last_idx - first_idx + 1


def find_keyword_AllQuesstionmark(array, target):
    # 전부 ?인 경우
    return len(array)


def find_keyword_StartQuesstionmark(array, target):
    # ?가 접두사로 붙는 경우
    n = len(array)
    reversed_target = target[::-1]  # 뒤집어서 저장했으니 얘도 뒤집어서 비교해주기
    target_notQuestionmark = ""
    for i in reversed_target:
        if i != "?":
            target_notQuestionmark += i

    first_idx = first_keyword(array, target_notQuestionmark, 0, n - 1)
    if first_idx == None:
        return 0  # target과 동일한 길이인 글자 0

    last_idx = last_keyword(array, target_notQuestionmark, 0, n - 1)

    return last_idx - first_idx + 1


words = ["a", "bb", "frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
# for word in words:
#     array[len(word)].append(word)
#     reversed_array[len(word)].append(word[::-1])  # 뒤집어서 넣기
# for i in range(10001):
#     array[i].sort()
#     reversed_array[i].sort()

# result = find_keyword_EndQuestionmark(array[len("fro??")], "fro??")  # 3
# result2 = find_keyword_AllQuesstionmark(reversed_array[len("?????")], "?????")  # 5
# result3 = find_keyword_StartQuesstionmark(reversed_array[len("????o")], "????o")  # 2
# print(result, result2, result3)

"""
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
    if (mid == 0 or array[mid - 1].find(target) == -1) and array[mid].find(
        target
    ) != -1:
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
    if (mid == len(array) - 1 or array[mid + 1].find(target) == -1) and array[mid].find(
        target
    ) != -1:
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
sorted_words = sorted(words)
sorted_byLen_words = sorted(words, key=len)
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
"""
