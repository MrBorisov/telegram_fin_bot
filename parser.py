def p_message(message):
    err = False
    x = message.split('. ')
    category = x[3]
    price = x[2].split(' ')[0]
    """
    тут пробуем проверить парсер, если он непавильно сработал, то в переменной price
    будет не число и мы получем исключение и вернем все что распарсили и true
    """
    try:
        float(price)
    except ValueError:
        err = True
    if err:
        return category, price, err
    else:
        return category, float(price), err