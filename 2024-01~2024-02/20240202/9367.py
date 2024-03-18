# 9367. 점점 커지는 당근의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    
    max_cnt = 0
    cnt = 0
    for i in range(1, N+1):
        if arr[i-1] < arr[i]:
             cnt += 1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")
    