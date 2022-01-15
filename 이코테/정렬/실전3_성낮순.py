# 2022-1-15
# 이코테 ch6 정렬 실전 문제 3 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []

for _ in range(n):
    name, score = input().split()
    score = int(score)
    array.append((score, name))  # 성적순 정렬을 위해 이렇게 입력

array.sort()

# 람다식 사용시
# array = sorted(array, key=lambda data: data[0])

for i in array:
    print(i[1], end=" ")

"""
TC
3
홍길동 97
이순신 77
이이이 100
"""
