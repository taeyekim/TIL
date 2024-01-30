
for t in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    for _ in range(dump):
        if max(arr) - min(arr) <= 1:
            break
        else:
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
    print(f"#{t + 1} {max(arr) - min(arr)}")
