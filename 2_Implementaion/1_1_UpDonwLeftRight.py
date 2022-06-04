import time
'''
Point 
1. 각 알파벳 입력으로 방향 선택
2. 범위 벗어나는 이동은 무시하는 조건 - x,y 값이 0보다 커야 하고, n보다 작거나 같아야 함

'''
n = int(input())
move = list(map(str, input().split()))
location = [1, 1]
# 알고리즘 실행 --------------------------------
start_time = time.time()

for dir in move:          # 입력된 UDRL 각각 값 변경
  temp = location[:]
  if dir == 'U':
    temp[0] -= 1
  elif dir == 'D':
    temp[0] += 1
  elif dir == 'R':
    temp[1] += 1
  elif dir == 'L':
    temp[1] -= 1

  if(temp[0] < 1 or temp[1] < 1 or temp[0] > n or temp[1] > n ):
    continue              # 값 변경 후 x,y 가 0보다 작거나 n보다 큰 경우는 무시
  else:
    location = temp[:]    # 위 조건에 해당하지 않는 경우는 변경값 반영

print(location[0], location[1])

end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
5
R R R U D D
-> 3 4

'''
