# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit로 묶어 십진수로 변한 하여 출력해보자
mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
           '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
           'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
           }

def binTodec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result

s = input()
answer = ''
for c in s:
    answer += mapping[c]
print(answer)
for i in range(0, len(answer), 7):
    if i + 7 >= len(answer):
        print(binTodec(answer[i:i+7]))
    else:
        print(binTodec(answer[i:i+7]), end = ', ')
