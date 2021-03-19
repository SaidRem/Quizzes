from capitals import europe, asia, africa, america, australia
import random

COUNTRIES = [europe['Europe'], asia['Asia'], africa['Africa'], america['America'], australia['Australia']]

def cap_quiz_rus():
    print('Тест по столицам стран.\nВыберите часть света: ')
    print('Europe(0), Asia(1), Africa(2), America(3), Australia(4), All(5)')
    while True:
        try:
            num = int(input('Введите цифру: '))
            if num > 5 or num < 0:
                continue
            break
        except ValueError:
            pass
    if num == 5:
        country_caps = {}
        for c in COUNTRIES:
            country_caps.update(c)
    else:
        country_caps = COUNTRIES[num]
    countries_list = list(country_caps.keys())
    random.shuffle(countries_list)
    countries_amount = len(countries_list)
    score = [0, 0]

    while countries_list:
        n = random.randint(0, countries_amount)
        country = countries_list.pop(n)
        countries_amount -= 1
        player_choice = input(f'Столица гос-ва {country} ("q" для выхода)\n=> ')
        if player_choice == 'q': break
        if player_choice == country_caps[country]:
            score[0] += 1
            print('Совершенно верно!\n')
        else:
            score[1] += 1
            print(f'Неверно.\nПравильный ответ: {country_caps[country]}\n')
    print(f'Твой результат: \n{score[0]} - верных ответов \n{score[1]} - неверных ответов')
    input('Game over')


# TODO
# 1. Add mode 'world'
# 2. Exclude questions that encountered
# 3. Score count
# 4. Make seversal modes

if __name__ == '__main__':
    # cap_quiz_rus({**europe['Europe']})
    cap_quiz_rus()
