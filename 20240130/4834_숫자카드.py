T = int(input())

for num in range(T):
    N = int(input())
    num_str = input()
    num_arr = [0 for _ in range(10)]
    for s in num_str:
        num_arr[int(s)] += 1
    max_cnt = 0
    max_num = 0
    for i in range(len(num_arr)):
        if max_cnt <= num_arr[i]:
            max_cnt = num_arr[i]
            max_num = i

    print(f"#{num + 1} {max_num} {max_cnt}")