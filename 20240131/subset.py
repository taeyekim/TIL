N = 5
arr = [1,2,3,4,5]

for i in range(1<<N):
    for j in range(N):
        if i&(i<<j):
            s = arr[j]
      
    print(s)