input_time, input_minute = input().split()
input_time = int(input_time)
input_minute = int(input_minute)
input_end = int(input())

'''
input_end를 일단 분단위로 나눔
분끼리 더하고 59 처리함
그 다음 시끼리 더하고 23 처리함

'''


cal_minute = input_minute + input_end
if cal_minute > 59 :
    cal_minute = 0
    input_time += 1
    if input_time > 23:
        input_time = 0
