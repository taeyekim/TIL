# # 1979. 어디에 단어가 들어갈 수 있을까

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
#     N += 1 # 0인 열과 행 추가[0]*(N+1)
#     # 가로, 세로로 연속한 1의 개수가 K인 경우의 수
#     ans = 0
#     print(arr)
#     for i in range(N+1):
#         cnt = 0 # i행에서 연속한 1의 개수
#         for j in range(N+1):
#             if arr[i][j]:
#                 cnt += 1
#             else:   # arr[i][j]==0 이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0

#     for j in range(N+1):
#         cnt = 0 # j열에서 연속한 1의 개수
#         for i in range(N+1):
#             if arr[i][j]:
#                 cnt += 1
#             else:   # arr[i][j]==0 이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     print(f'#{tc} {ans}')
# K = 3
# N = 6
# arr = [0, 1, 0, 1, 1, 1]
# ans = 0
# cnt = 0
# for i in range(N):
#     if arr[i] == 0:
#         if cnt == K:
#             ans += 1
#         cnt = 0
#     else:   # arr[i] == 1
#         cnt += 1
#         if i==N-1 and cnt==K:
#             if cnt == K:
#                 ans += 1
#
# print(ans)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    total_cnt = 0
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total_cnt += 1
                cnt = 0
                
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    total_cnt += 1
                cnt = 0
    print(f"#{tc} {total_cnt}")