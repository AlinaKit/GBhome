import random
from itertools import count
from operator import index
from os.path import split


def short_with_set(data):
    ddt = set()
    data1 = []
    for i in data:
        dt = [i]
        ddt.update(dt)
    for i in ddt:
        data1.append(i)
    return data1

def long_with_list(data):
    data2 = []
    for i in data:
        if i not in data2:
            data2.append(i)
    return data2

def checking(dt):
    dt = str(dt)
    ddt = ''
    dddt = ''
    for _ in dt.split('.'):
        ddt = ddt + _
    for _ in ddt.split('-'):
        dddt = dddt + _
    if dt.isdecimal():
        dt = int(dt)
    elif (dddt).isdecimal():
        dt = float(dt)
        if dt % 1 == 0:
            dt = int(dt)
    elif not dt.islower():
        dt = dt.lower()
    else:
        dt = dt.upper()
    return  dt

def dicty(tpl):
    dct = {}
    for i in tpl:
        if type(i) in dct.keys():
            b = [i]
            # dct[type(i)] = [dct[type(i)]]
            dct[type(i)].append(i)
        else:
            a = {type(i): [i]}
            dct.update(a)
    return dct

def unduplicate(lst):
    dlt = []
    for _ in lst:
        if lst.count(_) > 1:
            dlt.append(_)
    for _ in dlt:
        lst.remove(_)
    return lst

def notevenindex(lst):
    indxs = []
    for i, j in enumerate(lst):
        if j % 2 == 1:
            indxs.append(i + 1)
    return indxs

def stringprint():
    startline = str(input('enter line: '))
    mssv = startline.split()
    mssv = sorted(mssv)
    maxx = len(max(mssv, key=len))
    i = 0
    for _ in mssv:
        i += 1
        print(i, _.rjust(maxx, ' '))

def countfun1(strng):
    dct = {}
    for i in strng:
        if i in dct.keys():
            b = dct[i] + 1
            dct[i] = b
        else:
            if i.isalpha():  # строка для подсчёта только букв (lower and upper), если убрать - будут считаться все символы
                a = {i: 1}
                dct.update(a)
    # return dict(sorted(dct.items(), key=lambda x: x[1]))  #  сортировка по количеству вхождений символа
    return dct

def countfun2(strng):
    dct = {}
    for i in strng:
        if i.isalpha():
            a = {i: strng.count(i)}
            dct.update(a)
    return dct

def tourquests(itms):
    lst = []
    indxs = []
    for k, v in itms.items():
        lst.append(set(v))  # lst.append(set(itms[k]))
        indxs.append(k)
    ans = set(lst[0])
    for i in range(1, len(lst)):
        ans = ans & lst[i]
    print(ans, 'eсть у всех')
    for i in lst:
        lstshrt = lst.copy()
        crrnt = lstshrt.pop(lst.index(i))
        crrntres = crrnt.copy()
        uncrrnt = lstshrt[0]
        for j in lstshrt:
            uncrrnt = uncrrnt & j
            crrnt = crrnt - (j)
        print(f'{crrnt} eсть только у {indxs[lst.index(i)]}')
        print(f'{uncrrnt - crrntres} eсть у всех, кроме {indxs[lst.index(i)]}')

def dupleonly(lst):
    dplies = []
    for i in lst:
        if i not in dplies:
            if lst.count(i) > 1:
                dplies.append(i)
    return dplies

def topten(bstr):
    lstr = ''
    for i in bstr:
        if i.isalpha() or i == ' ':
            lstr += i
    words = lstr.split()
    dct = {}
    for i in words:
        if i in dct.keys():
            b = dct[i] + 1
            dct[i] = b
        else:  # для того, чтобы убрать предлоги, можно добавить (if len(i) > 2:) или заменить else: на (elif len(i) > 2:)
            a = {i: 1}
            dct.update(a)
    dct = dict(reversed(sorted(dct.items(), key=lambda x: x[1])))
    dctans = {}
    k = 0
    for i, j in dct.items():
        if k < 10:
            a = {i: j}
            dctans.update(a)
            k += 1
        else:
            break
    print(dctans)

def varies(wth):


# '''1'''
# data = [1, 3, 5, 1, 2, 6, 5, 8, 3, 4, 2, 2, 2, 6, 1]
# data1 = short_with_set(data)
# data2 = long_with_list(data)
# print(data, '\n', data1, '\n', data2)

# '''2'''
# a = input('')
# a = checking(a)
# print(a, type(a))

# '''3'''
# tpl = (1, 0.2, 'jhfd', '', 'fklj', 2, 0.3, -5, ' ')
# dct = dicty(tpl)
# print(tpl, '\n', dct)

# '''4'''
# lst = [1, 0.2, 'jhfd', '', ' ', 1, 0.2, -5, ' ']
# lst = unduplicate(lst)
# print(lst)

# '''5'''
# nmbs = [1, 2, 3, 5, 6, 2, 8, 7, 1, 5, 4, 2, 3, 6, 3, 2, 5, 1, 8]
# nteven = notevenindex(nmbs)
# print(nmbs, '\n, nteven)

# '''6'''
# stringprint()

# '''7'''
# strng = input('enter line: ')
# nocount = countfun1(strng)
# yescount = countfun2(strng)
# print(strng, '\n', nocount, '\n', yescount)  # сoвпадёт так как порядок вхождения символов одинаковый

# '''8'''
# itemsfr = {
#     'Alex': ('tent', 'food', 'water', 'fireplace'),
#     'Bob': ('food', 'cloth', 'tent', 'compas'),
#     'Cindy': ('tent', 'water', 'cloth', 'clock')
# }
# tourquests(itemsfr)

# '''д/з 1'''
# dpls = ['1', 2, 3, 5, '6', '7', 8, 7, '1', 5, 4, 2, 3, '6', 3, 2, 5, 1, 8, 1]
# print(dupleonly(dpls))

# '''д/з 2'''
# bigstr = """Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[15] или па́йтон[16]) — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[1][17], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[18]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[1]. Необычной особенностью языка является выделение блоков кода отступами[19]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[18]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[1]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[1][18].
#
# Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование[1], метапрограммирование[2], функциональное программирование[1] и асинхронное программирование[3]. Задачи обобщённого программирования решаются за счёт динамической типизации[20][21]. Аспектно-ориентированное программирование частично поддерживается через декораторы[22], более полноценная поддержка обеспечивается дополнительными фреймворками[23]. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений программирование можно реализовать с помощью библиотек или расширений[24]. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью[1], полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[25], высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты[26]."""
# topten(bigstr)

'''д/з 3'''


'''д/з 4*'''

