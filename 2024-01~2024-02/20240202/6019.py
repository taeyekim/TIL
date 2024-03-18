# 6019. 기차 사이의 파리

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A+B)
    answer = time * F
    print(f"#{tc} {answer:.10f}")