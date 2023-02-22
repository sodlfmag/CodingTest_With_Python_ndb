import time
from bisect import bisect_right

'''
Point -
1. 절단기 높이는 리스트의 가장 큰 값부터 설정해 줄여나간다.
2. 끝 점에서 중간점까지 뺐을 때의 값을 통해 이진 탐색을 수행한다.
3. 정확한 값을 찾는 경우 종료하고, 그렇지 못한 경우는 실패하기 전 마지막 중간값을 반환한다.

'''
# 입력값 ----------
N, M = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort()
print(rice)

start_time = time.time()
total = sum(rice)
H = max(rice)


def bs(start, end):

  
  mid = (start + end) //2
  point = N - bisect_right(rice, mid)
  print(mid)
  print(point)
  print(rice)
  if(total - (mid * point) == M):
    return mid
    
  elif(total - (mid * point) < M):
    bs(start, mid-1)

  elif(total - (mid * point) > M):
    if(total - ((mid+1) * point) <= M):
      return mid+1
    bs(mid+1, end)

print(H)

print(bs(0, H))



# 알고리즘 실행 --------------------------------
end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시

'''