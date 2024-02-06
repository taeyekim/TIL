# 14940. 4861 회문

def is_pelindrome():


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ARR = [input() for _ in range(N)]
    answer = ''
    for i in range(N):
        for j in range(N//2):
            print(ARR[i][j], ARR[i][N-1 - j])
            if ARR[i][j] != ARR[i][N-1 - j]:
                break
        else:
            answer = ARR[i]
            break

    for i in range(N):
        for j in range(N//2):
            if ARR[j][i] != ARR[N-1 - j][i]:
                break
        else:
            for k in range(N):
                answer += ARR[k][i]
                break

    print(f"#{tc} {answer}")


