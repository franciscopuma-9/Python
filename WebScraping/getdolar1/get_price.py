def get_price(price,delta, column):
    buy = price[column].get_text(strip=True, separator=' ')
    list_buy = buy.split(' ')
    price = list_buy[0] + list_buy[1]
    text_delta = delta[column].get_text(strip=True, separator=' ')
    list_delta = text_delta.split(' ')
    delta=''
    for i in list_delta:
        delta+=i
    return [price, delta]
