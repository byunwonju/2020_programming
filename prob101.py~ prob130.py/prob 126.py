number = input('우편번호: ')

#number[2] in "012" 

if 0<= int(number[2]) <3:

    print('강북구')

#number[2] in "345"

elif 3 <= int(number[2]) <6:

    print('도봉구')

#number[2] in "6789"  or else

elif 6 <= int(number[2]) <10:

    print('노원구')



