import time
'''
Point 
1. 남은 인원 중 공포도가 높은 사람 기준으로 인원 세기
2. max 공포도가 리스트 길이보다 크면 종료


'''
n = int(input())
adven = list(map(int, input().split()))
remain = []
coward = 0
cnt = 0
group_num = 0
# 알고리즘 실행 --------------------------------
start_time = time.time()
# 역순 정렬 해서 맨 앞에 공포도 최댓값이 오게 함
adven.sort()
remain = adven[:]
# 겁쟁이에 remain 첫 번째 요소 
coward = remain[0]

while True:
  for i in adven:
    if i <= cnt:
      group_num += 1
      cnt = 0
    else:
      cnt += 1

print(cnt)

end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
5 
2 3 1 2 2
-> 2
'''
