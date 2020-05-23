number = input('주민등록번호: ')
check = int(number[number.find('-')+1])
#number[7] in ['1','3']
if check == 1 or check == 3:
    print('남자')
else :

    print('여자')


