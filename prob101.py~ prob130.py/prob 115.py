#사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.

a= int(input("값을 입력하세요.:")
if(a>=0 and a<=255):
       a=(a-20)
       if (a<=255):
           print("0")
       else:
           print(a)
else:
    print("0-255 사이의 값을 입력하세요.")
