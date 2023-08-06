# 2023-08-06
# 좋은 코드 공부용
import heapq


def solution(operations):
    answer = []
    minq, maxq = [], []

    # 각 id별로 활성상태를 기록하는 플래그 리스트
    visited = [False for _ in range(1000001)]

    i = 0  # 식별자 id
    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)

        if op == "I":
            heapq.heappush(minq, (num, i))
            heapq.heappush(maxq, (-num, i))
            visited[i] = True
        elif num == -1:
            # 삭제연산 시, id를 기준으로 해당 노드가 다른 힙에서 삭제된 노드인지 체크
            # 이미 삭제된 노드일경우 삭제되지 않은 노드가 나올 때까지 버림
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            # 삭제 대상 노드가 등장하면 삭제
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)

        i += 1

    # 모든 연산이 끝난 후에도 쓰레기 노드들이 들어 있을 수 있어 비우기
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)

    if len(minq) == 0:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(maxq)[0], heapq.heappop(minq)[0]]

    return answer
