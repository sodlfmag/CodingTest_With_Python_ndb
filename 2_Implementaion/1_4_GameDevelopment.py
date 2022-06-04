import time
'''
Point
1. 방향 변수 -> 원래 숫자로 다시 돌아오면 뒤로가는 조건 수행
2. 가본 곳은 숫자 2로 처리 
3. 4 방향이 1 또는 2인 경우 방향변수 반대 방향으로 이동
4. 반대방향이 1인 경우 종료.

'''
cnt = 0
next = [0, 0]
back = [0, 0]
n, m = map(int, input().split())
loc = [0,0]
loc[0], loc[1], d = map(int,input().split())
map1 = [[0]*m for _ in range(n)]

for i in range(n):
  temp = list(map(int, input().split()))
  map1[i] = temp[:]

# for i in range(n):                # 초기 맵 상태 출력
#   print(map1[i])

map1[loc[0]][loc[1]] = 2                # 초기 위치 방문처리
move = [(-1,0), (0,1), (1, 0), (0,-1)] # 북 동 남 서 

# 알고리즘 실행 --------------------------------
start_time = time.time()

def turn90(direction):
  if(direction == 3):
    direction = 0
  else:
    direction += 1
  
  return direction
  
while cnt <= 4:
  d = turn90(d)
  cnt += 1
  next[0], next[1] = loc[0] + move[d][0], loc[1] + move[d][1] # 앞 쪽 위치 저장  
  if(map1[next[0]][next[1]] == 0):  # 앞이 안 가본 곳인 경우
    loc = next[:]
    map1[loc[0]][loc[1]] = 2
    cnt = 0
  elif(map1[next[0]][next[1]] >= 1):    # 앞이 바다나 가 본 곳인 경우
    if(cnt == 4):
      bd = turn90(d)
      bd = turn90(bd)                   # 180도 방향이 뒷 방향
      back[0], back[1] = loc[0] + move[bd][0], loc[1] + move[bd][1] # 뒤 쪽 위치 저장
      if(map1[back[0]][back[1]] == 1):   # 뒤가 바다인 경우 종료
        break
      elif(map1[back[0]][back[1]] == 2): # 뒤가 가본 곳인 경우 
        next = loc[:]
        loc = back[:]
        cnt = 0

# for i in range(n):                     # 유저 멈춘 후 맵 상태 출력
#   print(map1[i])
        
result = 0
for i in map1:
  for val in i:
    if val == 2:
      result += 1

print(result)


end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
-> 3

'''
