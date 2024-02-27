T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    answer = D * F / (A + B)
    print(f"#{tc} {answer}")