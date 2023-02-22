import time
start_time = time.time()
'''
Point -
1. 방향벡터를 설정
2. N X N을 벗어나는 이동은 무시
3. case를 이용해 방향벡터 적용

'''

# D R U L 순 방향벡터
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

x, y = 1, 1
temp_x, temp_y = 0, 0

N = int(input())
moves = list(input().split())

directions = {'D':0, 'R':1, 'U':2, 'L':3}

for move in moves:
  temp_x = x + dx[directions[move]]
  temp_y = y + dy[directions[move]]

  if(1<= temp_x<=N and 1<= temp_y <= N):
    x, y = temp_x, temp_y

print(x, y)

    
    


# 알고리즘 실행 --------------------------------
end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시

'''