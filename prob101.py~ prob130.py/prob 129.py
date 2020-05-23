number = input('주민등록번호: ')
my_sum = int(number[0])*2
my_sum += int(number[1])*3
my_sum += int(number[2])*4
my_sum += int(number[3])*5
my_sum += int(number[4])*6
my_sum += int(number[5])*7
my_sum += int(number[7])*8
my_sum += int(number[8])*9
my_sum += int(number[9])*2
my_sum += int(number[10])*3
my_sum += int(number[11])*4
my_sum += int(number[12])*5
my_sum = 11-(my_sum%11)
if int(number[13]) == my_sum:
    print('유효한 주민등록번호입니다.')
else :
    print('유효하지 않은 주민등록번호입니다.')



