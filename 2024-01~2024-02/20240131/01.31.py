# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# arr2 = [[0]*N for _ in range(N)]
# print(arr2)

# arr3 = [[0]*N]*N
# arr3[0][0] = 1

# print(arr3)

# # j행의 좌표
# # j열의 좌표
# for i in range(n) :
#     for j in range(m):
#         f(array[i][j])



# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 5
# for i in range(N) :
#     for j in range(N) :
#         for k in range(4) :
#             ni = i + di[k]
#             nj = j + dj[k]
#             print((ni, nj), end = ' ')
#         print()


# i = 3
# j = 4
# # for k in range(4) :
# #     ni = i + di[k]
# #     nj = j + dj[k]
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 5
# arr = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj])



# # 부분집합 생성하기
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit)


# # 원소의 갯수가 나오지 않더라도 사용할 수 있는 부분집합 생성 코드
# N = 5
# arr = [1, 2, 3, 4, 5]

# for i in range(1 << N):
#     for j in range(N):
#         if i & (1 << j):
#             print(arr[j], end=' ')
#     print()
#
# # 부분집합의 합을 출력하고자 할 때
# N = 3
# arr = [1, 2, 3]
# s = 0
# for i in range(1 << N):
#     for j in range(N):
#         if i & (1 << j):
#             s += arr[j]
#             print(arr[j], end=' ')
#
#     print(s)


# N = int(input())
# arr = list(map(int,input().split()))
# def f(arr, N):
#     for i in range(1, 1 << N) :
#         s = 0
#         for j in range(N):
#             if i & (1 << j):
#                 s += arr[j]
#         if s == 0:
#             return True
#     return False

# arr = [1, 2, 3] => arr[0], arr[1], arr[2]
#
# arr = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# => arr[0]=> [1, 2, 1]=> arr[0][0], arr[0][1], arr[0][3]]



# N = 3
# M = 4
# arr =  [[1, 1, 1, 10],
#         [2, 2, 2, 20],
#         [3, 3, 3, 30]]
#
# for row in range(N):
#     sumV = 0
#     for col in range(M):
#         print(arr[row][col])
#         sumV += arr[row][col]
#
#     if maxV < sumV:
#         maxV =sumV
#
# print(maxV)
#
# # 전체의 합 구하기
# sumV = 0
# for row in range(N):
#     for col in range(M):
#         print(arr[row][col])
#         sumV += arr[row][col]



# N = 3
# M = 4
# arr =  [[1, 1, 1, 10],
#         [2, 2, 2, 20],
#         [3, 3, 3, 30]]
# sumV = 0
# for col in range(M):
#     sumV = 0
#     for row in range(N):
#         sumV += arr[row][col]
#     print(sumV)


#  연습문제
# N = 5
# arr = [[1, 1, 1, 10, 1],
#        [2, 2, 2, 20, 1],
#        [3, 3, 3, 30, 1],
#        [3, 3, 3, 30, 1],
#        [3, 3, 3, 30, 1]]
#
# sumV = 0
# # 정방향
# for i in range(N):
#     sumV += arr[i][i]
# # 역방향
# # sumV = 0
# for i in range(N):
#     sumV += arr[i][N-1-i]
# sumV = sumV - arr[N//2][N//2]
#
#
# # 방향 구하기
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# for d in range(4) :
#     newR = row + dr[d]
#     newC = col + dr[d]
#     print(newR, newC)
#
#
# # 같은 것 다른 방법 (방향정해져있고, 그 방향 다 봐야할 때)
# for d in range[(-1, 0)(1, 0)(0, -1)(0, 1)]:
#     newR = row + dr[d]
#     newC = col + dr[d]
#     print(newR, newC)
#
# #   순서가 정해져있는 경우
# # 전체 다 보는 코드
# def myAbs(n):
#     if n > 0:
#         return n
#     return -n
# sumV = 0
# for row in range(N):
#     for col in range(N):
#         # print(row, col, arr[row][col])
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#
#         for d in range(4):
#             newR = row + dr[d]
#             newC = col + dr[d]
#             if 0<=newR<N and 0<=newC<N:
#                 t = myAbs(arr[row][col] - arr[newR][newC])
#              sumV += t
#
# print(sumV)
#
#
# # 부분집합
# numbers = [10, 11, 12]
#
# for i in [0, 1]: # range(1)
#     for j in [0, 1]:
#         for k in [0, 1]:
#
#
#             print('{', end = ' ')
#             if i ==1:
#                 print(numbers[0], end = ' ')
#             if j ==1:
#                 print(numbers[1], end = ' ')
#             if k == 1:
#                 print(numbers[2], end = ' ')
#
#             print('}')



numbers = [10, 11, 12, 2] # 000(0), 001(1), 010(2), 111(7)---1111(15)
N=4
# print(3, bin(3))

for i in range(2**N): #=> 8==2**3==1000(1<<3)
    print(i, end='=>')
# 비트마스킹에 1만 원본의 값을 뽑아주고 0이 있는 경우에는 0

    for j in range(N):
        # t = i & (1<<j)
        if i & (1<<j):
            print(numbers[j], end=' ')
        # else:

        # i의 0번째를 확인해서 1이면
        # else:
        #     pass

    print()

# 0101 = {10 12}

# i = 14
# i = 0b 1110
#      & 0001 (1<<0)
#  ======== 0001/0000
#  1100
# &0010 (1<<1)
#  ======== 0010/0000
#   1110
#   &0100(1<<2)
#   ======= 0100/0000



