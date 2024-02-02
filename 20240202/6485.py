# 삼성시의 버스 노선
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001 # 5000번 정류장까지
    # N개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1): # 1 <= A <= B <= 5000
            counts[j] += 1
    P = int(input())
    busstop = [int(input()) for _ in range(P)]
    print(f"#{tc}", end = ' ')
    for i in busstop: # 출력할 정류장 번호
        print(counts[i], end = ' ')
    print()