#쌤코드
def recu(row, col, midSum) :
    global minV

    if row == N-1 and col == N-1 :
        print(path)
        print(midSum)
        # sumV = sum(path)
        # if minV > sumV :
        #     minV = sumV

    if col+1 < N :
        path.append((row, col+1, arr[row][col+1]))
        recu(row, col+1, midSum+arr[row][col+1])
        path.pop()

    if row+1 < N :
        path.append((row+1, col, arr[row+1][col]))
        recu(row+1, col, midSum+arr[row+1][col])
        path.pop()


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    minV = 10*N
    recu(0,0,arr[0][0])

#전체 다 나오는 거
# def recu(row, col, midSum) :
#     global minV
#     path.append((row,col))
#     if row == N-1 and col == N-1 :
#         print(path)
#         print(midSum)
#
#     if col+1 < N :
#         recu(row, col+1, midSum+arr[row][col+1])
#
#     if row+1 < N :
#         recu(row+1, col, midSum+arr[row+1][col])

#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     path = []
#     minV = 10*N
#     recu(0,0,arr[0][0])