# 이진트리_삽입
def insert(data) :
    idx = 1
    while TREE[idx] :  #데이터가 있는 동안
        if TREE[idx] > data :
            idx = idx*2
        else :
            idx = idx * 2 + 1
    TREE[idx] = data
    print(TREE)

TREE = [0]*100 #완전이진트리 만들기
# for data in [9, 4, 12, 3, 6, 15, 13, 17]:
for data in [1,2,3,4,5]: #편향이진트리/정렬할 때는 inorder 순회
    insert(data)

#탐색
def insert(data) :
    idx = 1
    while TREE[idx] :  #데이터가 있는 동안
        if TREE[idx] > data :
            idx = idx*2
        else :
            idx = idx * 2 + 1
    TREE[idx] = data
    print(TREE)


def find(key) : #찾으면 index, 못 찾으면 -1
    idx = 1
    while TREE[idx] :
        if TREE[idx] == key:
            return idx
        if TREE[idx] < key :
            idx = idx * 2 + 1
        else :
            idx *= 2
    return -1


TREE = [0]*100 #완전이진트리 만들기
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
    insert(data)

print(find(2))
print(find(6))
print(find(15))



#힙:완전이진트리여야함 > 순서대로 데이터 채워야 함(왼쪽, 오른쪽 크기는 비교하지 않음, 부모하고의 크기만 비교!)
#최대힙은 부모 값이 자식 값보다 커야 함(최소힙은 반대)

#최대힙 : 우선순위 큐 만들 때 사용 : 넣어놨다가 빼면 우선순위가 높은 애(제일 큰 값/root)가 빠짐

#삽입
#삽입할 때 완전이진트리를 깨지 않도록 한 다음 위치에 데이터 넣음. 부모와 비교해서 자식이 더 크면 바꿈
#조건 2개 : 부모가 있는 동안 비교, 부모가 자식보다 클 때

# def enqueue(data) :
#     global last
#     last += 1            #내가 넣어야 하는 위치 만들기/마지막 데이터 위치 만들기
#     TREE[last] = data
#
#     c = last
#     p = last//2
#
#     while p :          #p가 0이 아닌 동안(나누면서 가니까)

#         if TREE[c] > TREE[p] :
#             TREE[c], TREE[p] = TREE[p], TREE[c]
#             c = p      #순서 안 바뀌게!
#             p = c//2
#         else :
#             break
#
#     print(TREE)
#
#
#
# TREE = [0]*100 #완전이진트리 만들기
# last = 0       #마지막 위치
# for data in [20, 15, 19, 24, 22]:
#     enqueue(data)


#삭제
#무조건 root 빠짐
#위에서 밑으로 내릴 때는 왼, 오 중 큰 거 비교해야함 > 일단 왼쪽으로 넣어놓고 인덱스 오른쪽과 비교해서 크면 바꾸기
def enqueue(data) :
    global last
    last += 1            #내가 넣어야 하는 위치 만들기/마지막 데이터 위치 만들기
    TREE[last] = data

    c = last
    p = last//2

    while p :          #p가 0이 아닌 동안(나누면서 가니까)
        if TREE[c] > TREE[p] :
            TREE[c], TREE[p] = TREE[p], TREE[c]
            c = p      #순서 안 바뀌게!
            p = c//2
        else :
            break

def dequeue() : #무조건 맨 위에 있는 게 빠지기 때문에 데이터 있으면 안 됨
    global last

    result = TREE[1]
    #힙 재구성
    TREE[1] = TREE[last] #마지막 꺼를 root로 보내기
    last -= 1   #last를 내 앞에 있는 애로 움직여주기

    p = 1       #root가 p
    c = p*2

    while c <= last :
        if c+1 <= last and TREE[c] < TREE[c+1] : #인덱스+1 이나 변환을 주게 되면 무조건 범위 먼저 작성
            c += 1
        if TREE[p] < TREE[c] :
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else :
            break
    print(last, TREE)

    return result

# TREE = [0]*100 #완전이진트리 만들기
# last = 0       #마지막 위치
# for data in [20, 15, 19, 24, 22]:
#     enqueue(data)
#
# print(dequeue())
# print(dequeue())
# print(dequeue())