number = input('주민등록번호: ')
check = int(number[number.find('-')+2:number.find('-')+4])
#int(number[8:9]) <= 8
if 1 <= check <= 8:
    print('서울 입니다.')
else :
    print('서울이 아닙니다.')



