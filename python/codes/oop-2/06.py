# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다')

# try:
#     num = int(input('숫자입력 :'))
# except ValueError:
#     print('숫자가 아닙니다.')

try:
    num = int(input())
except ValueError:
    print('숫자를 넣어줘')
except ZeroDivisionError:
    print('0으로 나누기가 될 것 같아?')
except:
    print("알 수 없는 에러가 발생했음")