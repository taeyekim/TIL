# def isFull():
#     return front == (rear+1)%SIZE
#
# def isEmpty():
#     return front == rear
#
# def deQueue():
#     global front
#
#     if isEmpty():
#         print('empty')
#         return
#
#     front = (front + 1) % SIZE
#     return Q[front]
#
# def enQueue(item):
#     global rear
#
#     if isFull():
#         print('full')
#         return
#
#     rear = (rear + 1) % SIZE
#     Q[rear] = item
#
#
# SIZE = 4
# Q = [-1] * SIZE
# front = -1
# rear = -1
# enQueue(10)
# enQueue(20)
# enQueue(30)
# t = deQueue()
# print(t)
# print(deQueue())
# print(deQueue())

Q = []
Q.append(10)
    if Q:
        print(Q.pop(0))

[100010, 10009, 10008, 10006,...1]

