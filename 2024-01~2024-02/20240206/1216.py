# 1216. [S/W 문제해결 기본] 3일차 - 회문2

def is_pelindrome(s):
    
    for i in range(len(s) // 2):
        if s[i] != s[-1 -i]:
            return False
    return True

def answer_pelindrome():
    
    N = 100
    arr = [list(input()) for _ in range(100)]
    answer1 = 0
    answer2 = 0
    for len in range(N, 0, -1): # 회문의 길이 100부터 1까지 반복 cnt 
        for row in range(N): # 0 ~ 99
            for col in range(100-len+1): # 0 ~ 99
                if is_pelindrome(arr[row][col:col+len]) == True: # len = 100이면 0~99 len 이 99이면 0~98, 1~99
                    answer1 = len
                if answer1:
                    break
            if answer1:
                break
        if answer1:
            break
    arr2 = [[] for _ in range(100)]
    for row in range(N):
        for col in range(N):
            arr2[row].append(arr[col][row])
            
    for len2 in range(N, len, -1): # 회문의 길이 100부터 1까지 반복 cnt 
        for row in range(N): # 0 ~ 99
            for col in range(100-len2+1): # 0 ~ 99
                if is_pelindrome(arr2[row][col:col+len2]) == True: # len = 100이면 0~99 len 이 99이면 0~98, 1~99
                    return len2
    else:
        return answer1

for _ in range(10):
    tc = int(input())
    print(f"#{tc} {answer_pelindrome()}")
