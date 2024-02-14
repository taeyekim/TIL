미로


# 2에서 시작해서 3으로 가는길이 있으면 1 없으면 0반환
def solve():
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j

    stack = []
    stack.append((r, c))
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        cr, cc = stack[-1]
        if arr[cr][cc] == 3:
            return 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    # dfs 수행중에 길 못찾음
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')

#     dfs 수행 중에 길 못찾음


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = solve()
    print(f'{tc} {result}')



----------------------------------------------------------

def solve():
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j

    stack = []
    stack.append((r, c))
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        cr, cc = stack[-1]
        if arr[cr][cc] == 3:
            return 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break  # << d가 전부 돌기 전에 break 하면 break 한 이후의 경우의 수는 씹혀버릴듯
        else:
            stack.pop()  # for-else로 구성하면 break 됐을 때 stack.pop() 작동 안되니까 반복문이 헛돌 수 있음


#     dfs 수행 중에 길 못찾음

# 길 못 찾는 경우는..? << return 0 시켜줘야 되는 부분 구현 안돼 있음


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    result = solve()
    print(f"{tc} {result}")

============================================================
연습문제 2
def f(i, k, t):#k개의 원소를 가진 배열A, 부분집합 합이 t인 경우 t는 내가 찾는 값
    if i == k: #모든 원소에 대해 결정하면
        ss = 0   #부분집합 원소의 합
        for j in range(k):
            if bit[j] == 1:  #원래라면 ==1 생략해도 괜찮음 A[i]가 포함된 경우
                    ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]: #A[j]가 포함된 경우
                    print(A[j], end = ' ')
            print()
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)

            # bit[i] = 1
            # f(i+1, k)
            # bit[i] = 0
            # f(i+1, k)
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N #bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 10)

---------------------------------------------------------------------

def f(i, k, s, t):#k개의 원소를 가진 배열A, 부분집합 합이 t인 경우 t는 내가 찾는 값
    global cnt
    cnt += 1
    if s == t: #모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j] == 1:
                print(A[j], end = ' ')#원래라면 ==1 생략해도 괜찮음 A[i]가 포함된 경우
        print()             #부분집합 출력
    elif i == k:
        return
    elif s > t:
        return
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, s+A[i]*j, t)

            # bit[i] = 1
            # f(i+1, k , s+A[i], t)
            # bit[i] = 0
            # f(i+1, k, s, t)
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N #bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt = 0
f(0, N, 0, 10)
print('cnt :', cnt)

-----------------------------------------------
# 순열
def nPr(i, k):
    global cnt
    global min_V
    if i == k:
        cnt += 1
        # print(*P)
        s = 0   #선택한 원소의 합
        for j in range(k):  #j 행에 대해
            s += arr[j][P[j]]  #j행에서 p[j]열을 고른 경우의 합 구하기
        if min_V > s:
            min_V = s
    else:
        for j in range(i, k): #P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i] #P[i] <-> P[j]
            nPr(i+1, k)
            P[i], P[j] = P[j], P[i]  #교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_V = 100
cnt = 0
P = [1, 2, 3]
nPr(0, N)
print(min_V, cnt)

# ================================================

def nPr(i, k, s):
    global cnt
    global min_V
    cnt += 1
    if i == k:
        # print(*P)
        if min_V > s:
            min_V = s
    elif s >= min_V:
        return
    else:
        for j in range(i, k): #P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i] #P[i] <-> P[j]
            nPr(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  #교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_V = 100
cnt = 0
P = [1, 2, 3]
nPr(0, N, 0)
print(min_V, cnt)

--------------------------------------- 오프라인 강사님
def subset(k):
    if k == N:
        print(check)
        sum_V = 0
        for i in range(N):
            if check[i]:
                sum_V += numbers[i]
                # print(numbers[i], end = ' ')
        print(sum_V)
        return

    for i in [0, 1]:
        check[k] = i
        subset(k+1)

N = 3
numbers = [10, 30, 20]
check = [-1] * N
# check = [0, 0, 0] => {}
# check = [0, 0, 1] => {20}
# check = [1, 1, 1] {10, 30, 20}
#        k=0  1  2
subset(0)

---------------------------------------------------------
N = 3
numbers = [10, 30, 20]
check = [-1] * N

def subset(k, midS):
    if k == N:
        print(check)
        print(midS)
        return

    # 백트래킹, 30을 넘어가면 보지 않겠다고 이야기 해줌
    if midS > 30:
        return


    for i in [1, 0]:
        check[k] = i
        if i == 0:
            subset(k + 1, midS)
        else:
            # midS += numbers[k]  -> 이렇게 쓰면 다음 반복에 영향을 줌 (값이 밑으로 내려가지 않음),
            # midS의 값이 바뀌지 않고 아래로 똑같이 내려보낼 수 있도록 작업을 한 것임
            subset(k + 1, midS + numbers[k])
subset(0,0)
===================================================================
# 순열
# check = [0, 1, 2] => [10, 30, 20]
# check = [0, 2, 1] => [10, 20, 30]
# check = [1, 0, 2] => [30, 10, 20]
# check = [1, 2, 0] => [30, 20, 10]
# check = [2, 0, 1] => [20, 10, 30]
# check = [2, 1, 0] => [20, 30, 10]

def perm(k):
    if k == N:
        print(check)
        for i in range(N):
            index = check[i]
            print(numbers[index], end = ' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            check[k] = i
            visited[i] = True #밑으로 내려보내기 전에 True하고, return 만나면서 해제 시켜야함
            perm(k+1)
            visited[i] = False   #해제
#             강의자료에 있던 순열도 이것과 똑같은 방식 사용
N = 3
numbers = [10, 30, 20]
check = [-1] * N
visited = [False] * N
# check = [0, 0, 0] => {}
# check = [0, 0, 1] => {20}
# check = [1, 1, 1] {10, 30, 20}
#        k=0  1  2

perm(0)


# 0번째와 0번째가 교환한 경우, 1번째와 0번째가 교환한 경우, 2번째와 0번째가 교환한 경우

