array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 삽입 정렬 : 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하는 정렬 방식
# 데이터가 거의 정렬되어 있는 경우, 효율적이다 (퀵 정렬보다 빠름)

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i번째 인덱스보다 앞의 원소를 전부 살펴봐야 하므로 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j - 1]:  # 한칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
