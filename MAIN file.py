'''бот @HelloooTutBot'''

import telebot.apihelper
from telebot import types

task_number = 0
BOT_TOKEN = '5167551152:AAG6AxDi1-u6K__z1DLjQriOlr_W7ba89pA'
ADMIN_ID = '1390420849'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def main_function(message):
    '''главная функция которая дает выбор: по какому предмету выполнять задания'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item_mathematics = types.InlineKeyboardButton(text = 'Математика')
    item_biology = types.InlineKeyboardButton(text = 'Биология')
    item_geography = types.InlineKeyboardButton(text = 'География')
    item_russian = types.InlineKeyboardButton(text = 'Русский')
    item_chemistry = types.InlineKeyboardButton(text = 'Химия')
    item_english = types.InlineKeyboardButton(text = 'Английский')
    item_history = types.InlineKeyboardButton(text = 'История')
    item_social_studies = types.InlineKeyboardButton(text = 'Oбществознание')
    item_informatics = types.InlineKeyboardButton(text = 'Информатика')
    item_physics = types.InlineKeyboardButton(text = 'Физика')
    markup.add(item_mathematics, item_biology, item_geography, item_russian, item_chemistry, item_english, item_history, item_informatics, item_physics, item_social_studies)

    msg = bot.send_message(message.chat.id, f'Приветик {message.from_user.first_name}! Выбери предмат по которому хочешь решить ОГЕ или определенное задание', reply_markup = markup)
    bot.register_next_step_handler(msg, checking_the_subject_selection)

def function_after_the_correct_answer_to_the_question(message):
    '''функция полсе правильного ответа на вопрос'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item_mathematics = types.InlineKeyboardButton(text = 'Математика')
    item_biology = types.InlineKeyboardButton(text = 'Биология')
    item_geography = types.InlineKeyboardButton(text = 'География')
    item_russian = types.InlineKeyboardButton(text = 'Русский')
    item_chemistry = types.InlineKeyboardButton(text = 'Химия')
    item_english = types.InlineKeyboardButton(text = 'Английский')
    item_history = types.InlineKeyboardButton(text = 'История')
    item_social_studies = types.InlineKeyboardButton(text = 'Oбществознание')
    item_informatics = types.InlineKeyboardButton(text = 'Информатика')
    item_physics = types.InlineKeyboardButton(text = 'Физика')
    markup.add(item_mathematics, item_biology, item_geography, item_russian, item_chemistry, item_english, item_history, item_informatics, item_physics, item_social_studies)

    msg = bot.send_message(message.chat.id, f'Можешь выбрать предмет', reply_markup = markup)
    bot.register_next_step_handler(msg, checking_the_subject_selection)

def checking_the_subject_selection(message):
    '''проверка выбора предмета'''

    if message.text == 'Математика':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_complete_the_task = types.InlineKeyboardButton(text = 'Пройти задание')
        item_learn_how_to_completea_task = types.InlineKeyboardButton(text = 'Научиться проходить задание')
        markup.add(item_complete_the_task, item_learn_how_to_completea_task)

        msg = bot.send_message(message.chat.id, 'Выбери действие', reply_markup = markup)
        bot.register_next_step_handler(msg, checking_what_the_user_has_chosen_after_math)

def checking_what_the_user_has_chosen_after_math(message):
    '''проверка что выбрал пользователь после того как выбрал математику'''

    if message.text == 'Пройти задание':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item_1 = types.InlineKeyboardButton(text = 'Задание 1')
        item_2 = types.InlineKeyboardButton(text = 'Задание 2')
        item_3 = types.InlineKeyboardButton(text = 'Задание 3')
        item_4 = types.InlineKeyboardButton(text = 'Задание 4')
        item_5 = types.InlineKeyboardButton(text = 'Задание 5')
        item_6 = types.InlineKeyboardButton(text = 'Задание 6')
        item_7 = types.InlineKeyboardButton(text = 'Задание 7')
        item_8 = types.InlineKeyboardButton(text = 'Задание 8')
        item_9 = types.InlineKeyboardButton(text = 'Задание 9')
        item_10=types.InlineKeyboardButton(text = 'Задание 10')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10)

        msg = bot.send_message(message.chat.id, 'Выбери номер задания', reply_markup = markup)
        bot.register_next_step_handler(msg, complete_a_math_assignment)

    if message.text == 'Научиться проходить задание':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item_1 = types.InlineKeyboardButton(text = 'Задание 1')
        item_2 = types.InlineKeyboardButton(text = 'Задание 2')
        item_3 = types.InlineKeyboardButton(text = 'Задание 3')
        item_4 = types.InlineKeyboardButton(text = 'Задание 4')
        item_5 = types.InlineKeyboardButton(text = 'Задание 5')
        item_6 = types.InlineKeyboardButton(text = 'Задание 6')
        item_7 = types.InlineKeyboardButton(text = 'Задание 7')
        item_8 = types.InlineKeyboardButton(text = 'Задание 8')
        item_9 = types.InlineKeyboardButton(text = 'Задание 9')
        item_10=types.InlineKeyboardButton(text = 'Задание 10')
        markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10)

        msg = bot.send_message(message.chat.id, 'Выбери номер задания', reply_markup = markup)
        bot.register_next_step_handler(msg, teach_to_solve_math_problems)

