
for t in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    for _ in range(dump):
        if max(arr) - min(arr) <= 1:
            break
        else:
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
    print(f"#{t + 1} {max(arr) - min(arr)}")
    
TC = 10

for tc in range(1, TC + 1):
    dump = int(input())
    arr = list(map(int, input().split()))
    arr_len = 0
    for _ in arr:
        arr_len += 1

    for i in range(dump):
        max_num = 0
        min_num = 100
        for j in range(arr_len): # 0 ~ (arr_len - 1)
            if arr[j] > max_num:
                max_num = arr[j]
            if arr[j] < min_num:
                min_num = arr[j]
                
        if max_num - min_num >= 2:
            arr[arr.index(max_num)] -= 1
            arr[arr.index(min_num)] += 1
        else:
            break
        
    print(f"{tc} {max_num - min_num}")
        
# dump = 834
# arr = 42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96

def dir(y, x) :
    
    dy = [-1, 1, 0, 0] #y방향 방향배열
    dx = [0, 0, -1, 1] #x방향 방향배열

arr[0][]
3x3배열
arr = [[1, 2, 3], arr[0][0] = 1 arr[0][2] = 3
       [4, 5, 6], arr[2][2] = 9
       [7, 8, 9]]
up = [dy[2]][dx[2]]
right = [dy[0]][dx[1]]

[[0,0], [0,1], [0,2],
 [1,0], [1,1], [1,2],
 [2,0], [2,1], [2,2]]

sum_v = 0
for i in range(4) : 
    #상, 하, 좌, 우 4방향이기 때문에, 대각선까지 포함하면 8, 대각선만 하면 4
    for j in range(1, K+1) :
        # 왜 1부터인가 ? 현재위치는 제외해야하기 때문에 1부터 함 -> 현재위치 제외(y, x)
        ny = y + dy[i] * j #next_y는 현재위치 + 방향 * 퍼져나가는 만큼
        nx = x + dx[i] * j #next_x는 현재위치 + 방향 * 퍼져나가는 만큼
        # dy와 dx는 상하좌우, j는 파워
        if 0 <= ny <= N and 0 <= nx <= N :
            # 합?? 폭탄설치 ?? 곱?? code ...
            # 합 구할 경우
            sum_v += arr[ny][nx]















