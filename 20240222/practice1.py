# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111
def binTodec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result

lst = list(input().split())
s = ''.join(lst)
print(s)

for i in range(0, len(s), 7):
    if i == len(s) - 7:
        print(binTodec(s[i:i+7]))
    else:
        print(binTodec(s[i:i+7]), end = ', ')