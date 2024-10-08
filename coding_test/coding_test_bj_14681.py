input_x = int(input())
input_y = int(input())


if input_x > 0 and input_y > 0 :
    print('1')
elif input_x < 0 and input_y > 0 :
    print('2')
elif input_x < 0 and input_y < 0 :
    print('3')
else :
    print('4')

