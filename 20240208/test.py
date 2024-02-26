# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# l = list(map(int, s.split()))

# def dfs(s):
#     ST = []
#     visited = [False] * (N+1)
#     ST.append(s)
#     visited[s] = True
#     while ST:
#         v = ST.pop()
#         print(v)

#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[w] = True

# N = 7 # 1~7
# E = len(l)
# G = [[] for _ in range(N+1)]

# for i in range(0, E, 2):
#     v1 = l[i]
#     v2 = l[i+1]
#     G[v1].append(v2)
#     G[v2].append(v1)

# print(G)
# dfs(5)

