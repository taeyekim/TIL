# s = '1010'
# t = int(s)
# print(t)
#
# t = int(s, 2)
# print(t)
#
# t = int(s, 16)
# print(t)

# 이진수 문자열을 십진수로 만들어 return
# def binTodec(s):
#     result = 0
#     for c in s:
#         result = result * 2 + int(c)
#
#     return result
#
#
#
# def decTobin(intV):
#     s = ''
#     while intV > 0:
#         s = str(intV % 2) + s
#         intV //= 2
#
#     return s
#
# def hexTodec(s):
#     result = 0
#     for c in s:
#         if c.isdigit():
#             result = result * 16 + int(c)
#         else:
#             result = result * 16 + ord(c) - ord('A') + 10
#
#     return result
#
# def decTohex(intV):
#     s = ''
#     while intV > 0:
#         r = intV % 16
#         if r < 10:
#             s = str(intV % 16) + s
#         else:
#             s = chr((r-10) + ord('A')) + s
#         intV //= 16
#
#     return s
#
# # def hexTobin(s):
# #     value = hexTodec(s)
# #     binS = decTobin(value)
# #     return binS
#
# def hexTobin(hexS):
#     mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
#                }
#
#     s = ''
#     for c in hexS:
#         s += mapping[c]
#     return s
#
# def binTohex(s):
#     value = binTodec(s)
#     hexS = decTohex(value)
#     return hexS
#
# s = '11001'
# print(binTodec(s))
# print(decTobin(25))
#
# print(hexTodec(s))
# print(hexTodec('A0'))
# print(decTohex(160))
#
# hexS = 'AA0'
# print(hexTobin(hexS))
# print(binTohex(s))

