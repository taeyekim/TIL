# N = int(input())
#
# arr = [[0] * 7 for _ in range(2)]
# for j in range(4):
#     arr[0][j] = N+j
#     arr[1][7-1-j] = N - j
#
# print(arr[0])
# print(arr[1])
#=====================================\

# N = int(input())
#
# lst = [[0] * 7 for _ in range(2)]
#
# t1 = N
# for i in range(4):
#     lst[0][i] = t1
#     t1 += 1
#
# t2 = N
# for i in range(6, 2, -1):
#     lst[1][i] = t2
#     t2 -= 1
#
# print(lst[0])
# print(lst[1])

import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", "w")

text = input()
print(text)
