array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬 : 가장 작은 데이터를 선택해서 앞으로 보내는 과정을 반복하는 정렬 방식
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap

print(array)
