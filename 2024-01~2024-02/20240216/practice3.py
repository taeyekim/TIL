'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(s):
    ST = []
    visited = [False] * (N+1)

    ST.append(s)
    visited[s] = True
    while ST:
        v = ST.pop(-1)
        print(v)

        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True

# def bfs(s): # 거리 개념
#     Q = []
#     visited = [0] * (N+1)
#
#     Q.append(s)
#     visited[s] = 1
#     while Q:
#         v = Q.pop(0)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = visited[v] + 1
#     print(visited)

def bfs(s):
    Q = []
    visited = [0] * (N+1)

    Q.append((s, 1))
    visited[s] = True
    while Q:
        v, d = Q.pop(0)
        print(v, d)

        for w in G[v]:
            if G[v][w] == 1 and not visited[w]:
                Q.append((w, d+1))
                visited[w] = True

N, E = map(int, input().split())
lst = list(map(int, input().split()))

# G = [[] for _ in range(N+1)]
# for i in range(0, len(lst), 2):
#     v1 = lst[i]
#     v2 = lst[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1) # 양방향 그래프
'''
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
'''
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1][v2] = 1
    G[v2][v1] = 1 # 양방향 그래프

# print(G)
bfs(1)
print(G)
# dfs(1)

