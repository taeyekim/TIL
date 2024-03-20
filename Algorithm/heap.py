def insert(value):
    global last

    TREE[last] = value
    last += 1

    c = last
    p = c // 2
    while True:
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c // 2
        else:
            break

TREE = [0, 20, 15, 19, 4, 13, 11] + [-1] * 100
# print(TREE)
last = 6
insert(17)
insert(23)