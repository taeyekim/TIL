# 최대힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가 (완전이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모 > 자식
    p = c // 2  # 부모 번호 계산
    while p >= 1 and h[p] < h[c]:   # 부모가 있는데, 더 작으면 교환
        h[p],, h[c] = h[c], h[p]    # 교환
        c = p
        p = c//2
    
N = 10      # 필요한 노드 수
h = [0] * (N+1) # 최대힙
last = 0        # 힙의 마지막 노드 번호