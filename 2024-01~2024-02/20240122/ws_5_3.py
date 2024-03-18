# 아래 함수를 수정하시오.
def sort_tuple(tup):
    answer = [i for i in tup]
    answer.sort()
    return tuple(answer)

result = sort_tuple((5, 2, 8, 1, 3))
print(result)