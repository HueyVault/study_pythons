#k = int(input())

def cal_triangular (n):
    return int(n * (n + 1) / 2) 

for k in range(1,20):

    n = 1
    while True:
        Tn = cal_triangular(n)
        if Tn >= k :
            break
        n += 1

    if n % 2 ==0:
        print(f'{k}:{k-cal_triangular(n-1)}/{n+1-(k-cal_triangular(n-1))}')
    else:
        print(f'{k}:{n+1-(k-cal_triangular(n-1))}/{k-cal_triangular(n-1)}')
# n 단계 마다 거꾸로 해야함.
