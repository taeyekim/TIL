data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for ele in data_1:
    if ele.isupper() == True or ele == ' ':
        print(ele, end="")
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

arr.append(data_2.index('내'))
arr.append(data_2.index('힘'))
arr.append(data_2.index('들'))
arr.append(data_2.index('다'))
print(arr)
arr.sort()
print(arr)

for ele in arr:
    print(data_2[ele], end ='')
