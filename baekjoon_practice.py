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

def bfs(N, K):
    q = deque()
    q.append((N, 0))
    visited = [False] * 100001
    visited[N] == True
    while q:
        pos, time = q.popleft()
        if pos == K:
            return time

        next_pos = pos * 2
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            q.append((next_pos, time + 1))
            visited[next_pos] = True

        for c in (pos-1, pos+1):
            if 0 <= c <= 100000 and not visited[c]:
                q.append((c, time + 1))
                visited[c] = True

# 수빈 위치 N, 동생 위치 K
N, K = map(int, input().split())
cnt = 0
answer = bfs(N, K)
print(answer)
