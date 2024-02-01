for _ in range(10):
    arr = []
    tc = int(input())
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    max_num = 0
    total_arr = []
    total_across = 0
    for i in range(100):
        total_row = 0
        total_col = 0
        total_across += arr[i][i]
        for j in range(100):
            total_row += arr[i][j]
            total_col += arr[j][i]
        total_arr.append(total_row)
        total_arr.append(total_col)
    total_arr.append(total_across)

    total_across = 0
    for i in range(100):
        total_across += arr[9-i][i]
    total_arr.append(total_across)

    for x in total_arr:
        if x >= max_num:
            max_num = x
    print(f"#{tc} {max_num}")
