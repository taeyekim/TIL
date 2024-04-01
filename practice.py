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

# S = input()

# arr = [-1] * 26

# for s in S:
#     if arr[ord(s) - ord('a')] == -1:
#         arr[ord(s) - ord('a')] = S.index(s)
# print(*arr)


# def bfs(root):
# import sys
# from collections import deque
#
# # 입력 함수를 빠른 sys.stdin.readline으로 변경
# input = sys.stdin.readline
#
# dx = [0, 0, 1, -1, 1, 1, -1, -1]
# dy = [1, -1, 0, 0, 1, -1, -1, 1]
#
# def bfs(row, col):
#     deq = deque()
#     jido[row][col] = 0
#     deq.append((row, col))
#     while deq:
#         x, y = deq.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
#                 if jido[nx][ny] == 1:
#                     deq.append((nx,ny))
#                     jido[nx][ny] = 0
#
# while True:
#
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     jido = [list(map(int, input().split())) for _ in range(h)]
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if jido[i][j] == 1:
#                 bfs(i, j)
#                 cnt += 1
#     print(cnt)

import sys
from collections import deque

# 입력 함수를 빠른 sys.stdin.readline으로 변경
# input = sys.stdin.readline

# def bfs(row, col):
#     lst = []
#     lst.append((row, col))
#     visited = [[0] * M for _ in range(N)]
#     visited[row][col] = True
#
#     while lst:
#         x, y = lst.pop(0)
#         for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
#                 if tomato[nx][ny] == 0 and visited[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     lst.append((nx, ny))
#
# M, N = map(int, input().split())
#
# tomato = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             bfs(i, j)
# for i in range(N):
#     if tomato[i].count(0) + tomato[i].count(-1) >= 1:
#         answer = -1
# for i in range(N):
#     if answer != -1 and answer >= max(tomato[i]):
#         answer = max(tomato[i])
# print(answer)

# 주어진 입력값
# K, N = map(int, input().split())
# lengths = []
# for i in range(K):
#     lengths.append(int(input()))
#
# # 이진 검색을 이용한 랜선 자르기
# def find_max_length(K, N, lengths):
#     start, end = 1, max(lengths) # 시작 길이와 끝 길이 설정
#
#     while start <= end:
#         mid = (start + end) // 2 # 중간 길이
#         num_cables = sum(length // mid for length in lengths) # 중간 길이로 잘랐을 때 만들 수 있는 랜선 개수
#
#         # 만들어진 랜선의 개수가 목표 개수보다 많거나 같다면, 더 긴 길이 탐색
#         if num_cables >= N:
#             start = mid + 1
#         else: # 만들어진 랜선의 개수가 목표 개수보다 적다면, 더 짧은 길이 탐색
#             end = mid - 1
#
#     return end # 최대 길이 반환
#
# answer = find_max_length(K, N, lengths)
# print(answer)

# dfs 출력, bfs 출력

# from collections import deque
# def dfs(s):
#     global visit
#     st = []
#     st.append(s)
#     visit[s] = True
#
#     while st:
#         v = st.pop()
#         print(v, end = ' ')
#         for w in sorted(G[v]):
#             if not visit[w]:
#                 dfs(w)
#
# def bfs(s):
#     q = deque()
#     q.append(s)
#     visited = [False] *(N + 1)
#     visited[s] = True
#     while q:
#         v = q.popleft()
#         print(v, end=' ')
#         for w in sorted(G[v]):
#             if not visited[w]:
#                 q.append(w)
#                 visited[w] = True
#
# N, M, V = map(int, input().split()) # 노드(정점) N, 간선 M, 정점 번호 V 4, 5, 1
#
# A = []
# G = [[] for _ in range(N+1)]
# for _ in range(M):
#     A.append(list(map(int, input().split())))
#
# for i in range((len(A))): # [[1,2], [1,3] .. [3,4]] / 첫 스타트 [1,2]
#     G[A[i][0]].append(A[i][1])
#     G[A[i][1]].append(A[i][0])
#
# visit = [False] * (N + 1)
# dfs(V)
# print()
# bfs(V)

