# 5356. 의석이의 세로로 말해요

T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    max_len = 0
    
    for lst in arr:
        if max_len < len(lst):
            max_len = len(lst)
    answer = ''
    for i in range(max_len):
        for j in range(5):
            if len(arr[j]) >= i + 1:
                answer += arr[j][i]
    print(f"#{tc} {answer}")
    
    