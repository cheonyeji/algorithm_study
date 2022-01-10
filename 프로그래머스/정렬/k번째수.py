# 선택정렬
def sorting(array, start, end, find):
    new_array = array[start - 1 : end]
    for i in range(len(new_array)):
        min_index = i
        for j in range(i + 1, len(new_array)):
            if new_array[min_index] > new_array[j]:
                min_index = j
        new_array[min_index], new_array[i] = new_array[i], new_array[min_index]

    return new_array[find - 1]


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorting(array, commands[i][0], commands[i][1], commands[i][2]))
    return answer
