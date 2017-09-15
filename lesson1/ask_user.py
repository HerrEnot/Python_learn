def ask_user():
    while True:        
        text = input('спроси меня: ')
        if text == 'пока':
            break
        print(get_answer(text))

def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question, "попробуй еще раз")

ask_user()