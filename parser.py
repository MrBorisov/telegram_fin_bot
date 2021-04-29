def p_message(message):
    print(message)
    x = message.split('. ')
    category = x[3]
    price = x[2].split(' ')[0]
    return (category, price)