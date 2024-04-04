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

from collections import deque


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

from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(col, row):
    cnt = 1
    q = deque()
    q.append((col,row))
    painting[col][row] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx <= m - 1 and 0 <= ny <= n-1 and painting[ny][nx] == 1:
                painting[ny][nx] = 0
                cnt += 1
        return cnt

n, m = map(int, input().split())

painting = [list(map(int, input().split())) for _ in range(n)]

painting_cnt = 0
answer = 0
for y in range(n):
    for x in range(m):
        if painting[y][x] == 1:
            painting_cnt += 1
            total = bfs(y, x)
            answer = max(answer, total)
print(painting_cnt)
print(answer)