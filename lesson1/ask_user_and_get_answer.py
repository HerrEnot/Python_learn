def ask_user():
    while True:
        try:        
            text = input('спроси меня: ')
            if text == 'пока':
                print("sayonara")  
                break
            print(get_answer(text))
        except KeyboardInterrupt:
            print("\nответишь и пойдешь гулять")

def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question, "попробуй еще раз")

ask_user()