input_hour, input_minute = map(int, input().split())
input_end = int(input())

'''
input_end를 일단 분단위로 나눔
분끼리 더하고 59 처리함
그 다음 시끼리 더하고 23 처리함

1000/60 = 16.40


'''
minute = 60
quotient, remainder = divmod(input_end, minute)

cal_minute = input_minute + remainder
if cal_minute > 59 :
    cal_minute -= minute
    input_hour += 1
cal_hour = input_hour + quotient
if cal_hour > 23:
    cal_hour -= 24

print(cal_hour,cal_minute)
