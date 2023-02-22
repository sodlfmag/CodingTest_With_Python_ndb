import time
'''
Point -
1. 0부터 시작해서 오른쪽의 각 수가 0 또는 1인 경우만 더해줌
2. 0, 1이 아닌 경우는 곱해줌

'''

total = 0
str = input()
splt_str = []

for i in range(len(str)):
  splt_str.append(int(str[i]))

for val in splt_str:
  if (val <= 1 or total == 0):
    total += val
  
  else:
    total *= val

print(total)

# 알고리즘 실행 --------------------------------
start_time = time.time()



end_time = time.time()
print("time :", "%.4f"%(end_time - start_time))

'''
입출력 예시
02984
-> 576

567
-> 210
'''