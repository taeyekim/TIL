'''
V E : V 1 ~ V번까지 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, N, G):  # 시작정점 s, 노드개수 N
    q = []  # 큐 생성
    visited = [0] * (N + 1)  # visited
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 처리안한 정점이 남아있으면
        t = q.pop(0)  # 처리할 정점 디큐
        if t == G:
            return visited[t] - 1  # 시작점이 1부터이기 때문에 간선수를 계산(몇개의 간선 지나가는지)하고자하면 1을 빼기 (최단경로 간선 수)
        for i in adjl[t]:  # t에 인접인 정점i (내가 찾는 경로가 아니면)
            if visited[i] == 0:  # 방문하지 않은 정점이면
                q.append(i)  # 인큐
                visited[i] = visited[t] + 1  # 방문표시
    return 0  # 0까지 경로가 없는 경우

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)  # 무향그래프(방향이 없음 -> 2개가 인접되어있다고 이야기하고자함)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')