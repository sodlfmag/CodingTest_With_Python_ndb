import time

# 입력값 ----------
str = input()
x, y = str[0], int(str[1])


start_time = time.time()
'''
Point -
1. x 좌표를 숫자로 변경함
2. 8방향을 모두 검사해서 (1, 1) ~ (8, 8) 내에 존재하는지 카운트함
'''

cnt = 0
x = ord(x) - ord('a') + 1

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

for i in range(8):
  point_x = x + dx[i]
  point_y = y + dy[i]

  if(1<=point_x<=8 and 1<=point_y<=8):
    cnt += 1

print(cnt)

# 알고리즘 실행 --------------------------------
end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시

'''