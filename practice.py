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

<<<<<<< HEAD
def is_prime(num):
    if num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1
    else:
        for i in range(2,num//2 + 1):
            if num % i == 0:
                return 0
        else:
            return 1

N = int(input())
cnt = 0
arr = list(map(int, input().split()))
for num in arr:
    cnt += is_prime(num)
print(cnt)
=======
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A % B == 0:
        ans = 'multiple'
    elif B % A == 0:
        ans = 'factor'
    else:
        ans = 'neither'
    print(ans)
>>>>>>> 0fb25dd544851fd297f9a449c44cd10a18de493f
