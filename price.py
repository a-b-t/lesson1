
def get_summ(one, two, delimiter = '&'):
    sum = str(one) + delimiter + str(two)
    return sum

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

b = format_price(56.24)
print(b)


a = get_summ('Learn', 'python').upper()
print(a)