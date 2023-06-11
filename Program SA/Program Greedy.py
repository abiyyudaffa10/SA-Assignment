from re import L
import sys
from queue import Queue

def reset():
    global dist, previous, q, in_queue
    for i in range(m):
        previous[i] = 0
        dist[i] = -INF
        in_queue[i] = False
    dist[source] = 0
    previous[source] = -1
    q.put(source)

def pushqueue(curr, before, new_distance):
    global dist, previous, q, in_queue
    dist[curr] = new_distance
    previous[curr] = before
    if not in_queue[curr]:
        q.put(curr)
        in_queue[curr] = True

def popqueue():
    value = q.get()
    in_queue[value] = False
    return value

INF = sys.maxsize
n = 3
m = n * 2 + 2

matrix =[
    [2, 4, 8],
    [4, 5, 6],
    [5, 7, 10]
]

matrix = [
    [6000, 10000, 20000],
    [7000, 7500, 9000],
    [9000, 11000, 15000]
]

flow = [[0] * m for _ in range(m)]
source = 2 * n
sink = 2 * n + 1
profit = 0
previous = [0] * m
dist = [-INF] * m
in_queue = [False] * m
q = Queue()

while True:
    reset()
    while not q.empty():
        vertex = popqueue()
        if vertex == source:
            for worker in range(n):
                if flow[source][worker] == 0:
                    pushqueue(worker, source, 0)
        elif vertex < n:
            for job in range(n, 2 * n):
                if flow[vertex][job] < 1 and dist[job] < dist[vertex] + matrix[vertex][job - n]:
                    pushqueue(job, vertex, dist[vertex] + matrix[vertex][job - n])
        else:
            for worker in range(n):
                if flow[vertex][worker] < 0 and dist[worker] < dist[vertex] - matrix[worker][vertex - n]:
                    pushqueue(worker, vertex, dist[vertex] - matrix[worker][vertex - n])
    
    curprofit = -INF
    for job in range(n, 2 * n):
        if flow[job][sink] == 0 and dist[job] > curprofit:
            curprofit = dist[job]
            previous[sink] = job
    
    if curprofit == -INF:
        break
    
    profit += curprofit
    cur = sink
    while cur != -1:
        prev = previous[cur]
        if prev != -1:
            flow[prev][cur] = 1
            flow[cur][prev] = -1
        cur = prev
    
    pick = [0] * n
    for i in range(n):
        for j in range(2 * n):
            if flow[i][j] == 1:
                pick[i] = j - n

# output
print("Matrix job assignment:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

print("The maximum profit is:", profit)
print("The selected assignments are:")
for i in range(n):
    print("Worker %d is assigned Job %d with profit %d" % (i + 1, pick[i], matrix[i][pick[i]]))
