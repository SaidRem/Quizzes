import sys
import random
from capitals import europe, asia, africa, america, australia
import random


COUNTRIES = [europe['Europe'], asia['Asia'], africa['Africa'], america['America'], australia['Australia']]

def cap_quiz():
    """
    Тест по столицам мира.
    World capitals test.
    """
    print('Тест по столицам стран.\nВыберите часть света: ')
    print('Europe(0), Asia(1), Africa(2), America(3), Australia(4), All(5)')
    while True:
        c = []
        try:
            num = input('Введите цифру или последовательность цифр: ')
            for i in num:
                if int(i) > 5 or int(i) < 0:
                    continue
                c.append(int(i))
            break
        except ValueError:
            pass
    country_caps = {}
    if num == 5:
        for i in COUNTRIES:
            country_caps.update(i)
    else:
        for i in c:
            country_caps.update(COUNTRIES[i])

    countries_list = list(country_caps.keys())
    random.shuffle(countries_list)
    countries_amount = len(countries_list)
    score = [0, 0]

    while countries_amount:
        n = random.randint(0, countries_amount-1)
        country = countries_list.pop(n)
        countries_amount -= 1
        player_choice = input(f'Столица гос-ва {country} (ввод "q" для выхода)\n=> ')
        if player_choice == 'q': break
        if player_choice == country_caps[country]:
            score[0] += 1
            print('Совершенно верно!\n')
        else:
            score[1] += 1
            print(f'Неверно.\nПравильный ответ: {country_caps[country]}\n')
    print(f'Твой результат: \n{score[0]} - верных ответов \n{score[1]} - неверных ответов')
    input('Game over')


if __name__ == '__main__':
    # cap_quiz()
    total = 0
    for c in COUNTRIES:
        total += len(c)
    print(total)
