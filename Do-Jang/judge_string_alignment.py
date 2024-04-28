price_input = map(int, input().split(';'))

prices = sorted(price_input, reverse=True)

for price in prices:
    formatted_price = '{:>9,d}'.format(price)
    print(formatted_price)
