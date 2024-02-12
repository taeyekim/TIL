# 2005. 파스칼의 삼각형

def pascal(n):
    arr = []
    for i in range(n):
        if i == 0:
            arr.append([1])
        elif i == 1:
            arr.append([1, 1])
        else:
            arr.append([])
            for j in range(0, len(arr[i-1]) - 1): # [1, 2, 1] 0,1 1,2 이전 배열의 인덱스 -1까지 참조해야 함
                arr[i].append(arr[i-1][j] + arr[i-1][j+1])
            arr[i].insert(0, 1)
            arr[i].append(1)
    return arr[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc}")
    for i in range(1, N+1):
        print(*pascal(i))