import time
'''
Point 
- N % K -> 1씩 뺄 횟수
- N // K -> K로 나눈 뒤 값
-> 1이 될 때까지 수행

'''

n, k = map(int, input().split())
cnt = 0

# 알고리즘 실행 --------------------------------
start_time = time.time()

while True:
  # n == 1 인 경우 반복문 탈출
  if n == 1:
    break
    # n >= k 인 경우 나머지 만큼 빼주고, K로 1번 나눠줌
  elif n >= k:
    cnt += n % k + 1
    n = n // k
    # n < k 인 경우 n - 1번 1을 빼 줌
  elif n < k:
    cnt += n - 1
    n = 1

print(cnt)

end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
25 5
-> 2
'''