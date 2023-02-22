import time
'''
Point
1. 문자열을 반 자른 다음 하나씩 요소 꺼내서 int 전환 후 계산

'''
front = 0
back = 0

n = input()
half = (len(n) // 2) - 1      # 0부터 시작하는 인덱스 번호 중간

for i in range(half + 1):     # 실제 절반 횟수
  front += int(n[i])          # 절반까지 더함
  back += int(n[half+i+1])    # 절반 다음 것부터 더함

if front == back:
  print('LUCKY')
else:
  print('READY')

# 알고리즘 실행 --------------------------------
start_time = time.time()


end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
123402
-> LUCKY

7755
-> READY
'''
