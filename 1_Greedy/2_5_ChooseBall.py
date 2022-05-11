import time
'''
Point 
1. nC2 - (각 겹치는 nC2)
2. Sort해서 겹치는 개수 list 따로 만들어서 처리
'''

# nC2 를 구하는 함수
def comb2(a):
  result = a * (a-1) / 2
  return result

n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()
overlap_cases = []
current_w = 1000
cnt = 1
case_num = 0

# 알고리즘 실행 --------------------------------
start_time = time.time()

for i in range(len(balls)):
  if balls[i] == current_w :     # 같은 무게 개수 세기
    cnt += 1
    if i == len(balls) - 1:      # 마지막 인덱스에 도달하면 겹치는 개수 저장(어차피 여긴 2개 이상)
      overlap_cases.append(cnt)
  else:
    if cnt > 1:                  # 다음 인덱스가 다른 무게일 때 이전 무게 겹치는 개수 저장
      overlap_cases.append(cnt)
    current_w = balls[i]
    cnt = 1

case_num = comb2(n)
for i in overlap_cases:
  case_num -= comb2(i)

print(int(case_num))

end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
0001100
-> 1

'''
