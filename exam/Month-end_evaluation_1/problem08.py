############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    dict = {} # 빈 리스트 선언
    for number in set(number_list): # number_list를 set으로 중복 제거 후 요소 순회
        dict[f'{number}'] = 0 # 순회하는 요소 number에 해당하는 dict의 'key' 값에 따른 value를 0으로 초기화
    
    for number in number_list: # number_list 요소 순회
        dict[f'{number}'] += 1 # 순회하는 요소 number에 해당하는 dict의 'key' 값에 따른 value +1 해줌(개수 체크)
    
    for number in set(number_list): # number_list를 set으로 중복 제거 후 요소 순회
        if dict[f'{number}'] == 1: # dict의 value 값이 1인 경우(짝이 맞지 않는 정수 1개)
            return number # 해당 값 반환



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
