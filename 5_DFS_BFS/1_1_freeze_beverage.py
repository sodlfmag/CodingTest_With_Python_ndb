import time

'''
Point -
1. 최상단 노드가 같은 덩어리인지 탐색한다.
2. 간선 비용이 동일하기 때문에 BFS를 사용한다.
3. 처음부터 끝까지 탐색하면서 0을 발견하면 BFS를 통해 1로 바꾼다.
4. 3번의 작업을 처음부터 끝까지 0이 없을 때까지 수행한다.
'''
# 입력값 ----------
from collections import deque
from pprint import pprint
N, M = map(int, input().split())

graph = []
for i in range(N):
  temp = list(map(int, list(input())))
  graph.append(temp)
  
start_time = time.time()

# 알고리즘 실행 --------------------------------

def bfs(x, y, graph, queue, dx, dy):
  graph[x][y] = 1
  for i in range(4):
    new_x = x+dx[i]
    new_y = y+dy[i]
    
    # 상하좌우 인접한 노드 중 0인 경우 큐에 삽입
    if(0 <= new_x < N and 0<=new_y<M and graph[new_x][new_y]==0):
      queue.append((new_x, new_y))

  # 큐에 삽입된 노드 대상으로 bfs 재귀 
  while (queue):
    next = queue.popleft()
    graph = bfs(next[0],next[1],graph, queue, dx, dy)

  return graph

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
cnt = 0

for i in range(N):
  for j in range(M):
    if(graph[i][j] == 0):
      graph = bfs(i, j, graph, queue, dx, dy)
      cnt += 1

print(cnt)

  

end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
4 5
00110
00011
11111
00000
'''