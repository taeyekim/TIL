N = 6
numbers = [6, 6, 7, 7, 6, 7]
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        for k in range(3):
            # if k==i or k==j:
            # continue
            print(i, j, k '=>', numbers[i], numbers[j], numbers[k])