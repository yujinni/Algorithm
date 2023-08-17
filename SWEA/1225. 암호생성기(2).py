from collections import deque
 
T = 10
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    deq = deque(num_list)
 
    cycle = 1
    while True:
        head_num = deq.popleft() - cycle
 
        if head_num <= 0:
            head_num = 0
            deq.append(head_num)
            break
 
        deq.append(head_num)
        cycle = cycle % 5 + 1
 
    print('#{}'.format(tc), *deq)