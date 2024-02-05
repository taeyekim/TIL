# 1221. [S/W 문제해결 기본] 5일차 - GNS

T = int(input())
for tc in range(1, T+1):
    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_arr = [0] * 10
    TC_num, N = input().split()
    lst = list(map(str, input().split()))
    for ele in lst:
        cnt_arr[arr.index(ele)] += 1
 
    for i in range(10):
        print(f"{TC_num}")
        for j in range(cnt_arr[i]):
            print(f"{arr[i]} ", end=' ')
