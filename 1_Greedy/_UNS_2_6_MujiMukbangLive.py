def solution(food_times, k):
    cur_loc = 0
    for i in range(k):
        if max(food_times) == 0:
                return -1
        while True:
            # 값이 0인 경우 다음 음식으로이동
            if food_times[cur_loc] == 0:
                cur_loc += 1
            # 0인경우인데 마지막 음식이었을 경우 첫번째로 이동
                if cur_loc == len(food_times):
                    cur_loc = 0
            else:
            # 값이 0이 아닌 경우
                food_times[cur_loc] -= 1
                cur_loc += 1
                if cur_loc == len(food_times):
                    cur_loc = 0
                break
    if max(food_times) == 0:
        return -1
    answer = cur_loc + 1
    return answer
