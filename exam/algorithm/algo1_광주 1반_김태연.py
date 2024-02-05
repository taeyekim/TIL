
dx = [0, 1, 0, -1] # 상하좌우 4방향으로 한 칸씩 옮겨줄 x 좌표 리스트
dy = [1, 0, -1, 0] # 상하좌우 4방향으로 한 칸씩 옮겨줄 y 좌표 리스트

T = int(input()) # T 테스트 케이스 입력 받음

for tc in range(1, T+1): # 테스트 케이스만큼 반복
    N = int(input()) # 리스트의 가로세로 갯수 입력 받음
    arr = [list(map(int, input().split())) for _ in range(N)] # N개의 행 만큼 리스트 입력 받음 (N * N 리스트)

    bonus_num = 0 # 최종 보너스 점수 0으로 초기화 후 시작
    for x in range(N):
        for y in range(N): # x와 y를 인덱스 기준 0~N-1씩 반복문 돌림
            pos = arr[x][y] # 가운데 위치값
            num = 0 # 중간 계산 점수 0 초기화 후 시작

            for k in range(4): # x,y 좌표 리스트의 요소 4개씩 반복할 k = 0~3 순회하는 반복문 생성
                nx = x + dx[k] # 이동할 x좌표
                ny = y + dy[k] # 이동할 y좌표
                if 0 <= nx <= N-1 and 0 <= ny <= N-1: # 이동할 x,y좌표가 0~N-1 사이라면
                    num += arr[nx][ny]  # 점수에 합산
                else: # 이동할 x, y 좌표가 리스트의 범위를 벗어났다면
                    num = 0 # 점수 0 초기화 후 break로 for문 종료
                    break
            num -= pos # 중간 계산 점수는 num - 현재 위치값
            if num < 0: # num이 0보다 작다면
                num = 0 # num = 0
            elif num > 0 and num % 2 == 0: # num이 양수이고 동시에 짝수일 경우
                num *= 2 # 점수 * 2

            if bonus_num < num: # 지금까지 합산한 점수 num이 bonus_num 보다 클 시에
                bonus_num = num # bonus_num에 중간 계산 점수 num이 할당됨
# 따라서 최종값 bonus_num과 중간계산 점수 num을 비교하여 반복문을 돌려 나온 num 중 가장 큰 값이 bonus_num에 할당되게 됨

    print(f"#{tc} {bonus_num}") # 최종 출력
