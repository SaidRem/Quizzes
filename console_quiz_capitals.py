from capitals import europe
import random


def cap_quiz_rus(country_caps):
    countries_list = list(country_caps.keys())
    random.shuffle(countries_list)
    countries_amount = len(countries_list)

    for _ in range(10):
        n = random.randint(0, countries_amount)
        player_choice = input(f'Столица гос-ва {countries_list[n]}')
        if player_choice == country_caps[countries_list[n]]:
            print('Совершенно верно!')
        else:
            print(f'Неверно.\nПравильный ответ{country_caps[countries_list[n]]}')
    input('Game over')


# TODO
# 1. Add other continents 
# 2. Exclude questions that encountered
# 3. Score count
# 4. Make seversal modes

if __name__ == '__main__':
    cap_quiz_rus({**europe['Europe']})
