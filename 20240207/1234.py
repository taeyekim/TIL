# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호

for tc in range(1, 11):
    N_len, N = map(int, input().split())
    N = list(''.join(str(N)))
    stack = []
    for n in N: # N = 1238099084 /  N : [1 2 3 8 0 9 9 0 8 4] n : 1 2 3 8 0 9 9 0 8 4
        if len(stack) <= 0:
            stack.append(n)
        else:
            if stack[-1] == n:
                stack.pop()

            else:
                stack.append(n)
    answer = ''
    for c in stack:
        answer += c
    answer = answer.lstrip('0')
    print(f'#{tc} {answer}')