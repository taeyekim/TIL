# 1989. 초심자의 회문 검사

T = int(input())

for tc in range(1, T+1):
    A = input()
    print(A, A[::-1])
    if A == A[::-1]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")