# 4615. 재미있는 오셀로 게임

# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [[0] * N for _ in range(N)] # 흑 = 1, 백 2
#     arr[N//2][N//2] = 2
#     arr[N//2-1][N//2-1] = 2
#     arr[N//2][N//2-1] = 1
#     arr[N//2-1][N//2] = 1
#
#     dr = [0, -1, 0, 1, 1, -1, 1, -1]
#     dc = [1, 0, -1, 0, 1, -1, -1, 1]
#     for _ in range(M):
#         y, x, dol = map(int, input().split())
#         x_pos, y_pos = x-1, y-1
#         arr[x_pos][y_pos] = dol
#         dol_r = 2 if dol == 1 else 1
#         print()
#         for i in range(N):
#             for j in range(N):
#                 print(arr[i][j], end='')
#             print()
#         print()
#         for i in range(8):
#             nr = x_pos + dr[i]
#             nc = y_pos + dc[i]
#             while 0 <= nr <= N-1 and 0 <= nc <= N-1 and arr[nr][nc] == dol_r:
#                 nr += dr[i]
#                 nc += dc[i]
#             if 0 <= nr <= N-1 and 0 <= nc <= N-1 and arr[nr][nc] == dol:
#                 nr -= dr[i]
#                 nc -= dr[i]
#                 while 0 <= nr <= N-1 and 0 <= nc <= N-1 and arr[nr][nc] == dol_r:
#                     arr[nr][nc] = dol
#                     nr -= dr[i]
#                     nc -= dr[i]
#         print()
#         for i in range(N):
#             for j in range(N):
#                 print(arr[i][j], end='')
#             print()
#         print()
#
#     sum_black = 0
#     sum_white = 0
#     for c in arr:
#         sum_black += c.count(1)
#         sum_white += c.count(2)
#     print(f"#{tc} {sum_black} {sum_white}")

# 명령갯수 만큼 반복
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ARR = [[0] * N for _ in range(N)]  # 흑 = 1, 백 2
    ARR[N//2][N//2] = 2
    ARR[N//2-1][N//2-1] = 2
    ARR[N//2][N//2-1] = 1
    ARR[N//2-1][N//2] = 1

    for _ in range(M):
        col, row, color = map(int, input().split())
        row -= 1
        col -= 1

        if color == 2:
            color_r = 1
        else:
            color_r = 2

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            newR = row + dr
            newC = col + dc
            # 범위 비교, 값 비교(나하고 다른 색인 동안): # == color_r
            while 0 <= newR < N and 0 <= newC < N and ARR[newR][newC] == color_r: # 지금 나온 색 == color_r
                newR += dr
                newC += dc

            # 값을 찾아서 나온 경우
            if 0 <= newR < N and 0 <= newC < N and ARR[newR][newC] == color:
                # 원래 좌표까지 색을 바꾼다. 역방향으로

                # while not (newR == row and newC == col):
                while newR != row or newC != col:
                    newR -= dr
                    newC -= dc
                    ARR[newR][newC] = color

    sum_black = 0
    sum_white = 0
    for c in ARR:
        sum_black += c.count(1)
        sum_white += c.count(2)
    print(f"#{tc} {sum_black} {sum_white}")

