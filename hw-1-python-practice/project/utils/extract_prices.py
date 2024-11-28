def extract_prices(products):
    price = []
    for i in products:
        price.append(i.price)
    return price
