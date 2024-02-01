T = int(input())

for tc in range(1, T+1):
    arr = []
    for _ in range(100):
        arr.append(list(map(int,input().split())))
    for col in range(100):
        if arr[99][col] == 2:
            break
    for row in range(98, -1, -1):

        if arr[row][col - 1] and d == "up":
            while arr[row][col - 1]:
                col -= 1
                d = "left"
        elif arr[row][col + 1] and d == "up":
            while arr[row][col + 1]:
                col += 1
                d = "right"
        else:
            row -= 1
            d = "up"
    print(f"#{tc} {col}")


