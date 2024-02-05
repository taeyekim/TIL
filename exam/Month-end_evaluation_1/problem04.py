############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):

    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt = 0 # 글자 개수 체크 cnt = 0 초기화
    for i in user['password']: # user 딕셔너리의 키 'password'에 해당하는 value 요소 순회
        cnt += 1 # 요소 순회할 때마다 +1
    if 8 <= cnt < 32 and user['password'] == user['password_confirm']:
         # 요소의 길이가 8글자 이상, 32글자 미만이며 user['password']의 값과 user['password_confirm']의 값이 일치할 경우
        return True # True 반환
    else: # 그외의 경우
        return False # False 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
