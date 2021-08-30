from yahoo_fin import stock_info

brands=input("enter the company : ")
while True:
    price= stock_info.get_live_price(brands)
    print(price)
    if price < 3000:
        print("sell")
    elif price < 3450:
        print("invest")
    elif price > 4000:
        print("profit")
