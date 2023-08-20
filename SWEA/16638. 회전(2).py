def enqueue(item):
    global rear
    rear += 1
    q[rear] = item

  
def dequeue():
    global front
    front += 1
    return q[front]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    size = N + M
    q = [0] * size

    front = rear = -1

    for i in range(N):
        enqueue(num_list[i])

    for j in range(M):
        d = dequeue()
        enqueue(d)

    print(f'#{tc} {dequeue()}')