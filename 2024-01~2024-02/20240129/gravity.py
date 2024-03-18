'''
9
7 4 2 0 0 6 0 7 0
'''

N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))

max_v = 0 # 가장 큰 낙차
for i in range(N-1): # for i : 0 -> N - 1
    cnt = 0 # 오른쪽에 있는 더 낮은 높이
    for j in range(i+1, N): for j : 