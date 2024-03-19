def insert(value):
    pos = 1
    while True:
        if TREE[pos] == -1:
            TREE[pos] = value
            break
        if TREE[pos] > value:
            pos *= 2
        else:
            pos = pos*2 + 1

def inOrder(rootP):
    if TREE[rootP*2] != -1:
        inOrder(rootP*2)
    print(TREE[rootP])
    if TREE[rootP*2+1] != -1:
        inOrder(rootP*2+1)

TREE = [-1] * 100
insert(9)
insert(12)
insert(15)
insert(4)
print(TREE)