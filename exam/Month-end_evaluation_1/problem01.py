############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min 함수를 사용하지 않습니다.
def min_cost(cost_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    min = cost_list[0] # 월세 리스트의 첫번째 값 min 변수에 할당
    for i in range(1, len(cost_list)): # 월세 리스트의 인덱스 1부터 끝까지 순환
        if min > cost_list[i]: # min 값보다 월세 리스트의 요소의 값이 작다면
            min = cost_list[i] # min 값에 요소 값 할당
            
    return min # 최종 가장 작은 수 반환


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_cost([25, 40, 50, 55]))  # 25
print(min_cost([60, 70, 90, 80, 100, 35])) # 35
#####################################################
