import time
'''
Point - 
1. N이 K로 나누어 떨어지면 나누기
2. N이 K로 나누어 떨어지지 않으면 %연산한 만큼 빼기
3. 1의 경우 cnt에 1, 2의 경우 cnt에 나머지 값만큼 더하기
4. N이 1이 되는 경우 종료
'''
  
cnt = 0
N, K = map(int, input().split())

while(N != 1):
  if(N % K == 0):
    N /= K
    cnt += 1

  else:
    cnt += N % K
    N -= N % K
    

print(cnt)

# 알고리즘 실행 --------------------------------
start_time = time.time()



end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
25 5
-> 2
'''