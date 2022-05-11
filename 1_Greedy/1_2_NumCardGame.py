import time

'''
Point - 각 행의 최솟값들 중 최댓값이 무엇인가
다 필요없고 값만 구하면 됨
'''
n, m = map(int, input().split())
max_rowval = 0

start_time = time.time()

for i in range(n):
  cards_row = list(map(int, input().split()))
  # i번 행에서 최솟값 저장
  min_val = min(cards_row)
  # 행당 최솟값 중 최댓값 최신화
  max_rowval = max(max_rowval, min_val)


# 최댓값 출력
print(max_rowval)

end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
3 3 
3 1 2 
4 1 4 
2 2 2
-> 2

2 4
7 3 1 8
3 3 3 4
-> 3
'''
