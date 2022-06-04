import time
'''
Point
1. 1시간에 몇개의 3이 들어가는지 계산하고 배수. 예외 - 시간에 3이 들어가는 경우
2. 3이 들어가는 경우는 큰 경우로 생각 - 시각에 3이 들어가면 1시간은 전부,
십분에 들어가면 10분동안은 전부, 분에 들어가면 1분동안 전부,
3. 1시간은 00.00 ~ 59.59 까지 총 3600 개 수. 
4. 10초에 1개, 60초(1분)에 10 + 6 - 1 = 15개
5. 10분에 60 + 15* (10 - 1)   = 195개
6. 60분에 600 + 195 * (6 - 1) = 1575개
7. 예외 - 시간에 3이 들어간 경우 - 1시간 내내 포함 = 3600개
8. 0~N 시간까지 3이 들어가는 경우는 3600, 아닌 경우는 1575개 더하기

'''
result = -1
n = int(input())

# 알고리즘 실행 --------------------------------
start_time = time.time()


if(n < 3):
  result = 1575 * (n+1)
elif( 3 <= n < 13):
  result = 3600 + 1575 *(n)
elif(13 <= n < 23):
  result = 3600 * 2 + 1575 *(n-1)
elif (n == 23):
  result = 3600 *3 + 1575 * (n-2)

print(result)

end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
5
-> 11475

'''