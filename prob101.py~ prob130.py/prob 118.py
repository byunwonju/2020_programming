warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a= str(input("종목 명을 입력하세요:"))

if a in warn_inverstment_list:
    print("투자 경고 종목이 아닙니다.")
else:
    print("투자 경고 종목입니다.")
