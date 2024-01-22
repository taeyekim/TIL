# 아래 함수를 수정하시오.
def reverse_string(strs):
    answer = list(strs)
    answer.reverse()
    
    return ''.join(answer)

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
