import math
import fractions
from sys import getsizeof


def cheking(*args):
    for _ in args:
        print(_, '=', type(_))

def listing(list):
    for i, st in enumerate(list):
        print(f'индекс: {i + 1}')
        print(f'значение: {st}')
        print(f'адрес: {id(st)}')
        print(f'размер: {getsizeof(st)}')
        print(f'хэш: {hash(st)}')
        if type(st) == type(1): print('int: ', True)
        if type(st) == type('fgh'): print('str: ', True)
        print()

def octobini():
    num = int(input('число: '))
    mod = num
    now = num
    num2 = ''
    num8 = ''
    if num == 0:
        num2 = '0'
        num8 = '0'
    else:
        while mod >= 1:
            num2 = str(int(mod % 2)) + num2
            if mod % 2 == 0:
                mod /= 2
            else:
                mod = (mod - 1) / 2

        while now >= 1:
            num8 = str(int(now % 8)) + num8
            if now % 8 == 0:
                now /= 8
            else:
                now = (now - now % 8) / 8

    print(f'{num2 = }, {bin(num) = }')
    print(f'{num8 = }, {oct(num) = }')


def sl():
    i = 0
    if i < 1:
        d = int(input('diameter: '))
        if 0 < d and d <= 1000:
            i += 1
    s = math.pi * (d / 2) ** 2
    l = 2 * math.pi * (d / 2)
    print(f's = %.42f' % s)
    print(f'l = %.42f' % l)


def resolver():
    a = float(input('коэффициент для х^2: '))
    b = float(input('коэффициент для х: '))
    c = float(input('коэффициент для const: '))
    d = b ** 2 - 4 * a * c
    if d == 0:
        x = -1 * b / (2 * a)
        print(round(x, 3))
    elif d > 0:
        x1 = -1 * (b - math.sqrt(d)) / (2 * a)
        x2 = -1 * (b + math.sqrt(d)) / (2 * a)
        print(round(x1, 3), round(x2, 3))
    else:
        x1 = complex((-1 * (b) / (2 * a)), ( -1 * math.sqrt(abs(d)) / (2 * a)))
        x2 = complex((-1 * (b) / (2 * a)), ( math.sqrt(abs(d)) / (2 * a)))
        print(f'{round(x1.real, 3)}{round(x1.imag, 3)}, {round(x2.real, 3)}+{round(x2.imag, 3)}')

def cash_machine():
    op = 0
    i = 0
    global money
    while op < 3:
        if i == 3:
            i = 0
        if money > 5000000:
            '''выполняется перед операциями, в т. ч. перед выходом и при пустом вводе'''
            money = money - (money / 10)
            print('налог на роскошь, баланс:', money)
        else:
            print('balance:', money)
        x = input('1 - пополнить, 2 - снять, 3 - выйти: ')
        op = int(x if x.isdecimal() else 0)
        if op == 1:
            delta = 1
            while delta % 50 != 0:
                y = input('введите верную сумму пополнения (шаг 50 у.е.): ')
                delta = int(y if y.isdecimal() else 0)
            if delta > 0:
                money += delta
                i += 1
                if i == 3:
                    money = money + (money / 100 * 3)
        elif op == 2 and money < 50.75:
            '''уточнение 50,75 необходимо для учёта комиссии при снятии'''
            print('недостаточно средств')
        elif op == 2:
            delta = 1
            while delta % 50 != 0 or delta >= (money * 1.015):
                y = input('введите верную сумму снятия (шаг 50 у.е.): ')
                delta = int(y if y.isdecimal() else 0)
            if delta > 0:
                perc = (delta / 100 * 1.5)
                money = money - delta - min(600, max(30, perc))
                i += 1
                if i == 3:
                    money = money + (money / 100 * 3)
        elif op == 3:
            return print('balance:', money)
        else:
            print('неверная операция')


def hexini():
    num = int(input('число: '))
    now = num
    num16 = ''
    if num == 0:
        num16 = '0'
    else:
        while now >= 1:
            num16 = str(int(now % 16)) + num16
            if now % 16 == 0:
                now /= 16
            else:
                now = (now - now % 16) / 16
    print(f'{num16 = }, {hex(num) = }')

def fracty():
    x = (input() or '1/1').split('/')
    y = (input() or '1/1').split('/')
    for i in (0, 1):
        x[i] = int(x[i])
        y[i] = int(y[i])
    sm = (x[0] * y[1] + x[1] * y[0]) / (x[1] * y[1])
    mlt = (x[0] * y[0]) / (x[1] * y[1])
    mod_x = fractions.Fraction(x[0], x[1])
    mod_y = fractions.Fraction(y[0], y[1])
    mod_sm = mod_x + mod_y
    mod_mlt = mod_x * mod_y
    print(f'{sm = } = {mod_sm}\n{mlt = } = {mod_mlt}')

'''задача 1'''
a = 3
b = 'fgh'
c = 3.3
cheking(a, b, c)

'''задача 2'''
data = [a, b, c]
listing(data)
data = [3, 'fgh', 3.3, 'fgh', 3]
listing(data)

'''задача 3'''
octobini()

'''задача 4'''
sl()

'''задача 5'''
resolver()

'''задача 6'''
money = 0
cash_machine()
cash_machine()
cash_machine()

'''д/з задача 1'''
hexini()

'''д/з задача 2'''
fracty()