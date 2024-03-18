N = 6
numbers = [68, 15, 23, 41, 44, 16]

def quickSort(s, e):
    while s<e:
        p = partition(s, e)
        quickSort(s, p-1)
        quickSort(p+1, e)

quickSort(0, N-1)
