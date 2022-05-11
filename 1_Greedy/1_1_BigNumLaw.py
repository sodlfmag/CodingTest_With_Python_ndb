import time


N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

start_time = time.time()
sum = 0
cnt = 0
# 가장 큰 수
first = max(numbers)
numbers.remove(first)
# 두 번째로 큰 수
second = max(numbers)

for i in range(M):
  # K번 최댓값 더했을 때 second 더해주고 cnt 초기화
  if(cnt == K):
    sum += second
    cnt = 0
  # 최댓값 더해주기
  else:
    sum += first
    cnt += 1

print(sum)
    

end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))