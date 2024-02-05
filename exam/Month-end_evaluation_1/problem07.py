############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.

    dict = {} # 빈 딕셔너리 선언
    for email in email_list: # email_list 요소 순회
        dict[f'{email}'] = 0 # email_list의 요소가 dict의 'key' 값에 해당하는 경우 해당 value를 0으로 초기화

    for email in email_list: # email_list 요소 순회
        dict[f'{email}'] += 1 # email_list의 요소가 dict의 'key' 값에 해당하는 해당 value에 +1
    return dict # 딕셔너리 반환


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
