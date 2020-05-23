vv = int(btc["min_price"]) - int(btc["max_price"])
opening_price = int(btc["opening_price"]) + vv

if opening_price > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
