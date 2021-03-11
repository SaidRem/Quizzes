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

    for _ in range(10):
        n = random.randint(0, countries_amount)
        player_choice = input(f'Столица гос-ва {countries_list[n]}\n=> ')
        if player_choice == country_caps[countries_list[n]]:
            print('Совершенно верно!\n')
        else:
            print(f'Неверно.\nПравильный ответ: {country_caps[countries_list[n]]}\n')
    input('Game over')


# TODO
# 1. Add mode 'world'
# 2. Exclude questions that encountered
# 3. Score count
# 4. Make seversal modes

if __name__ == '__main__':
    # cap_quiz_rus({**europe['Europe']})
    cap_quiz_rus()
