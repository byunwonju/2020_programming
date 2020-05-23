a= ["A","B","C","D","E"]
b= int (input("정수를 입력해주세요.:"))

if b>=81:
    print("grade is", a[0])
elif b>= 61:
    print("grade is", a[1])
elif b>= 41:
    print("grade is", a[2])
elif b>= 21:
    print("grade is", a[3])
else:
    print("grade is", a[4])
