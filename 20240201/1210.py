# T = int(input())
#
# for tc in range(1, T+1):
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#
#     d = "up"
#
#     for col in range(100):
#         if arr[99][col] == 2:
#             break
#     print(f"col : {col}")
#     for row in range(98, -1, -1):
#         print(row)
#         if arr[row][col - 1] and d == "up":
#             while arr[row][col - 1]:
#                 col -= 1
#                 d = "left"
#         elif arr[row][col + 1] and d == "up":
#             while arr[row][col + 1]:
#                 col += 1
#                 d = "right"
#         else:
#             if row == 0:
#                 break
#
#     print(f"#{tc} {col}")
#

for tc in range(1, 11):
    T = int(input())
    N = 100
    LADDER = [list(map(int, input().split())) for _ in range(N)]

    #1 99row에서 2의 위치를 찾아라
    for col in range(N):
        if LADDER[99][col] == 2:
            # print("in")
            break

    #2. 위로 한칸씩 이동하면서
    for row in range(98, -1, -1):
        # 2-1 col의 왼쪽에 1이 있는지 확인
        if col > 0 and LADDER[row][col-1]:
            while col > 0 and LADDER[row][col-1]:
                col -= 1
        # 2-2 col의 오른쪽에 1이 있는지 확인
        elif col < N-1 and LADDER[row][col+1]:
            while col < N-1 and LADDER[row][col+1]:
                col += 1

    print(f"\n#{T} {col}")

