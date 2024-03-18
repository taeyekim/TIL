def bitPrint(num):
    for j in range(4):
        if num & 1<<j:
            print(1)
        else:
            print(0)

bitPrint(7)
print(bin(7))

    # 0번째 bit # 1<<0
    if num & 1:
        print(1)
    else:
        print(0)
    # 1번째 bit # 1<<1
    if num & 2:
        print(1)
    else:
        print(0)
    # 2번째 bit
    if num & 4: # 1<<2
        print(1)
    else:
        print(0)

def decTobin(num):

num = 7
#'0111'

# num = '10'
# print(int(num))
# print(int(num, 10))
# print(int(num, 2))
# print(int(num, 16))
#
# num = 5
# binV = bin(num)
# hexV = hex(num)
# print(num)
# print(num, binV, type(binV))
# print(num, hexV, type(hexV))