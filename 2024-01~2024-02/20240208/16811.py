# 16811. 당근 포장하기

T = int(input())
# T = 1

for tc in range(1, T+1):
    N = int(input())
    # N= 21
    # ARR = list(map(int, '1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7'.split()))
    ARR = list(map(int, input().split())) # 1 1 1 2 2 5 1 10 6 30
    num_arr = []
    ARR.sort()
    for ele in set(ARR):
        num_arr.append(ARR.count(ele)) # 1 2 3 4 -> 5, 3, 1, 10
        # print(ele)
    
    # print(num_arr)
    N2 = len(num_arr)
    # print(N2)
    min_V = 99999999
    for li1 in range(0, N2 - 2):
        for li2 in range(li1 + 1, N2 - 1):
            total = [0, 0, 0]
            
            for i in range(0, li1 + 1):
                total[0] += num_arr[i]
            for j in range(i + 1, li2 + 1):
                total[1] += num_arr[j]
            for k in range(j + 1, N2):
                total[2] += num_arr[k]
            if max(total[0], total[1], total[2]) > N//2:
                # print("total continue point : ", li1, li2, total[0], total[1], total[2])
                continue
                
            v1 = abs(total[0] - total[1])
            v2 = abs(total[1] - total[2])
            v3 = abs(total[2] - total[0])
            # print(min_V, li1, li2, total[0], total[1], total[2], v1, v2 ,v3)

            min_V = min(min_V, max(v1, v2, v3))

    if min_V == 99999999:
        min_V = -1
    print(f"#{tc} {min_V}")
    
    