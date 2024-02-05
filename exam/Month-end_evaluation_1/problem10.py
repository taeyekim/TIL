############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    row = current[0] # row 변수에 current 튜플의 row값 할당 (인덱스 0)
    col = current[1] # col 변수에 current 튜플의 col값 할당 (인덱스 1)
    if M == 0: # M = 0 일때 row 위치 -1 (위로 이동)
        row -= 1
    elif M == 1: # M = 1 일때 row 위치 +1 (아래로 이동)
        row += 1
    elif M == 2: # M = 2 일때 col 위치 -1 (왼쪽으로 이동)
        col -= 1
    elif M == 3: # M = 3 일때 col 위치 +1 (오른쪽으로 이동)
        col += 1

    if 0 <= row <= N-1 and 0 <= col <= N-1: 
        # row의 값(행 위치)이 0~N-1 범위에 있고, col의 값(열 위치)이 0~N-1 범위에 있다면
        return True # True 반환
    return False # 그외에는 범위를 벗어난 것이기 때문에 False 반환
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
