# 삭제
# 힙은 우선순위 큐를 만들기 위해서 사용 (우선순위가 높은애가 빠지는 것)-> 예) 계산기 문제
# 힙은 가장 높은 우선수위가 가장 높은 것

def insert(data):
    idx = 1
    while TREE[idx]:   #데이터가 있는 동안
        if TREE[idx] > data:
            idx *= 2   #데이터가 더 작으면 왼쪽
        else:
            idx = idx*2 + 1   #데이터가 더 크면 오른쪽

    TREE[idx] = data
    print(TREE)

# 찾으면 index, 못찾으면 -1
def find(key):
    # idx = 1:
    while TREE[idx]:
        if TREE[idx] == key:
            return idx
        if TREE[idx] < key:
            idx = idx*2 + 1
        else:
            idx *= 2
    return -1


TREE= [0] * 100
for data in [9, 4, 12, 3, 6, 15, 13, 17]:
    insert(data)

print(find(2))
print(find(16))
print(find(5))
print(find(3))
print(find(12))
print(find(15))

#  최대힙 (부모> 자식) + 넣을 때 왼쪽의 크기는 비교하지 않아도 괜찮음
# 위에서 밑으로 볼때는 왼쪽과 오른쪽 자식 중에 더 큰 값과 비교 (왼쪽거를 넣어놓고, 오른쪽것과 비교하면서 넣기)
def enqueque(data):
    global last

    last += 1
    TREE[last] = data

    c = last
    p = last//2

    while p:
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c // 2 #순서바꾸면 안됨 (먼저 나누면 이상해짐)
        else:
            break
    print(TREE)

def dequeue():
    global last
    result = TREE[1]
    # 힙을 재구성
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and TREE[c] < TREE[c+1]:
            c += 1
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p * 2
        else:
            break


TREE = [0] * 100
last = 0
for data in [20, 15, 19, 24, 13, 11]:
    enqueque(data)

# print(dequeue())
# print(dequeue())
# print(dequeue())
