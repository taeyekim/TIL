# from collections import deque
#
# def is_prime(num):
#     if num == 2 or num == 3:
#         return True
#     for i in range(2, int(num**0.5 + 1)):
#         if num % i == 0:
#             return False
#     else:
#         return True
#
# N = int(input())
# prime_list = []
# cnt = 0
# for i in range(2, N//2+2):
#     if is_prime(i):
#         prime_list.append(i)
# total = 0
# for i in range(-1, len(prime_list) - 1):
#     total = 0
#     # t = []
#     for j in range(i+1, len(prime_list)):
#         total += prime_list[j]
#         # t.append(prime_list[j])
#         if total > N:
#             break
#         elif total == N:
#             cnt += 1
#             # print(t)
#             break
# if N == 3:
#     print(1)
# elif is_prime(N):
#     print(cnt + 1)
# else:
#     print(cnt)

# from collections import deque


# # 소수 판별 함수
# def is_prime(num):
#     if num < 2:
#         return False
#     if num in (2, 3):
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True
#
#
# # 연속된 소수의 합으로 표현될 수 있는 방법의 수를 찾는 함수
# def prime_sum_ways(N):
#     # 소수 리스트 생성
#     prime_list = [i for i in range(2, N + 1) if is_prime(i)]
#
#     count = 0  # 방법의 수
#     left, right = 0, 0  # 투 포인터 초기화
#     total = 0  # 현재 합계
#
#     # 투 포인터 알고리즘 적용
#     while True:
#         if total >= N:
#             total -= prime_list[left]
#             left += 1
#         else:
#             if right == len(prime_list):
#                 break
#             total += prime_list[right]
#             right += 1
#
#         if total == N:
#             count += 1
#
#     return count
#
#
# # 주어진 수 N에 대해 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 계산합니다.
# N = int(input())
# print(prime_sum_ways(N))

# from collections import deque
# import sys
#
# def bfs(pos):
#     q = deque()
#     visited = [[[False] * M for _ in range(N)] for _ in range(H)]
#     for height, sero, garo in pos:
#         q.append((height, sero, garo, 0))
#         visited[height][sero][garo] = True
#
#     while q:
#         h, y, x, cnt = q.popleft()
#         for dh, dy, dx in ((0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0)):
#             nh = h + dh
#             ny = y + dy
#             nx = x + dx
#             if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
#                 if not visited[nh][ny][nx] and tomato[nh][ny][nx] == 0:
#                     tomato[nh][ny][nx] = 1
#                     visited[nh][ny][nx] = True
#                     q.append((nh, ny, nx, cnt + 1))
#     else:
#         unripe_tomato_exists = any(tomato[h][n][m] == 0 for h in range(H) for n in range(N) for m in range(M))
#         if unripe_tomato_exists:
#             return -1
#         else:
#             return cnt
#
#
# M, N, H = map(int, sys.stdin.readline().split()) # M 가로, N 세로, H 상자 수
# tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
# position = []
# cnt = 0
# for n in range(N):
#     for m in range(M):
#         for h in range(H):
#             if tomato[h][n][m] == 1:
#                 position.append((h, n, m))
# answer = bfs(position)
# print(answer)

# N = int(input())
# lst = [0] * 10001
# for _ in range(N):
#     num = int(input())
#     lst[num] += 1
# for i in range(len(lst)):
#     if lst[i] >= 1:
#         for j in range(lst[i]):
#             print(i)
#
# from collections import deque
#
# def bfs(y1, x1, y2, x2):
#     q = deque()
#     q.append((y1, x1, 0))
#     lst[y1][x1] += 1
#     while q:
#         y, x, cnt = q.popleft()
#         if y == y2 and x == x2:
#             return cnt
#         for dy, dx in ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1)):
#             ny = y + dy
#             nx = x + dx
#             if 0 <= ny <= I-1 and 0 <= nx <= I-1 and lst[ny][nx] == 0:
#                 q.append((ny, nx, cnt+1))
#                 lst[ny][nx] = cnt
#     else:
#         return 0
#
# T = int(input()) # 테스트 케이스 개수
#
# for _ in range(T):
#     I = int(input()) # 한 변의 길이
#     lst = [[0] * I for _ in range(I)]
#     x1, y1 = map(int, input().split())
#     x2, y2 = map(int, input().split())
#     answer = bfs(y1, x1, y2, x2)
#     print(answer)

# A, B, V = map(int, input().split()) # 낮 A 미터, 밤 B미터, V미터 도달
# meter = A
# day = 1
# if A >= V:
#     day = 1
# else:
#     day = (V - A) // (A - B) + 1
#     if (V - A) % (A - B) > 0:
#         day += 1
# print(day)