# # 1 익은 토마토, 0 익지 않은 토마토, -1 토마토 없는 칸
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# from collections import deque
# def bfs(pos):
#     # global day
#     q = deque()
#     for ele in pos:
#         q.append(ele + [tomato[ele[0]][ele[1]]])
#     # visited = list([0] * M for _ in range(N))
#     # visited[x][y] = day
#     while q:
#         v = q.popleft()
#         # day += 1
#         for i in range(4):
#             nx = v[0] + dx[i]
#             ny = v[1] + dy[i]
#             if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
#                 if tomato[nx][ny] == 0:
#                     tomato[nx][ny] = tomato[v[0]][v[1]] + 1
#                     q.append([nx, ny, tomato[v[0]][v[1]] + 1])
#         # for i in range(N):
#         #     print(tomato[i])
#         # print()
#
# M, N = map(int, input().split()) # 가로 M, 세로 N
#
# tomato = [list(map(int, (input().split()))) for _ in range(N)]
# bp = False
# day = 0
# pos = []
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             pos.append([i, j])
#
# bfs(pos)
#
# answer = 0
# for i in range(N):
#     answer = max(answer, max(tomato[i]))
#     if tomato[i].count(0) >= 1:
#         answer = -1
#         break
# if answer == -1:
#     print(-1)
# else:
#     print(answer - 1)

# def bfs(r,c):
#     #공기일떄만 q 에 넣기
#     while q :
#         vr, vc =  q.popleft()
#
#         for dr, dc in [(상)(하)(좌)(우)]:
#             nr =
#             nc =
#             if 범위 and not visited:
#                 if 새로 갈 곳이 0이면
#                 큐에 넣기
#                 방문처리 하기
#                 if 새로 갈 곳이 1이면
#                 값을 0으로 바꿔주기
#                 녹는 치즈 카운트+1
#                 방문처리 하기
# cnt = 1
# time = 0
# while True:
#     if cnt == 0:
#         print(time)
#         print(cnt)
#         break
#     cnt = 0
#     for r in range():
#         for c in range():
#             if arr[r][c] == 0:
#                 cnt = bfs(r, c)
#     time += 1
# print()
# from collections import deque
#
# def melt_cheese():
#     q = deque([(0, 0)])  # 판의 가장자리에서 시작
#     visited = [[False] * row for _ in range(col)]
#     melt_list = []  # 이번 단계에서 녹을 치즈의 위치를 저장
#
#     while q:
#         y, x = q.popleft()
#         for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < row and 0 <= ny < col and not visited[ny][nx]:
#                 if lst[ny][nx] == 1:
#                     melt_list.append((ny, nx))  # 외부 공기에 접촉한 치즈 저장
#                 elif lst[ny][nx] == 0:
#                     q.append((ny, nx))
#                 visited[ny][nx] = True
#
#     # 외부 공기에 접촉한 치즈 녹이기
#     for y, x in melt_list:
#         lst[y][x] = 0
#
#     return len(melt_list)  # 이번 단계에서 녹은 치즈의 수 반환
#
# col, row = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(col)]
# time = 0
# last_melt = 0
#
# =======
# <<<<<<< HEAD
# def is_prime(num):
#     if num == 1:
#         return 0
#     elif num == 2 or num == 3:
#         return 1
#     else:
#         for i in range(2,num//2 + 1):
#             if num % i == 0:
#                 return 0
#         else:
#             return 1
#
# N = int(input())
# cnt = 0
# arr = list(map(int, input().split()))
# for num in arr:
#     cnt += is_prime(num)
# print(cnt)
# =======
# >>>>>>> 3cd294d36fe0f3e24ead3cc557f58dda18f273ce
# while True:
#     melted = melt_cheese()
#     if melted == 0:
#         break
# <<<<<<< HEAD
#     last_melt = melted
#     time += 1
#
# print(time)
# print(last_melt)
#
# =======
#     if A % B == 0:
#         ans = 'multiple'
#     elif B % A == 0:
#         ans = 'factor'
#     else:
#         ans = 'neither'
#     print(ans)
# >>>>>>> 0fb25dd544851fd297f9a449c44cd10a18de493f
# >>>>>>> 3cd294d36fe0f3e24ead3cc557f58dda18f273ce
from collections import deque

# def find_closest_sum(cards, N, M, start, depth, current_sum):
#     global max_sum
#
#     if depth == 3:
#         if current_sum <= M:
#             max_sum = max(max_sum, current_sum)
#         return
#
#     if start >= N:
#         return
#
#     find_closest_sum(cards, N, M, start + 1, depth + 1, current_sum + cards[start])
#     find_closest_sum(cards, N, M, start + 1, depth, current_sum)
#
#
# N, M = map(int, input().split())
#
# cards = list(map(int, input().split()))
#
# max_sum = 0
# find_closest_sum(cards, N, M, 0, 0, 0)
#
# print(max_sum)

T = int(input())

for _ in range(T):
    s = input()
    ST = []
    for c in s:
        if