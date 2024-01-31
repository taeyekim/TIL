T = int(input())

A = [i for i in range(1, 13)]
num = len(A)
for tc in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << num): #=> 8==2**3==1000(1<<3)
        
        arr = []
        for j in range(num):
            if i & (1<<j):
                arr.append(A[j])
        if len(arr) == N and sum(arr) == K:
            cnt += 1

    print(f"#{tc+1} {cnt}")