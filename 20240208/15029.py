# 15029. 4871 그래프 경로

# N = 7 # 1 ~ 7
# E = len(l)
# G = [[] for _ in range(N+1)]
#
# for i in range():
#     v1, v2 = input().split()
#     G[v1].append(v2)
#     G[v2].append(v1)
#
# print(G)
# dfs(5)

def dfs(start, end):
    stack = []
    visited = [False] * (len(Graph) + 1)
    stack.append(start)
    visited[start] = True
    while stack:
        v = stack.pop()
        if v == end:
            return 1
        for w in Graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
    
    return 0

T = int(input()) # 테스트 케이스의 개수 입력
for case in range(1, T + 1):
    V, E = map(int, input().split()) # 노드의 개수와 간선의 개수 입력
    Graph = [[] for _ in range(V + 1)] # 그래프 초기화

    # 간선 정보 입력
    for _ in range(E):
        v1, v2 = map(int, input().split())
        Graph[v1].append(v2)
        Graph[v2].append(v1)

    S, G = map(int, input().split()) # 출발 노드와 도착 노드 입력

    result = dfs(S, G) # DFS를 통해 경로 존재 여부 확인
    print("#{} {}".format(case, result)) # 결과 출력

