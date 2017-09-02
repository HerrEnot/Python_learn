def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question, "попробуй еще раз")
#aloha = input("добро пожаловать, ")
#print(get_answer(question=aloha.lower()))
#how = input("спроси меня, ")
#print(get_answer(question=how.lower()))
#bye = input("скажи пока, ")
#print(get_answer(question=bye.lower()))
def get_question(greeting):
    question = input(greeting)
    print(get_answer(question.lower()))
get_question("добро пожаловать  ")
get_question("спроси меня  ")
get_question("попрощаемся?  ")
