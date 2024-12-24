import random

def yearing():
    '''Задание 6'''
    BORDER = 1582
    yr = int(input('Введите год: '))
    if yr < BORDER:
        res = 'Слишком рано'
    elif yr % 400 == 0:
        res = f'{yr} - високосный'
    elif yr % 100 == 0:
        res = f'{yr} - невисокосный'
    elif yr % 4 == 0:
        res = f'{yr} - високосный'
    else:
        res = f'{yr} - невисокосный'
    print(res)


def nummy():
    '''задача 7'''
    i = 0
    while i < 1:
        num = int(input('введите от 1 до 999: '))
        if 1 <= num and num <= 999:
            i += 1

    if num // 10 == 0:
        num_num = 'цифра'
        res_num = num ** 2
    elif num // 100 == 0:
        num_num = 'двузначное число'
        res_num = (num // 10) * (num % 10)
    else:
        num_num = 'трёхзначное число'
        res_num = f'{num % 100 % 10}{num % 100 // 10}{num // 100}'
    print(f'{num_num}, {res_num}')


def pinetree():
    rws = int(input('\nколичество рядов: '))
    lnght = rws * 2 - 1
    for _ in range(1, rws + 1):
        strng = '*' * (_ * 2 - 1)
        spc = ' ' * (rws - _)
        print(f'{spc}{strng}{spc}')

    # for _ in range(1, rws + 1):
    #     strng = '*' * (_ * 2 - 1)
    #     print(strng.center(lnght, ' '))


def table_print():
    STRT = 2
    ND = 10
    FST = 2
    SCND = 9
    CLMN = 4
    RWS = int((SCND - FST + 1) / CLMN)
    for i in range(1, RWS+ 1):
        for j in range(STRT, ND + 1):
            for k in range(FST, FST + CLMN):
                print(f'{k:2d} X {j:2d} = {(k * j):2d}', end='\t\t')
            print()
        print()
        FST += CLMN

def triangle_verif(aa, bb, cc):
    '''д/з 1'''

    summ = aa + bb + cc
    a = min(aa, bb, cc)
    c = max(aa, bb, cc)
    b = summ - a - c
    if a + b > c:
        if a == b == c:
            print('равносторонний')
        elif a ==b or a == c or b == c:
            print('равнобедренный')
        else:
            print('разносторонний')
    else:
        print('не существует')

def verific(n):
    '''д/з 2'''

    vr = 0
    if n <= 0 or n > 100000:
        return print('неверное число')
    else:
        for i in range(1, round(n/2) + 1):
            if n%i == 0:
                vr += 1
    if vr <= 1:
        print('простое')
    else:
        print('составное')

def game():
    '''д/з 3'''

    tn = random.randint(0, 1000)
    print('GUESS ME!!!: ')
    for count in range(1, 11):
        i = int(input('Введите число: '))
        if i == tn:
            return print('YEEY!!!\nur try is', count)
        else:
            if count < 10:
                if i < tn:
                    print(f'nope. make it bigger.')
                else:
                    print(f'nope. make it smaller.')
    print('nope. u lose.')

'''задача 6'''
yearing()
yearing()
yearing()

'''задача 7'''
nummy()
nummy()
nummy()

"""задача 8"""
pinetree()
pinetree()
pinetree()

'''задача 9'''
table_print()

'''первая д/з задача'''
a = int(input('1 сторона: '))
b = int(input('2 сторона: '))
c = int(input('3 сторона: '))
triangle_verif(a, b, c)

'''вторая д/з задача'''
num = int(input('число: '))
verific(num)

'''третья д/з задача'''
game()