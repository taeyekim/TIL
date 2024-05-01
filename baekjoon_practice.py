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
#
# def bfs(N, K):
#     q = deque()
#     q.append((N, 0))
#     visited = [False] * 100001
#     visited[N] == True
#     while q:
#         pos, time = q.popleft()
#         if pos == K:
#             return time
#
#         next_pos = pos * 2
#         if 0 <= next_pos <= 100000 and not visited[next_pos]:
#             q.append((next_pos, time + 1))
#             visited[next_pos] = True
#
#         for c in (pos-1, pos+1):
#             if 0 <= c <= 100000 and not visited[c]:
#                 q.append((c, time + 1))
#                 visited[c] = True
#
# # 수빈 위치 N, 동생 위치 K
# N, K = map(int, input().split())
# cnt = 0
# answer = bfs(N, K)
# print(answer)

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
#         # if lst[i][j] == 1:
#         #     fish_pos[1].append([i, j])
#         # elif lst[i][j] == 2:
#         #     fish_pos[2].append([i, j])
#         # elif lst[i][j] == 3:
#         #     fish_pos[3].append([i, j])
#         # elif lst[i][j] == 4:
#         #     fish_pos[4].append([i, j])
#         # elif lst[i][j] == 5:
#         #     fish_pos[5].append([i, j])
#         # elif lst[i][j] == 6:
#         #     fish_pos[6].append([i, j])
#
# answer = bfs(col, row)
# print(answer)

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
#
# s = 'abc'
# while s:
#     s = input()
#     if s == '.':
#         break
#     st = []
#     answer = 'yes'
#     for c in s:
#         # print(c, st)
#         if c == '[':
#             st.append('[')
#         elif c == '(':
#             st.append('(')
#
#         if st:
#             if c == ']':
#                 if c == st[-1]:
#                     st.pop()
#                 else:
#                     answer = 'no'
#                     break
#             elif c == ')':
#                 if c == st[-1]:
#                     st.pop()
#                 else:
#                     answer = 'no'
#                     break
#         else:
#             if c == ']' or c == ')':
#                 answer = 'no'
#                 break
#
#     print(answer)

<<<<<<< HEAD
<<<<<<< HEAD
N, M, B = map(int, input().split()) # N 개의 줄, M개의 가로, B개의 블록 보유

arr = [list(map(int, input().split())) for _ in range(N)]

=======
def solve(s_lev, e_lev, lst):
    # 변수 초기화
    blocks_needed = 0
    blocks_removed = 0
    add_time = 0
    remove_time = 0
=======
# def solve(s_lev, e_lev, lst):
#     # 변수 초기화
#     blocks_needed = 0
#     blocks_removed = 0
#     add_time = 0
#     remove_time = 0
#
#     # 초기 높이 설정 계산
#     for c in range(N):
#         for r in range(M):
#             diff = s_lev - lst[c][r]
#             if diff > 0:
#                 blocks_needed += diff
#                 add_time += diff
#             else:
#                 blocks_removed += -diff
#                 remove_time += -diff * 2
#
#     ans_level = s_lev
#     ans_time = add_time + remove_time
#
#     # 각 높이별 시간과 블록 수 조정
#     for level in range(s_lev + 1, e_lev + 1):
#         have_blocks = B
#         t = 0
#         for c in range(N):
#             for r in range(M):
#                 diff_d = level - lst[c][r]
#                 if diff_d > 0:
#                     t += diff_d
#                     have_blocks -= diff_d
#                 elif diff_d < 0:
#                     diff_d = -diff_d
#                     t += diff_d * 2
#                     have_blocks += diff_d
#
#         if have_blocks < 0:
#             continue
#         ans_time = min(t, ans_time)
#         if ans_time == t:
#             ans_level = level
#     return ans_time, ans_level
#
# N, M, B = map(int, input().split()) # 세로 N, 가로 M, 인벤토리 블록 수
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# start_num = 256
# end_num = 0
# for i in range(N):
#     for j in range(M):
#         start_num = min(arr[i][j], start_num)
#         end_num = max(arr[i][j], end_num)
# time, lev = solve(start_num, end_num, arr)
# print(time, lev)
>>>>>>> 1b4ce4fb763ece900b6d2c33e0531fb1be23e8d0

import turtle
import random

# 가정: 학생들의 이름이 주어졌다고 가정
students = ['구혜인', '김여준', '김태연', '박민철', '유지연', '최민규',
            '최은경', '한세훈', '강두홍', '김민영', '박지응', '서규범',
            '윤성준', '이예지', '전가현', '정금열', '정남용', '김성은',
            '서민수', '이정준', '최승필', '이주호', 'NULL', 'NULL']

# 학생 이름을 랜덤하게 배치
random_students = random.sample(students, len(students))

# 6x4 배열 생성
numbers = [['' for _ in range(7)] for _ in range(4)]

# 배치된 학생 이름을 numbers 배열에 할당
student_index = 0
for row in range(4):
    for col in range(7):
        if col != 3:  # 네 번째 열은 복도
            numbers[row][col] = random_students[student_index]
            student_index += 1

<<<<<<< HEAD
arr = [list(map(int, input().split())) for _ in range(N)]
start_num = 256
end_num = 0
for i in range(N):
    for j in range(M):
        start_num = min(arr[i][j], start_num)
        end_num = max(arr[i][j], end_num)
time, lev = solve(start_num, end_num, arr)
print(time, lev)
>>>>>>> 7e7aa09c649293d00efdc202c039f72c84b41ee3
=======
# Turtle 그래픽을 사용하여 자리 배치도를 그리는 함수
def draw_seating_chart_corrected():
    # Turtle 환경 설정
    screen = turtle.Screen()
    screen.setup(width=1000, height=650)  # 창의 크기를 더 크게 조정
    t = turtle.Turtle()
    t.speed(0)

    # 사각형 그리기 함수
    def draw_square(x, y, name):
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(70)  # 사각형 크기 증가
            t.right(90)
        t.penup()
        t.goto(x + 35, y - 45)  # 글자 위치 조정
        if name == 'NULL':  # NULL 값일 경우 빨간색으로 설정
            t.pencolor("red")
        else:
            t.pencolor("black")
        t.write(name, align="center", font=("Arial", 10, "normal"))  # 글자 크기 조정
        t.pencolor("black")

    start_x, start_y = -300, 200  # 시작 위치 조정
    # 자리 그리기
    for i, row in enumerate(numbers):
        for j, name in enumerate(row):
            if name:  # 빈 칸이 아니면 그린다.
                x = start_x + j * 80  # 각 칸 사이 간격 증가
                y = start_y - i * 80  # 각 칸 사이 간격 증가
                draw_square(x, y, name)

    t.hideturtle()
    screen.mainloop()

draw_seating_chart_corrected()
>>>>>>> 1b4ce4fb763ece900b6d2c33e0531fb1be23e8d0
