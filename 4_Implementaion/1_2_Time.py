import time

# 입력값 ----------
N = int(input())

start_time = time.time()
'''
Point -
1. 03시, 13시, 23시를 제외하면 1시간 단위에 3이 포함되는 경우의 수는 같음
2. 초에 3이 들어가는 경우 15 * 60
3. 분에 3이 들어가는 경우 15 * 60
4. 초와 분에 3이 모두 들어가는 경우 15 * 15
5. 3) + 4) - 5) = 15 * 105 = 1575
'''

result = 0

if(N < 3):
  result = 1575 * (N+1)

elif(3<= N < 13):
  result = 1575 * N + 3600

elif(13 <= N < 23):
  result = 1575 * (N-1) + 7200

elif(N == 23):
  result = 1575 * (N-2) + 10800

print(result)
  
  


# 알고리즘 실행 --------------------------------
end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시

'''