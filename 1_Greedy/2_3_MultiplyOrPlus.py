import time
'''
Point 
1. 0과 1 중 뭉텅이 개수가 뭐가 적은 지
2. 적은 개수 출력

'''

s = input()
l = len(s)
current_s = '' # 이전 뭉텅이 값 저장
cnt0 = 0
cnt1 = 0
# 알고리즘 실행 --------------------------------
start_time = time.time()

for i in s:
  if i == current_s:      # 이전 값과 동일한 경우 continue
    continue
  elif i == '0':          # 이전은 1 다음은 0 인 경우
    cnt0 += 1
  elif i == '1':          # 이전은 0 다음은 1 인 경우
    cnt1 += 1
  current_s = i           # 이전 / 다음 값 다른 경우 최신화

result = min(cnt0, cnt1)
print(result)


end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
0001100
-> 1

'''
