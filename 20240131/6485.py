T = int(input())

for tc in range(T): # T 테스트 케이스 갯수
    N = int(input()) # N 입력받을 노선 갯수
    arr = []
    for _ in range(N):
        input_arr = list(map(int,input().split())) # A, B가 들어간 리스트 (A이상 B이하 주행 버스 노선)
        arr.append(input_arr)
    P = int(input()) # P 정류장의 갯수
    C_arr = [0 for _ in range(5000)]
    
    C_check = []
    for _ in range(P):
        C_check.append(int(input()))
    for i in range(N):
        for j in range(arr[i][0], arr[i][1] + 1):
                C_arr[j] += 1
        
    print(f"{tc+1} ", end ='')
    for i in range(len(C_check)):
        print(C_arr[C_check[i]], end = " ")