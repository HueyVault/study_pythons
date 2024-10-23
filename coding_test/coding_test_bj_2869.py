A, B, V = map(int, input().split())

'''
100 99 1000000000
일 때 루프 너무 많이 돔 

'''

# dist = 0
# day = 0
# while True :
#     dist += A
#     day += 1
#     if V > dist :
#         dist -= B
#     else :
#         break

# V > A * day - B * (day-1)
# A 5 B 1 V 6
# (V-A) % (A-B) == 0 
# (V-A) // (A-B) + 1
# (V-A) % (A-B) != 0
# (V-A) // (A-B) + 2

day = 0
if (V-A) % (A-B) == 0:
    day = (V-A) // (A-B) + 1
else:
    day = (V-A) // (A-B) + 2
print(day)