def teach_to_solve_math_problems(message):
    '''научиться решать задания по математике'''

    if message.text == 'Задание 1' or message.text == 'Задание 2' or message.text == 'Задание 3' or message.text == 'Задание 4' or message.text == 'Задание 5':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        item_looked = types.InlineKeyboardButton(text = 'Все я посмотерл')
        item_I_dont_want_to_read = types.InlineKeyboardButton(text = 'Не хочу смотреть')
        markup.add(item_looked, item_I_dont_want_to_read, item)

        msg = bot.send_message(message.chat.id, 'Желаю хорошего просмотра https://www.youtube.com/watch?v=uH-FTOAjqUY', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

def complete_a_math_assignment(message):
    '''вывод задания по пматематики'''

    global task_number

    task_number += 1
    print(task_number)

    if message.text == 'Задание 1':

        if task_number == 1:

            with open('PICTURES for oge/Математика задание 1 переменная 1.jpg', 'rb') as file:
                msg = bot.send_photo(message.chat.id, file, 'Для объектов, указанных в таблице, определите, какими цифрами они обозначены на схеме. Заполните таблицу, в ответ запишите последовательность четырёх цифр.\nНа плане изображена схема квартиры (сторона каждой клетки на схеме равна 1 м). Вход и выход осуществляются через единственную дверь.\nПри входе в квартиру расположен коридор, отмеченный цифрой 1. Перед входом в квартиру располагается ванная комната, а справа от неё — санузел.\nГостиная занимает наибольшую площадь в квартире, из гостиной можно попасть в детскую комнату. Также в квартире есть кухня, из которой можно попасть на балкон, отмеченный цифрой 6. В конце коридора находится кладовая комната, имеющая площадь 10 м (в квадрате).\nПотолок в ванной комнате и санузле планируется покрасить в белый цвет. Для покраски одного 1 м (в квадрате) потолка требуется 0,2 л краски.\nВ квартире стоит однотарифный счётчик электроэнергии. Имеется возможность установить двухтарифный счётчик.')
                bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_1)

        if task_number == 2:

            with open('PICTURES for oge/Математика задание 1 переменная 2.jpg', 'rb') as file:
                msg = bot.send_photo(message.chat.id, file, 'Завод допускает установку шин с другими маркировками. В таблице показаны разрешённые размеры шин.\nАвтомобильное колесо, как правило, представляет собой металлический диск с установленной на него резиновой шиной. Диаметр диска совпадает с диаметром внутреннего отверстия в шине.\nДля маркировки автомобильных шин применяется единая система обозначений. Например, 195/65 R15 (рис. 1). Первое число (число 195 в приведённом примере) обозначает ширину шины в миллиметрах (параметр B на рисунке 2). Второе число (число 65 в приведённом примере) — процентное отношение высоты боковины (параметр на рисунке 2) к ширине шины, то есть 100 умножить на дробь: числитель: H, знаменатель: B конец дроби .\nПоследующая буква обозначает тип конструкции шины. В данном примере буква R означает, что шина радиальная, то есть нити каркаса в боковине шины расположены вдоль радиусов колеса. На всех легковых автомобилях применяются шины радиальной конструкции.За обозначением типа конструкции шины идёт число, указывающее диаметр диска колеса d в дюймах (в одном дюйме 25,4 мм). Таким образом, общий диаметр колеса D легко найти, зная диаметр диска и высоту боковины.\nВозможны дополнительные маркировки, обозначающие допустимую нагрузку на шину, сезонность использования, тип дорожного покрытия и другие параметры.\nЗавод производит легковые автомобили определённой модели и устанавливает на них колёса с шинами маркировки 165/70 R13.')
                bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_2)

        if task_number == 3:

            with open('PICTURES for oge/Математика задание 1 переменная 3.jpg', 'rb') as file:
                msg = bot.send_photo(message.chat.id, file, 'Павел страховал свою гражданскую ответственность три года. В течение первого года были сделаны две страховые выплаты, после этого выплат не было.Какой класс будет присвоен Павлу на начало четвёртого года страхования?Каждый водитель в Российской Федерации должен быть застрахован по программе обязательного страхования гражданской ответственности (ОСАГО). Стоимость полиса получается умножением базового тарифа на несколько коэффициентов. Коэффициенты зависят от водительского стажа, мощности автомобиля, количества предыдущих страховых выплат и других факторов.Коэффициент бонус-малус (КБМ) зависит от класса водителя. Это коэффициент, понижающий или повышающий стоимость полиса в зависимости от количества ДТП в предыдущий год. Сначала водителю присваивается класс 3. Срок действия полиса, как правило, один год. Каждый последующий год класс водителя рассчитывается в зависимости от числа страховых выплат в течение истекшего года, в соответствии со следующей таблицей.')
                bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_3)

        if task_number == 4:

            with open('PICTURES for oge/Математика задание 1 переменная 4.jpg', 'rb') as file:
                msg = bot.send_photo(message.chat.id, file, 'Какое наименьшее количество дуг нужно заказать, чтобы расстояние между соседними дугами было не более 60 см? Алексей Юрьевич решил построить на дачном участке теплицу длиной NP = 4,5 м. Для этого он сделал прямоугольный фундамент. Для каркаса теплицы Алексей Юрьевич заказывает металлические дуги в форме полуокружностей длиной 5,2 м каждая и плёнку для обтяжки. В передней стенке планируется вход, показанный на рисунке прямоугольником ACDB. Точки A и B — середины отрезков MO и ON соответственно.')
                bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_4)

