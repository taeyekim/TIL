# 10761. 신뢰

T = int(input())

for tc in range(1, T+1):

    arr = list(input().split())
    b_rb = []
    o_rb = []
    for i in range(1, len(arr) - 1, 2):
        if arr[i] == 'B':
            b_rb.append(arr[i+1])
        elif arr[i] == 'O':
            o_rb.append(arr[i+1])
    print(b_rb, o_rb)

    for i in range(len(b_rb)):
        if i == 0:
            total = abs(b_rb[i] - 1)
