


def solve(N, K, ARR):
    
    curP = 0
    pre = 0
    result = 0
    
    for _ in range(K): # 점프횟수 K만큼 반복문 실행
        jump = ARR[curP]
        if ARR[curP] > 0 and pre < 0:
            jump = jump + (-pre)
        pre = ARR[curP]
        curP = curP + jump
        if curP < 0 or curP >= N:
            return result
        
        result = result + ARR[curP]
        
    return result

N, K = map(int, input().split())
ARR = list(map(int, input().split()))
print(solve(7, 4, ARR))
