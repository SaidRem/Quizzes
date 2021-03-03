from capitals import europe, asia
import random
from quiz_world_cap import eurasia

# Generate 10 quiz files.
def quizes_rus(country_capit):
    """
    Creates files with quizzes and answers.
    """
    for num_quiz in range(1, 11):

        # Creating the quiz and answer key files
        
        # answer_key = open(f'capitals_quiz_answers{num_quiz}', 'w')
        with open(f'capitals_quiz{num_quiz}.txt', 'w', encoding='utf-8') as quiz_file, \
             open(f'capitals_quiz_answers{num_quiz}', 'w', encoding='utf-8') as answer_key:
            # Header for the quiz.
            quiz_file.write('{:20s}Тест. Вариант {:d}.\nСтолицы стран мира'.format('', num_quiz))
            quiz_file.write('\n\n')
        # Shuffle the order of capitals.
        # countries = list({**country_capit['Europe'], **country_capit['Asia']}.keys())
            countries = list(country_capit.keys())
            random.shuffle(countries)
        
            for question_num in range(20):
            # Get correct answers
                correct_ans = country_capit[countries[question_num]]
                wrong_ans = list(country_capit.values())
                del wrong_ans[wrong_ans.index(correct_ans)]
                wrong_ans = random.sample(wrong_ans, 3)
                ans_options = wrong_ans + [correct_ans]
                random.shuffle(ans_options)
                
                # Writing the question and the answer options to the quiz file.
                quiz_file.write('{:d}. Столица {:s}?\n'.format(question_num+1, 
                                                                              countries[question_num]))
                for abcd, option in zip("ABCD", ans_options):
                    quiz_file.write(f'{abcd}. {option}\n')
                quiz_file.write('\n')
                
                # Writing the answer key to a file
                answer_key.write(f'{question_num+1}. {"ABCD"[ans_options.index(correct_ans)]}\n')


if __name__ == "__main__":
    quizes_rus({**europe['Europe'], **asia['Asia']})
