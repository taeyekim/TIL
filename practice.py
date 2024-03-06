# def bfs(stR, stC):
#     Q = []
#     visited = [[False] * N for _ in range(N)]
#     direction = [(0,1), (0,-1), (1, 0), (-1, 0)]
#
#     Q.append((stR, stC))
#     visited[stR][stC] = True
#
#     while Q:
#         vR, vC = Q.pop(0)
#         for dr, dc in direction:
#             wR = vR + dr
#             wC = vC + dc
#
#             if 0 <= wR < N and 0 <= wC < N:
#                 if arr[wR][wC] == 3:
#                     return 1
#
#                 if arr[wR][wC] == 0 and not visited[wR][wC]:
#                     Q.append((wR, wC))
#                     visited[wR][wC] = True
#
#     return 0
#
#
# T = 10
# for _ in range(1, T+1):
#     tc = int(input())
#     N = 16
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     for row in range(N):
#         for col in range(N):
#             if arr[row][col] == 2:
#                 stR = row
#                 stC = col
#                 break
#
#     print(f'#{tc} {bfs(stR, stC)}')

while True:
    a, b = map(int,input().split())
    if (a, b) == (0, 0):
        break
    print(a+b)