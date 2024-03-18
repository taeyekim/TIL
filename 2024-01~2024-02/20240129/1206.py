

for cnt in range(1, 11):

    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    
    for i in range(2, len(arr) - 2):
        
        answer_list = []
        if arr[i] - arr[i-2] > 0:
            answer_list.append(arr[i] - arr[i-2])
        else:
            continue
        if arr[i] - arr[i-1] > 0:
            answer_list.append(arr[i] - arr[i-1])
        else:
            continue
        if arr[i] - arr[i+1] > 0:
            answer_list.append(arr[i] - arr[i+1])
        else:
            continue
        if arr[i] - arr[i+2] > 0:
            answer_list.append(arr[i] - arr[i+2])
        else:
            continue
        
        sum += min(answer_list)

    print(f"#{cnt} {sum}")