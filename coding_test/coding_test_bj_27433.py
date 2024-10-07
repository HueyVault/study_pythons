number = int(input())

def func(num):
    if num:
        return func(num-1) * num 
    else :
        return 1
    
print(func(number))
