in_money = input('입력: ')

money = float(in_money[:in_money.find(' ')])

check = in_money[in_money.find(' ')+1:len(in_money)]

if '달러' == check:

    print(money*1167,'원')

elif '엔' == check:

    print(money*1.096,'원')

elif '유로' == check:

    print(money*1268,'원')

elif '위안' == check:

    print(money*171,'원')
