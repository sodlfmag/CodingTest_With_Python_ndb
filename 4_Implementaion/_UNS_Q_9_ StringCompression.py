import time
'''
Point 
1. 1개부터 n//2 + 1 까지 잘라서 자른 결과를 리스트에 담고 최소값 인덱스 찾기
2. 자르는 것이 불가능한 경우는 문자열 길이로 저장

'''

s = input()
length = len(s)
str_cnt = [0] * length + 1
str_cnt[0] = length
over_case = []
over_cnt = [1] * length
cur_case = ''
unit = 1

while unit < (n // 2 + 2):
  cur_loc = 0
  while cur_loc < length - unit:   # 
    over_case.append(s[cul_loc : cul_loc + unit])
    cul_loc += unit
  if cul_loc + 1 < length:         # 뒷 부분이 다른 경우
    over_case.append(over_case[cul_loc :])
    
  cul_case = over_case[0]  
  cul_index = 0
  for i in range(1, len(over_case)):
    if (over_case[i] == cul_case):
      over_cnt 
      
      
  unit += 1
  
  
  
str


# 알고리즘 실행 --------------------------------
start_time = time.time()



end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시

'''