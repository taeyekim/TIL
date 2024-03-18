# 삭제
# 힙은 우선순위 큐를 만들기 위해서 사용 (우선순위가 높은애가 빠지는 것)-> 예) 계산기 문제
# 힙은 가장 높은 우선수위가 가장 높은 것
# 삽입할 때 완전이진트리를 깨지 않도록 한 다음 위치에 데이터 넣음. 부모와 비교해서 자식이 더 크면 바꿈
# 조건 2개: 부모가 있는 동안 비교, 부모가 자식보다 클 때
# 이진트리 삽입
def insert(data):
    idx = 1
    while Tree[idx]:   #데이터가 있는 동안
        if Tree[idx] > data:
            idx *= 2   #데이터가 더 작으면 왼쪽
        else:
            idx = idx*2 + 1   #데이터가 더 크면 오른쪽

    Tree[idx] = data
    print(Tree)

Tree= [0] * 100
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
    insert(data)
#======================================================
# 찾으면 index, 못찾으면 -1
def insert(data):
    idx = 1
    while Tree[idx]:   #데이터가 있는 동안
        if Tree[idx] > data:
            idx *= 2   #데이터가 더 작으면 왼쪽
        else:
            idx = idx*2 + 1   #데이터가 더 크면 오른쪽

    Tree[idx] = data
    print(Tree)


def find(key):
    idx = 1
    while Tree[idx]:
        if Tree[idx] == key:
            return idx
        if Tree[idx] < key:
            idx = idx*2 + 1
        else:
            idx *= 2
    return -1

#
Tree= [0] * 100
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
    insert(data)

print(find(2))
print(find(16))
print(find(5))
print(find(3))
print(find(12))
print(find(15))
# # ==============================================================
# 힙 : 완전이진트리여야함 -> 순서대로 데이터 채워야함
# #  최대힙 (부모> 자식) + 넣을 때 왼쪽의 크기는 비교하지 않아도 괜찮음
# # 위에서 밑으로 볼때는 왼쪽과 오른쪽 자식 중에 더 큰 값과 비교 (왼쪽거를 넣어놓고, 오른쪽것과 비교하면서 넣기)
def enqueque(data):
    global last

    last += 1
    Tree[last] = data
    c = last
    p = last//2

    while p:
        if Tree[p] < Tree[c]:
            Tree[p], Tree[c] = Tree[c], Tree[p]
            c = p
            p = c // 2 #순서바꾸면 안됨 (먼저 나누면 이상해짐)
        else:
            break

    print(Tree)

Tree= [0] * 100
last = 0
for data in [20, 15, 19, 24, 13, 11]:
    enqueque(data)


# =============================================================
# 삭제
# 무조건 root 빠짐
# 위에서 밑으로 내릴 때는 왼, 오중에 큰거 비교해야함 -> 일단 왼쪽으로 넣어두고 인덱스 오른쪽과 비교해서 크면 바꾸기
def dequeue(data):
    global last

    result = Tree[1]
    # 힙을 재구성
    Tree[1] = Tree[last]
    last -= 1  #last를 옮겼기 때문에 번호를 하나 줄여주기
    p = 1       #root가 p
    c = p * 2
    while c <= last:
        if c+1<=last and Tree[c] < Tree[c+1]: #인덱스 +1 이나 변환을 주게 되면 무조건 범위 먼저 작성
            c += 1
        if Tree[p] < Tree[c]:
            Tree[p], Tree[c] = Tree[c], Tree[p]
            p = c #밑으로 또 내려가서 확인해봐야하기 때문에 다시 정의하기
            c = p*2
        else:
            break
    print(last,Tree)

    return result



Tree= [0] * 100   #완전이진트리 만들기
last = 0          #마지막 위치
for data in [20, 15, 19, 24, 13, 11]:
    enqueque(data)
#
# print(dequeue())
# print(dequeue())
# print(dequeue())