# int를 사용하지말고, ord와 chr 함수 이용해서 만들기
# ord('a')를 넣으면 정수 97을 반환합니다.
# chr(97)을 하면 문자 'a'를 반환합니다.
def atoi(s): # '123' => 123
    r = 0
    for c in s:
        r = r*10 + ord(c) - ord('0')
    return r

t = atoi('123')
print(t, type(t))

def itoa(number): # 321 => '321'

    result = ""
    while number > 0:
        c = chr(48 + number % 10)
        result = result + c
        number = number // 10
    return result

t = itoa(321)
print(t, type(t))

# a = 'aa'
# b = 'ab'
# print(a>b) -> False