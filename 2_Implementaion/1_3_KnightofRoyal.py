import time
'''
Point
1. 나이트가 움직일 수 있는 위치는 상하좌우로 남아있는 줄의 개수에 영향을 받음.
2. 1줄, 2줄 겹치는 경우, 안 겹치는 경우 나눠서 트리를 만들어 경우를 3 * 3으로 나눔
'''

possible = -1
location = input()
dx = ord(location[0]) - ord('a') + 1
dy = int(location[1])

xf = 2 < dx < 7              # x가 아무데도 안 걸치는경우
yf = 2 < dy < 7               # y가 아무데도 안 걸치는경우
x1 = (dx == 2 or dx == 7)    # x가 1줄 걸치는 경우
x2 = (dx == 1 or dx == 8)    # x가 2줄 걸치는 경우
y1 = (dy == 2 or dy == 7)    # y가 1줄 걸치는 경우
y2 = (dy == 1 or dy == 8)    # y가 2줄 걸치는 경우

# 알고리즘 실행 --------------------------------
start_time = time.time()

if x1:
  if yf:
    possible = 6
  elif y1:
    possible = 4
  elif y2:
    possible = 3
elif x2:
  if yf:
    possible = 4
  elif y1:
    possible = 3
  elif y2:
    possible = 2
elif xf:
  if yf:
    possible = 8
  elif y1:
    possible = 6
  elif y2:
    possible = 4
  

print(possible)
print(dx , dy)
end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
a1
-> 2

'''
