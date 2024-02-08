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

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    S, G = map(int, input().split())

