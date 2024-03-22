# 1238. [S/W 문제해결 기본] 10일차 - Contact

# 1. 자료구조
# - 그래프(인접행렬, 인접리스트)
#
# 2. 알고리즘
# - BFS
#     - 문제를 보니 노드 탐색 : BFS 알고리즘이
#     - 추가로 뭔가 동작을 해야하네...??
#     - N번 만에 해당 노드를 탐색했다. (level, depth)
#     - 마지막 level에서 숫자가 가장 큰 노드
#     - flood fill
#     - 시간 복잡도, 공간 복잡도
#
# BFS의 시간 복잡도
# - 계산하는 방법 : 얼마나 방문을 할 수 있을까?
# -> 노드의 수(V)가 최대 100개
# -> 간선의 수(E) => O(V+E)(인접 리스트 기준)

import sys
sys.stdin = open("input.txt", "r")

def bfs(start):
    q = [start]
    visited = [0] * 101
    visited[start] = 1

    max_number = start
    max_depth = 1

    while q:
        now = q.pop(0)

        # 갈 수 있는 곳들
        for to in graph[now]:
            # 이미 방문했다면 pass
            if visited[to]:
                continue

            # 현재 방문 = 이전 방문 + 1 번만에 왔다.
            visited[to] = visited[now] + 1

            # depth 가 더 깊어졌네 ? ==> max_number 초기화
            # depth 는 같은데 숫자가 더 크네 => 초기화
            if max_depth < visited[to] or \
                    (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to

            q.append(to)

    return max_number


for tc in range(1, 11):
    N, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    # 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i + 1]
        graph[s].append(e)

    r = bfs(start)
    print(f'#{tc} {r}')