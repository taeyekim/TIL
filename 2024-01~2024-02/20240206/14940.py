# 14940. 4861 회문

def is_pelindrome(s):
    if s == s[::-1]:
        return s
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    answer = False
    
    for i in range(N):
        for j in range(N - M + 1):
            if is_pelindrome(arr[i][j:j + M]) != -1:
                answer = arr[i][j:j + M]
                
        if answer:
            break
    
    
    for i in range(N): # 0 ~ 10
        for j in range(0, N - M + 1): # 0 ~ 2
            str = ''
            for k in range(j, j+M): # 0 ~ 8
                str += arr[k][i]
        if is_pelindrome(str) != -1:
            answer = str
            
        if answer:
            break
        else:
            str = ''
        
    print(f"#{tc} {answer}")


