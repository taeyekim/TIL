# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )


T = int(input()) # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input()) # 색칠할 영역 개수
    lst = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        
        arr = list(map(int, input().split())) # 색칠 정보 담긴 배열 생성
        for i in range(arr[0], arr[2] + 1):
            for j in range(arr[1], arr[3] + 1):
                if (lst[i][j] == 1 and arr[4] == 2) or (lst[i][j] == 2 and arr[4] == 1):
                    lst[i][j] = 3
                else:
                    lst[i][j] += arr[4]
    purple_check = 0
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                purple_check += 1
    print(f"#{tc} {purple_check}")