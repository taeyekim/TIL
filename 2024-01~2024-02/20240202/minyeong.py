#16268. 풍선팡2
di = [0,1,0,-1]
dj = [1,0,-1,0]


T = int(input())
for tc in range(T) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxv= 0 # 최대 꽃가루 합계
    for i in range(N) : # N*M 크기의 게임판
        for j in range(M) :
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수

            # 주변 풍선의 꽃가루
            for k in range(4) : # 주변 풍선의 인덱스 ni, nj
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M :
                    cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if maxv < cnt :
                maxv = cnt
    print(f'# {tc+1} {maxv}')

#풍선팡
di = [0,1,0,-1]
dj = [1,0,-1,0]


T = int(input())
for tc in range(T) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxv= 0 # 최대 꽃가루 합계
    for i in range(N) : # N*M 크기의 게임판
        for j in range(M) :
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수

            # 주변 풍선의 꽃가루
            for k in range(4) : # 주변 풍선의 인덱스 ni, nj
                for l in range(1, arr[i][j]+1):
                ni = i + di[k] *l
                nj = j + dj[k] *l
                if 0 <= ni < N and 0 <= nj < M :
                    cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if maxv < cnt :
                maxv = cnt
    print(f'# {tc+1} {maxv}')




while distance > 0.000001:
    #시간 생성
    t1  = distance/(파리속도+B기차속도)

    #파리 이동 거리
    total += t1*파리속도

    #distance 변경
    distance -= (A 기차속도 + B기차 속도) * t1