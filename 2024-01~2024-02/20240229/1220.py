# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(input().split()) for _ in range(N)]
#
#     cnt = 0
#     for j in range(N):
#         is_n = False
#         is_s = False
#         for i in range(N):
#             if arr[i][j] == '1':
#                 is_n = True
#             if is_n:
#                 if arr[i][j] == '2':
#                     cnt += 1
#                     is_n = False
#
#             if arr[i][j] == '2':
#                 is_s = True
#
#     print(f'#{tc} {cnt}')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 1은 S극(아래)에 끌림, 2는 N극(위)에 끌림
    cnt = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if flag == False and arr[i][j] == 2:
                flag = False

            if arr[i][j] == 1 and flag == False:
                flag = True

            if flag and arr[i][j] == 2:
                flag = False
                cnt += 1

    print(f"#{tc} {cnt}")