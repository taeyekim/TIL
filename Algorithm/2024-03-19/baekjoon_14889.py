def combi(k, s):
    if k==N//2:
        (값 구한다)
        return

    for i in range(s, N):
        result[k] = i
        combi(k+1, i+1)
