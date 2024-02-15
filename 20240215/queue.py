# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# # print(queue.pop(0))
# # print(queue.pop(0))
# # print(queue.pop(0))
# while queue:
#     print(queue.pop(0))

# ----------------

N = 10
q = [0] * N
front = rear = -1

rear += 1   # enqueue(10)
q[rear] = 10
rear += 1   # enqueue(20)
q[rear] = 20
rear += 1   # enqueue(30)
q[rear] = 30

while front != rear:  # 큐가 비어있지 않으면
    front += 1      # dequeue()
    print(q[front])
