import time
'''
Point
1. 하나하나 잘라서 알파벳 / 숫자 분리
2. 알파벳은 리스트에 따로 넣어서 sort로 오름차순 처리 -> 아스키로 처리
3. 숫자는 ord('A')보다 작은 조건으로 넣고 따로 숫자 sum 변수에 누적하도록

'''
str = input()
sum = 0
alpha =[]
# 알고리즘 실행 --------------------------------
start_time = time.time()

for val in str:
  if(ord(val) < ord('A')):     # 숫자인 경우
    sum += int(val)
  else:
    alpha.append(val)

alpha.sort()
for i in alpha:
  print(i,end='')
print(sum)

end_time = time.time()
print("time :", "%.4f" % (end_time - start_time))

'''
입출력 예시
K1KA5CB7
-> ABCKK13

AJKDLSI412K4JSJ9D
-> ADDIJJJKKLSS20

'''
