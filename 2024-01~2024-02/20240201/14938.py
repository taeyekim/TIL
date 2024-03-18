T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = []
    for i in range(N):
        total = 0 if i % 2 == 0 else 100
        check_value = 0
        for ele in arr:
            if i % 2 == 0:
                if total < ele:
                    total = ele
            else:
                if total > ele:
                    total = ele
        answer.append(total)
        arr.remove(total)

    print(f"#{tc} ",end = '')
    for i in range(10):
        print(answer[i], end=" ")
    print()
