T = int(input())

for cnt in range(T):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    max = sum(arr[:M])
    min = sum(arr[:M])
    for i in range(1, len(arr) - M + 1):
        if max < sum(arr[i:i+M]):
            max = sum(arr[i:i+M])
        if min > sum(arr[i:i+M]):
            min = sum(arr[i:i+M])
    
    print(f"#{cnt+1} {max - min}")