def checking_the_first_math_assignment_the_variable_is_4(message):
    '''проверка задания математики если переменная равна 4'''

    if message.text == '9':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Круто, поздравляю! Можешь порешать еще задачи', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    else:

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_decision = types.InlineKeyboardButton(text = 'Посмотреть решение')
        item_decide_first = types.InlineKeyboardButton(text = 'Решить сначала')
        item_view_training = types.InlineKeyboardButton(text = 'Посмотреть обучение')
        markup.add(item_view_training, item_decision, item_decide_first)

        msg = bot.send_message(message.chat.id, 'Вы решили задачу не правильно, можешь выбрать что-то из предложенного ниже', reply_markup = markup)
        bot.register_next_step_handler(msg, incorrect_answer_according_to_mathematics_the_variable_is_3)

def incorrect_answer_according_to_mathematics_the_variable_is_4(message):
    '''что делать после на правильного ответа на первый вопрос по математики и если переменная равна 4'''

    if message.text == 'Посмотреть решение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Переведем 60 см = 0,6 м. Найдем количество промежутков между дугами: 4,5 : 0,6 = 7,5, следовательно, наименьшее количество промежутков — 8. Количество дуг на единицу больше, чем количество промежутков: 8 + 1 = 9.')
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    if message.text == 'Решить сначала':

        with open('PICTURES for oge/Математика задание 1 переменная 4.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Какое наименьшее количество дуг нужно заказать, чтобы расстояние между соседними дугами было не более 60 см? Алексей Юрьевич решил построить на дачном участке теплицу длиной NP = 4,5 м. Для этого он сделал прямоугольный фундамент. Для каркаса теплицы Алексей Юрьевич заказывает металлические дуги в форме полуокружностей длиной 5,2 м каждая и плёнку для обтяжки. В передней стенке планируется вход, показанный на рисунке прямоугольником ACDB. Точки A и B — середины отрезков MO и ON соответственно.')
            bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_4)

    if message.text == 'Посмотреть обучение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        item_looked = types.InlineKeyboardButton(text = 'Все я посмотерл')
        item_I_dont_want_to_read = types.InlineKeyboardButton(text = 'Не хочу смотреть')
        markup.add(item_looked, item_I_dont_want_to_read, item)

        msg = bot.send_message(message.chat.id, 'Лови ссылку на урок https://www.youtube.com/watch?v=uH-FTOAjqUY, а после можешь выбрать предмет', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

def checking_the_first_math_assignment_the_variable_is_3(message):
    '''проверка задания математики если переменная равна 3'''

    if message.text == '1':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Круто, поздравляю! Можешь порешать еще задачи', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    else:

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_decision = types.InlineKeyboardButton(text = 'Посмотреть решение')
        item_decide_first = types.InlineKeyboardButton(text = 'Решить сначала')
        item_view_training = types.InlineKeyboardButton(text = 'Посмотреть обучение')
        markup.add(item_view_training, item_decision, item_decide_first)

        msg = bot.send_message(message.chat.id, 'Вы решили задачу не правильно, можешь выбрать что-то из предложенного ниже', reply_markup = markup)
        bot.register_next_step_handler(msg, incorrect_answer_according_to_mathematics_the_variable_is_3)

def incorrect_answer_according_to_mathematics_the_variable_is_3(message):
    '''что делать после на правильного ответа на первый вопрос по математики и если переменная равна 3'''

    if message.text == 'Посмотреть решение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'В начале первого года Павлу был присвоен класс 3. После двух выплат в течение первого года на начало второго года Павлу был присвоен класс М. Поскольку в течение второго года Павел не делал страховых выплат, на начало третьего года Павлу был присвоен класс 0. В течение третьего года Павел также не делал страховых выплат, следовательно, на начало четвёртого года Павлу будет присвоен класс 1.')
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    if message.text == 'Решить сначала':

        with open('PICTURES for oge/Математика задание 1 переменная 3.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Павел страховал свою гражданскую ответственность три года. В течение первого года были сделаны две страховые выплаты, после этого выплат не было.Какой класс будет присвоен Павлу на начало четвёртого года страхования?Каждый водитель в Российской Федерации должен быть застрахован по программе обязательного страхования гражданской ответственности (ОСАГО). Стоимость полиса получается умножением базового тарифа на несколько коэффициентов. Коэффициенты зависят от водительского стажа, мощности автомобиля, количества предыдущих страховых выплат и других факторов.Коэффициент бонус-малус (КБМ) зависит от класса водителя. Это коэффициент, понижающий или повышающий стоимость полиса в зависимости от количества ДТП в предыдущий год. Сначала водителю присваивается класс 3. Срок действия полиса, как правило, один год. Каждый последующий год класс водителя рассчитывается в зависимости от числа страховых выплат в течение истекшего года, в соответствии со следующей таблицей.')
            bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_3)

    if message.text == 'Посмотреть обучение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        item_looked = types.InlineKeyboardButton(text = 'Все я посмотерл')
        item_I_dont_want_to_read = types.InlineKeyboardButton(text = 'Не хочу смотреть')
        markup.add(item_looked, item_I_dont_want_to_read, item)

        msg = bot.send_message(message.chat.id, 'Лови ссылку на урок https://www.youtube.com/watch?v=uH-FTOAjqUY, а после можешь выбрать предмет', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

def checking_the_first_math_assignment_the_variable_is_2(message):
    '''проверка задания математики если переменная равна 2'''

    if message.text == '185':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Круто, поздравляю! Можешь порешать еще задачи', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    else:

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_decision = types.InlineKeyboardButton(text = 'Посмотреть решение')
        item_decide_first = types.InlineKeyboardButton(text = 'Решить сначала')
        item_view_training = types.InlineKeyboardButton(text = 'Посмотреть обучение')
        markup.add(item_view_training, item_decision, item_decide_first)

        msg = bot.send_message(message.chat.id, 'Вы решили задачу не правильно, можешь выбрать что-то из предложенного ниже', reply_markup = markup)
        bot.register_next_step_handler(msg, incorrect_answer_according_to_mathematics_the_variable_is_2)

def incorrect_answer_according_to_mathematics_the_variable_is_2(message):
    '''что делать после на правильного ответа на первый вопрос по математики и если переменная равна 2'''

    if message.text == 'Посмотреть решение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Из таблицы видно, что при диаметре 15 дюймов наименьшая ширина шины — 185 мм.')
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    if message.text == 'Решить сначала':

        with open('PICTURES for oge/Математика задание 1 переменная 2.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Завод допускает установку шин с другими маркировками. В таблице показаны разрешённые размеры шин.\nАвтомобильное колесо, как правило, представляет собой металлический диск с установленной на него резиновой шиной. Диаметр диска совпадает с диаметром внутреннего отверстия в шине.\nДля маркировки автомобильных шин применяется единая система обозначений. Например, 195/65 R15 (рис. 1). Первое число (число 195 в приведённом примере) обозначает ширину шины в миллиметрах (параметр B на рисунке 2). Второе число (число 65 в приведённом примере) — процентное отношение высоты боковины (параметр на рисунке 2) к ширине шины, то есть 100 умножить на дробь: числитель: H, знаменатель: B конец дроби .\nПоследующая буква обозначает тип конструкции шины. В данном примере буква R означает, что шина радиальная, то есть нити каркаса в боковине шины расположены вдоль радиусов колеса. На всех легковых автомобилях применяются шины радиальной конструкции.За обозначением типа конструкции шины идёт число, указывающее диаметр диска колеса d в дюймах (в одном дюйме 25,4 мм). Таким образом, общий диаметр колеса D легко найти, зная диаметр диска и высоту боковины.\nВозможны дополнительные маркировки, обозначающие допустимую нагрузку на шину, сезонность использования, тип дорожного покрытия и другие параметры.\nЗавод производит легковые автомобили определённой модели и устанавливает на них колёса с шинами маркировки 165/70 R13.')
            bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_2)

    if message.text == 'Посмотреть обучение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        item_looked = types.InlineKeyboardButton(text = 'Все я посмотерл')
        item_I_dont_want_to_read = types.InlineKeyboardButton(text = 'Не хочу смотреть')
        markup.add(item_looked, item_I_dont_want_to_read, item)

        msg = bot.send_message(message.chat.id, 'Лови ссылку на урок https://www.youtube.com/watch?v=uH-FTOAjqUY, а после можешь выбрать предмет', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

def checking_the_first_math_assignment_the_variable_is_1(message):
    '''проверка задания математики если переменная равна 1'''

    if message.text == '2748':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Круто, поздравляю! Можешь порешать еще задачи', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    else:

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_decision = types.InlineKeyboardButton(text = 'Посмотреть решение')
        item_decide_first = types.InlineKeyboardButton(text = 'Решить сначала')
        item_view_training = types.InlineKeyboardButton(text = 'Посмотреть обучение')
        markup.add(item_view_training, item_decision, item_decide_first)

        msg = bot.send_message(message.chat.id, 'Вы решили задачу не правильно, можешь выбрать что-то из предложенного ниже', reply_markup = markup)
        bot.register_next_step_handler(msg, incorrect_answer_according_to_mathematics_the_variable_is_1)

def incorrect_answer_according_to_mathematics_the_variable_is_1(message):
    '''что делать после на правильного ответа на первый вопрос по математики и если переменная равна 1'''

    if message.text == 'Посмотреть решение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        markup.add(item)

        msg = bot.send_message(message.chat.id, 'Перед входом в квартиру располагается ванная комната, следовательно, ванная комната отмечена цифрой 2. Гостиная занимает наибольшую площадь в квартире, из гостиной можно попасть в детскую комнату, поэтому детская комната отмечена цифрой 7. Также в квартире есть кухня, из которой можно попасть на балкон, отмеченный цифрой 6, значит, кухня отмечена на схеме цифрой 4. В конце коридора находится кладовая комната, имеющая площадь 10 м (в квадрате), следовательно, кладовая комната отмечена цифрой 8.\nОтвет: 2748.\nВыбирай следующий предмет', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

    if message.text == 'Решить сначала':

        with open('PICTURES for oge/Математика задание 1 переменная 1.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Для объектов, указанных в таблице, определите, какими цифрами они обозначены на схеме. Заполните таблицу, в ответ запишите последовательность четырёх цифр.\nНа плане изображена схема квартиры (сторона каждой клетки на схеме равна 1 м). Вход и выход осуществляются через единственную дверь.\nПри входе в квартиру расположен коридор, отмеченный цифрой 1. Перед входом в квартиру располагается ванная комната, а справа от неё — санузел.\nГостиная занимает наибольшую площадь в квартире, из гостиной можно попасть в детскую комнату. Также в квартире есть кухня, из которой можно попасть на балкон, отмеченный цифрой 6. В конце коридора находится кладовая комната, имеющая площадь 10 м (в квадрате).\nПотолок в ванной комнате и санузле планируется покрасить в белый цвет. Для покраски одного 1 м (в квадрате) потолка требуется 0,2 л краски.\nВ квартире стоит однотарифный счётчик электроэнергии. Имеется возможность установить двухтарифный счётчик.')
            bot.register_next_step_handler(msg, checking_the_first_math_assignment_the_variable_is_1)

    if message.text == 'Посмотреть обучение':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item = types.InlineKeyboardButton(text = 'Выбрать предмет')
        item_looked = types.InlineKeyboardButton(text = 'Все я посмотерл')
        item_I_dont_want_to_read = types.InlineKeyboardButton(text = 'Не хочу смотреть')
        markup.add(item_looked, item_I_dont_want_to_read, item)

        msg = bot.send_message(message.chat.id, 'Лови ссылку на урок https://www.youtube.com/watch?v=uH-FTOAjqUY, а после можешь выбрать предмет', reply_markup = markup)
        bot.register_next_step_handler(msg, function_after_the_correct_answer_to_the_question)

bot.polling()