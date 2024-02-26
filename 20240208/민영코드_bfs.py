#너비우선은 형제 먼저 보기
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

#<거리구하기1>
# def bfs(s) :
#     q = []
#     visited = [0]*(N+1) # 노드 개수만큼 만들기
#     q.append((s,1))       # 거리가 1
#     visited[s] = 1
#     while q :
#         v,d = q.pop(0)        # v, 거리d
#         print(v,d)

#         for w in G[v] :
#             if not visited[w] :
#                 q.append((w, d+1))
#                 visited[w] = visited[v] + 1 # visted를 거리 개념을 바꿔서 visited가 갖고 있는 노선에 +1 / 인덱스는 노드, 몇 번만에 왔는지
#     print(visited)


#<거리구하기2>
def bfs(s) :
    q = []
    visited = [0]*(N+1) #노드 개수만큼 만들기
    q.append(s)
    visited[s] = 1
    while q :
        v = q.pop(0)        #pop()은 스택이니까 아예 인덱스 쓰기!!!
        print(v)

        for w in G[v] :
            if not visited[w] :
                q.append(w)
                visited[w] = visited[v] + 1 #visted를 거리 개념을 바꿔서 visited가 갖고 있는 노선에 +1 / 인덱스는 노드, 몇 번만에 왔는지
    print(visited)

#2차원배열로 거리구하기
def bfs(s) :
    q = []
    visited = [False]*(N+1) #노드 개수만큼 만들기
    q.append((s,1))       #거리가 1/start가 두 개면 여기에 두 개 넣기
    visited[s] = True
    while q :
        v,d = q.pop(0)        #v, 거리d
        print(v,d)

        for w in range(N+1) :
            if G[v][w] == 1 and not visited[w] :
                q.append((w, d+1))
                visited[w] =True

N, E = map(int, input().split())
lst = list(map(int, input().split()))

G = [[] for _ in range(N+1)]
# G = [[0]*(N+1) for _ in range(N+1)]
'''
[[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
연결된 곳에 1또는 값을 쓰는 방식
'''
for i in range(0, len(lst), 2) :
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1].append(v2)
    G[v2].append(v1)

# for i in range(0, len(lst), 2) :
#     v1 = lst[i]
#     v2 = lst[i+1]
#     G[v1][v2] = 1
#     G[v2][v1] = 1


# print(G)
# bfs(1)
# dfs(1)
print(G)
bfs(1)