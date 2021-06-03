def p_message(message):
    err = False
    x = message.split('. ')
    category = x[3]
    price = x[2].split(' ')[0]
    # проверим переменную price
    try:
        float(price)
    except ValueError:
        err = True
    if err:
        return category, price, err

    return category, float(price), err
