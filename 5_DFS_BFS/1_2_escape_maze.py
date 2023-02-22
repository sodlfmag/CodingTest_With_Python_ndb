import sys
sys.setrecursionlimit(10**7)
import time
from pprint import pprint
'''
Point -
1. bfs를 진행하면서 바로 이전 노드까지의 최단거리를 이용한다.
2. (1, 1)을 제외하고는 네 방향 중 1을 초과하는 값 중 최솟값 +1 이 최단거리가 된다.
3. graph값을 계속 갱신해주고, 최종으로 (N,M) 의 값을 출력
'''
# 입력값 ----------

N, M = map(int, input().split())
graph = [[0]*(M+2)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
  temp = list(map(int, input()))
  graph.append([0] + temp + [0])
graph.append([0]*(M+2))

def bfs(x, y, old_x, old_y):
  if(graph[y][x]==1):
    graph[y][x] = graph[old_y][old_x] + 1
    
  if(graph[y][x] > 1):
    graph[y][x] = min(graph[old_y][old_x] +1, graph[y][x])

  for i in range(4):
    side = graph[y+dy[i]][x+dx[i]]
    if(side > 0 ):
      bfs(x+dx[i], y+dy[i], x, y)

bfs(1,1,0,0)
pprint(graph)
  
  
start_time = time.time()



# 알고리즘 실행 --------------------------------
end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
5 6
101010
111111
000001
111111
111111
-> 10
'''