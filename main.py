# QAP-105 Задание 18.8.19 (HW-03)

DISCOUNT = 10  # 10 = 10%
TICKETS_DISCOUNT = 3
PRICE_MIN = 990
PRICE_FULL = 1390
order_price = 0.0
order_discount = 0.0


def get_int(prompt):
    while True:
        value = 0
        try:
            value = int(input(prompt))
        except ValueError:
            print('\033[31mПри вводе данных необходимо использовать только цифры!\033[0m\n')
            continue
        if value < 0:
            print('\033[31mОтрицательные числа не принимаются\033[0m\n')
            continue
        else:
            break
    return value


print('\u250c' + '\u2500' * 67 + '\u2510')
print('\u2502 \033[1;4;32mПрограмма подсчета общей стоимости билетов для онлайн-конференции\033[0m \u2502')
print('\u2514' + '\u2500' * 67 + '\u2518')
print(f'Помните что при заказе от \033[31m{TICKETS_DISCOUNT}-х\033[0m билетов действует скидка ',
      f'в \033[31m{DISCOUNT}%\033[0m на весь заказ\n')
print('\033[1;31m*** ВАЖНО! При вводе данных используйте только цифры! ***\033[0m\n')

tickets = get_int('Введите количество билетов для приобретения (0 - для выхода):')
print()

if tickets:
    for i in range(1, tickets + 1):
        age = get_int(f'Введите возраст {i}-го посетителя:')
        if age < 18:
            print('Этот посетитель проходит на конференцию бесплатно\n')
        elif age < 25:
            print(f'Цена билета для этого посетителя равна {PRICE_MIN} руб.\n')
            order_price += PRICE_MIN
        else:
            print(f'Цена билета для этого посетителя равна {PRICE_FULL} руб.\n')
            order_price += PRICE_FULL

    print('\u2500' * 45)
    print(f'Общая стоимость заказа: {order_price} руб.\n')
    if tickets >= TICKETS_DISCOUNT:
        order_discount = order_price * DISCOUNT / 100
        print(f'Ваша скидка: {order_discount} руб.\n')
        print(f'\033[1mИтоговая цена со скидкой: \033[1;32m{order_price - order_discount} руб.\033[0m')
    print('\u2500' * 45)

else:
    print('Спасибо за использование программы.\n')