# from collections import deque
#
# dy = [-1, 0, 0, 1]
# dx = [0, -1, 1, 0]
#
# def bfs(col, row):
#     q = deque()
#     q.append((col, row, 0))
#     size = 2
#     fish_cnt = 0
#     visited = [[False] * N for _ in range(N)]
#     visited[col][row] = True
#     check = 0
#     while q:
#         y, x, move = q.popleft()
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
#                 if lst[ny][nx] <= size and not visited[ny][nx]:
#                     q.append((ny, nx, move + 1))
#                     visited[ny][nx] = True
#
#                     if lst[ny][nx] != 0 and lst[ny][nx] <= size - 1:
#                         fish_cnt += 1
#                         lst[ny][nx] = 0
#                         visited = [[False] * N for _ in range(N)]
#                         visited[ny][nx] = True
#                         while q:
#                             q.popleft()
#                         q.append((ny, nx, move + 1))
#                         check = move + 1
#
#                         if fish_cnt == size:
#                             if size != 7:
#                                 fish_cnt = 0
#                                 size += 1
#                         print(
#                             f"check : {check}, ny : {ny}, nx : {nx}, move : {move + 1}, fish_cnt : {fish_cnt}, size = {size}, visited[{ny}][{nx}] : {visited[ny][nx]}")
#                         for j in range(N):
#                             print(lst[j], visited[j])
#                         print()
#                         break
#     else:
#         return 0 if check == 0 else check
#
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# fish_pos = [[] for _ in range(7)]
# print(fish_pos)
# for i in range(N):
#     for j in range(N):
#         if lst[i][j] == 9:
#             lst[i][j] = 0
#             col, row = i, j
#
# answer = bfs(col, row)
# print(answer)

# from collections import deque
#
# dy = [-1, 0, 0, 1]
# dx = [0, -1, 1, 0]
#
#
# def bfs(col, row, size):
#     q = deque([(col, row, 0)])  # 아기 상어의 위치와 이동 시간을 큐에 저장
#     visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장하는 배열
#     visited[col][row] = True  # 아기 상어의 위치 방문 처리
#     eatable_fishes = []  # 먹을 수 있는 물고기의 위치와 이동 시간을 저장하는 배열
#
#     while q:
#         y, x, move = q.popleft()
#
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             # 다음 위치가 범위 내에 있고 방문하지 않았으며 아기 상어가 지나갈 수 있는 칸인 경우
#             if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx] <= size:
#                 visited[ny][nx] = True  # 다음 위치 방문 처리
#                 q.append((ny, nx, move + 1))  # 큐에 다음 위치 추가
#                 # 다음 위치에 먹을 수 있는 물고기가 있는 경우
#                 if 0 < lst[ny][nx] < size:
#                     eatable_fishes.append((ny, nx, move + 1))  # 먹을 수 있는 물고기의 위치와 이동 시간 저장
#
#     # 먹을 수 있는 물고기가 있는 경우, 가장 가까운 물고기의 위치와 이동 시간 반환
#     if eatable_fishes:
#         eatable_fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # 이동 시간, 위쪽 위치, 왼쪽 위치 순으로 정렬
#         return eatable_fishes[0][0], eatable_fishes[0][1], eatable_fishes[0][2]
#     else:  # 먹을 수 있는 물고기가 없는 경우
#         return None, None, None
#
#
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         if lst[i][j] == 9:  # 아기 상어의 초기 위치
#             col, row = i, j
#             lst[i][j] = 0  # 아기 상어가 있는 위치는 빈 칸으로 변경
#
# time = 0  # 아기 상어가 물고기를 먹으며 이동한 총 시간
# ate_fishes = 0  # 아기 상어가 먹은 물고기의 수
# baby_shark_size = 2  # 아기 상어의 초기 크기
#
# while True:
#     # 아기 상어가 먹을 수 있는 물고기의 위치와 이동 시간을 구함
#     next_col, next_row, eat_time = bfs(col, row, baby_shark_size)
#
#     # 먹을 수 있는 물고기가 없는 경우 종료
#     if next_col is None:
#         break
#
#     # 아기 상어가 먹은 물고기의 수를 증가시키고, 아기 상어의 위치를 업데이트
#     ate_fishes += 1
#     time += eat_time
#     lst[next_col][next_row] = 0
#     col, row = next_col, next_row
#
#     # 아기 상어의 크기를 증가시키고, 먹은 물고기의 수가 아기 상어의 크기와 같아지면 크기 증가
#     if ate_fishes == baby_shark_size:
#         baby_shark_size += 1
#         ate_fishes = 0
#
# print(time)
s = 'abc'
while s:
    s = input()
    if s == '.':
        break
    st = []
    answer = 'yes'
    for c in s:
        # print(c, st)
        if c == '[':
            st.append('[')
        elif c == '(':
            st.append('(')

        if st:
            if c == ']':
                if c == st[-1]:
                    st.pop()
                else:
                    answer = 'no'
                    break
            elif c == ')':
                if c == st[-1]:
                    st.pop()
                else:
                    answer = 'no'
                    break
        else:
            if c == ']' or c == ')':
                answer = 'no'
                break

    print(answer)
