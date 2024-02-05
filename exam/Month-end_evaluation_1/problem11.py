############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    for i in range(len(matrix)): # matrix의 행 인덱스 i 반복
        for j in range(len(matrix[0])): # matrix의 열 인덱스 j 반복
            if matrix[i][j] == 1: # matrix[i][j]의 값이 1인 곳이 발견되면 row = i, col = j 행, 열 할당
                row = i
                col = j
    
    for M in move_list:
        if M == 0: # M = 0 일때 row 위치 -1 (위로 이동)
            row -= 1
        elif M == 1: # M = 1 일때 row 위치 +1 (아래로 이동)
            row += 1
        elif M == 2: # M = 2 일때 col 위치 -1 (왼쪽으로 이동)
            col -= 1
        elif M == 3: # M = 3 일때 col 위치 +1 (오른쪽으로 이동)
            col += 1

        if 0 <= row <= N-1 and 0 <= col <= N-1:
            # row의 값(행 위치)이 0~N-1 범위에 있고, col의 값(열 위치)이 0~N-1 범위에 있다면 continue(현재 반복문 종료 후 다음 값 순회)
            continue
        else: # row 혹은 col 변수가 정해진 범위를 벗어나면 그 즉시 None 반환
            return None
    
    return [row, col] # 마지막까지 범위를 벗어나지 않아서 None을 반환하지 않았다면 현재 위치 반환



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
