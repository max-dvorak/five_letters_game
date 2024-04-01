from random import choice
from datetime import datetime, time
import csv

credit = '--- v.1.1. Apr 2024. M.Dvorak ---'

GAME_TITLE = '5 БУКВ с Якубовичем 2.0'
HOST_NAME = 'Якубович 2.0'
INDENT = ' ' * 14
MAX_TRIES = 6
BOARD_INDEXES = {
    '0': 1,
    '1': 4,
    '2': 7,
    '3': 10,
    '4': 13
}

# users = {
#     'Макс': {
#         'Всего сыграно': 0,
#         'Отгадано слов': 0,
#         'Отгаданные слова': []
#     }
# }


def login() -> str:
    entered_name = input('Привет! Пожалуйста, введи свое имя:\n')
    # if entered_name in users:
    #     welcome_back = (
    #         'С возвращением в игру! У тебя на счету:\n'
    #         f'Игр: {0} | Побед: {0}\n'
    #         'Слова, которые были тобой угаданы:\n'
    #         f'{[]}\n'
    #     )
    #     print(welcome_back)
    # else:
    #     print('Добро пожаловать в игру! Сохраняем данные пользователя.\n')
    #     users[entered_name] = {
    #         'Всего сыграно': 0,
    #         'Отгадано слов': 0,
    #         'Отгаданные слова': []
    #     }
    # print('А теперь самое время разбудить Якубовича 2.0!\n')
    return entered_name


gamer_name = login()


superprizes = (
    'а-а-а-автомобиль',
    'телевизор',
    'iPhone 16 Pro Max Ultra 4 Tb Titanium Gold (точно не китайская копия)',
    f'{HOST_NAME} сбреет усы себе',
    f'{HOST_NAME} сбреет усы у {gamer_name}'
)


# Внешний контур: запуск и финал серии игр.
def start():
    time_of_day = user_time_hello()
    print(f'''{HOST_NAME}: {time_of_day}, здра-а-авствуйте!
              Добро пожаловать на игру "{GAME_TITLE}"!
              C вами ее ведущий, бессменный и неподражаемый {HOST_NAME}!

              * аплодисменты *

              Позвольте сразу представить нашу тройку игроков:
              это два великолепных голоса в моей голове, а также
              прекрасный человек {gamer_name}! Поприветствуем!

              * овации *

              Итак, {gamer_name}, ты уже играл(а) в "{GAME_TITLE}"?
              (Только давай договоримся: на вопросы отвечаем "да" или нет")''')
    played = yes_or_no()
    if played == 'нет':
        hello_new_player()
    else:
        print(f'{HOST_NAME}: Отлично! Тогда начнём игру!')

    stop_playing = False
    games_counter = 0
    wins_counter = 0
    current_words = []
    with open('5_char_words.csv', newline='', encoding='cp1251') as file:
        for row in csv.reader(file):
            current_words.append(row[0].lower())
    guessed_words = []

    while not stop_playing:
        # Запускаем игру.
        games_counter += 1

        the_word = choice(current_words)
        current_words.pop(current_words.index(the_word))

        print(f'''{INDENT}Доска готова, и все ждут, затаив дыхание!

                 Игра № {games_counter}
              ''')

        result = the_game(the_word)

        if result:
            wins_counter += 1
            guessed_words.append(the_word)
            print(f'{HOST_NAME}: По-о-оздравляю, это была великолепная игра!')
        else:
            print(f'{INDENT}Ну и нестрашно, в следующий раз получится!')

        result_text = (
            f'{INDENT}Игр в серии: {games_counter}\n'
            f'{INDENT}Из них побед: {wins_counter}\n'
            f'{INDENT}Еще разочек сыграем?'
        )
        print(result_text)

        wanna_play_again = yes_or_no()
        if wanna_play_again == 'да':
            print(f'{HOST_NAME}: О-о-отличный выбор! Погнали ещё раз!')
        else:
            stop_playing = True

    save_results()
    superprize = choice(superprizes)

    print(f'{HOST_NAME}: Тогда спасибо за игру!')
    if wins_counter:
        if wins_counter == 1:
            print(f'{INDENT}Тебе удалось победить {wins_counter} раз.')
            print(f'{INDENT}Уверен, в следующий раз будет больше!')
        elif wins_counter < 5:
            print(
                f'{INDENT}Неплохо, тебе удалось победить {wins_counter} раза!')
        else:
            print(
                f'{INDENT}Это великолепно, тебе удалось победить '
                f'{wins_counter} раз!')
        print(f'{INDENT}Слова, которые тебе удалось отгадать:')
        words_str = ''
        for word in guessed_words:
            words_str += word
            if len(guessed_words) > guessed_words.index(word) + 1:
                words_str += ', '
        print(INDENT + words_str)
        print(f'''\n{INDENT}Разумеется, ты заслуживаешь наш суперприз!
              Напоминаю, сегодня это:
              {superprize}!!!

              * восхищение публики *

              Ты можешь забрать его ближайшего 30 февраля.''')
    print(f'''
              Это была увлекательная серия "{GAME_TITLE}"!
              Киберобнял-киберприподнял, твой обожаемый {HOST_NAME}.
              Не скучаем, увидимся совсем скоро!

              * прощальные овации *

              {credit}''')


def save_results():
    pass


# Текст приветствия для нового игрока.
def hello_new_player():
    print(f'''{HOST_NAME}: Что ж, пока рекламная пауза, разберёмся, что к чему!
              "{GAME_TITLE}" - это классическая игра "5 букв",
              только с великолепным ведущим - мной, Якубовичем 2.0!

              * бурные аплодисменты *

              За шесть попыток нужно угадать слово, состоящее из пяти букв.
              Ты называешь слово, и мы вместе смотрим, оно загадано или нет.
              Загадываются только существительные в единственном числе
              (кроме случаев, когда есть только множественная форма).
              Вместо буквы "ё" - "е". Имен собственных тоже нет.

              Если слово отгадано неверно, мы увидим,
              какие буквы из него все же правильные.
              Отсутствующие отправляются в Буквотилизатор под игровым полем:
              они всегда будут видны. Угаданные буквы останутся на доске.
              Они могут быть прописными [А] - значит, стоят на своем месте, -
              либо строчными [а] - значит, они есть где-то еще в слове.
              Нужен пример?''')
    needed = yes_or_no()
    if needed == 'нет':
        print(f'{HOST_NAME}: Ну супер, тогда погнали играть!')
    else:
        print(
            f'{HOST_NAME}: Отлично, давай быстренько разберемся, '
            f'пока реклама не кончилась.')
        print(f'{INDENT}Вот как выглядит игровая доска:')
        print('')
        example_board = new_empty_board()
        print('')
        print(f'''{HOST_NAME}: Стрелка справа показывает, какая сейчас попытка.
              Первая строка = первая попытка. Буквотилизатор очевидно пуст.
              Предположим, загадано слово "слово". Повезло, что в нем 5 букв.
              Пробуем угадать - пишем, допустим, "моряк". Что получилось:
        ''')
        example_board[2] = '[_][о][_][_][_] < моряк'
        example_board[9] = '[м_р_я_к______]'
        example_board[3] += ' <'
        for row in example_board:
            print(INDENT + row)
        print('')
        print(f'''{HOST_NAME}: Что ж, слово неправильное, но хорошие новости:
              у нас есть буква "о"! Она строчная, значит ее нужно переставить.
              Обрати внимание: в "слово" две буквы "о", но поскольку ты ввел
              только одну - одна и отображается.
              Буквы, которых нет в слове, провалились в подвал:
              там у нас Буквотилизатор.
              Введенные тобой слова будут сохраняться справа от доски.
              Попробуем ввести "плато" и посмотрим на результат.
        ''')
        example_board[3] = '[_][Л][_][_][О] < плато'
        example_board[9] = '[м_р_я_к_п_а_т]'
        example_board[4] += ' <'
        for row in example_board:
            print(INDENT + row)
        print('')
        print(f'''{HOST_NAME}: Неплохо! Целых две буквы на своих местах!
              Первая буква "о" в "слово" не отображается - ее тоже нужно найти.
              И - так, на всякий случай: если ввести какую-то чушь
              (например, "хливо") или слово не из 5 букв ("сладость"),
              мы тебя дисквалифицируем, а твой компьютер самоуничтожится.
              Шутка! Просто такой ответ я принять, к сожалению, не смогу.
              Что ж, пробуем ввести "слово"!
        ''')
        example_board[4] = '[С][Л][О][В][О]'
        example_board[4] += ' < < < <'
        for row in example_board:
            print(INDENT + row)
        print('')
        print(INDENT + '[    Э Т О    ]')
        print(INDENT + '[П О Б Е Д А !]')
        print('')
        print(f'''{HOST_NAME}: Ура! Мы это сделали!
              А теперь, как говорил Шерлок, - в игру, в игру!''')


# Первый вложенный контур: конкретная игра.
def the_game(the_word: str) -> bool:
    sorry_no_set = (
        'К сожалению, загадано другое слово =(',
        'Нет, это не подошло, давай еще разок.',
        'Я в тебя верю, рано или поздно все получится!',
        'Нет, это неправильно, сорри.',
        'Ну же, я прямо чувствую, как победа приближается!',
        f'Уфф, дамы и господа, поддержим {gamer_name} аплодисментами!',
        '* Хрустит яблоком из кибермузея "Поле Чудес" *',
    )

    tries_count = 0
    current_board = new_empty_board()
    # print(f'ЗАГАДАННОЕ СЛОВО: {the_word}')
    print(f'\n{HOST_NAME}: Какое слово назовешь первым?')
    while tries_count <= 6:
        tries_count += 1
        guess_word = enter_the_word()
        if guess_word != the_word:
            current_board = your_move(
                board=current_board,
                secret_word=the_word,
                try_number=tries_count,
                users_word=guess_word
            )
            if tries_count < 6:
                print(f'\n{HOST_NAME}: {choice(sorry_no_set)}')
        else:
            current_board = winner_board(
                winner_board=current_board,
                the_word=the_word,
                the_try=tries_count
            )
            print('')
            for row in current_board:
                print(' ' * 14 + row)
            return True
        if tries_count < 6:
            print(' ' * 14 + f'Осталось попыток: {MAX_TRIES - tries_count}')
            if tries_count == 4:
                print(
                    '{INDENT}{gamer_name}, внимательнее! Осталось 2 попытки!')
        else:
            print(f'{HOST_NAME}: К сожалению, попыток не осталось. :(')
            print(' ' * 14 + f'А загадано было слово "{the_word}".')
            return False


# Второй вложенный контур: работа с конкретным ходом
# и сборка доски для следующей попытки.
def your_move(
        board: list,
        secret_word: str,
        try_number: int,
        users_word: str  # Сюда попадают только неправильные слова
) -> list:
    # Индекс текущего ряда на доске всегда на 1 больше номера попытки.
    current_row = board[try_number + 1]
    # Актуальный буквотилизатор всегда на последней строке
    current_utilizer = board[-1]

    # Делаем из слов списки, чтобы с ними можно было работать.
    secret_list = list(secret_word)
    user_list = list(users_word)

    # Проверка в два прогона.
    # 1-й проверяет полные совпадения букв (на тех же позициях).
    # 2-й проверяет наличие букв в других позициях.
    # Также на втором прогоне если букв в слове нет, они буквотилизируются.
    for char in user_list:  # 1-й прогон
        user_pos = user_list.index(char)  # Индекс буквы в слове пользователя
        secret_pos = user_pos  # Индекс эквивалентной буквы в загаданном слове
        board_pos = BOARD_INDEXES.get(str(user_pos))  # Место буквы на доске

        if char in secret_list:
            if secret_list[secret_pos] == user_list[user_pos]:
                current_row = upper_case_add(current_row, char, board_pos)
                secret_list[secret_pos] = ' '

        board[try_number + 1] = current_row
        # чтобы индекс следующей такой буквы был ОК
        user_list[user_list.index(char)] = char.upper()
    # 1-й прогон закончен

    # Возвращаем список из слова в исходное состояние после прогона
    for char in user_list:
        user_list[user_list.index(char)] = char.lower()

    for char in user_list:  # 2-й прогон
        user_pos = user_list.index(char)
        secret_pos = user_pos
        board_pos = BOARD_INDEXES.get(str(user_pos))

        # Проверяем, свободен ли Буквотилизатор.
        if current_utilizer[13] != '_':
            board.append('[_____________]')
            current_utilizer = board[-1]

        if char in secret_list:
            # Если буквы с одним индексом не равны
            # и если текущая позиция не пустая
            # (тогда на этом месте есть буква,
            # выставленная после первого прогона).
            if (secret_list[secret_pos] != user_list[user_pos]
                    and secret_list[secret_pos] != ' '):
                current_row = lower_case_add(current_row, char, board_pos)
                secret_list[secret_list.index(char)] = char.upper()
        # Утилизация, если в слове после 1-го прогона не осталось этой буквы,
        # а также если она не появилась на доске.
        elif (char not in secret_list
                and char.upper() != current_row[board_pos]):
            # Убеждаемся, что в утилизаторе еще нет этой буквы.
            # Дубликаты не нужны.
            utilized_chars = set()
            for row in board[::-1]:
                if row[0] == '[':
                    for letter in list(row):
                        if letter != '[' and letter != ']' and letter != '_':
                            utilized_chars.add(letter)
                else:
                    # Если строка начинается не с '[' - это "БУКВОТИЛИЗАТОР:"
                    break
            # print('Буквы в утилизаторе:')
            # print(utilized_chars)
            # Если в получившемся множестве этой буквы нет - добавляем.
            if char not in utilized_chars:
                current_utilizer = utilize(current_utilizer, char)
        # Утилизация закончена

        board[-1] = current_utilizer  # Обновляем утилизатор на доске.
        # Отмечаем букву в юзерлисте как отработанную.
        user_list[user_list.index(char)] = char.upper()
    # 2-й прогон закончен

    current_row += f' {users_word}'
    board[try_number + 1] = current_row
    if try_number < 6:
        board[try_number + 2] += ' <'

    print('')
    for row in board:
        print(' ' * 14 + row)
    return board


# Чек "да-нет"-вопросов.
def yes_or_no() -> str:
    yes_or_no_varietes = [
        'Мы же вроде договорились: только "да" или "нет".',
        'Дружище, камон, всего два варианта: "да" или "нет". М-м?',
        'Напоминаю, отвечать можно только "да" или "нет".'
    ]
    while True:
        answer_is = input(f'{gamer_name}: ').lower()
        if answer_is == 'да' or answer_is == 'нет':
            return answer_is
        else:
            print(f'{HOST_NAME}: {choice(yes_or_no_varietes)}')


# Чек на формат введённого игроком слова.
def enter_the_word() -> str:
    not_five_chars = (
        f'{HOST_NAME}: В слове должно быть пять букв.',
        f'{HOST_NAME}: Киберзуб даю, не больше и не меньше, ровно пять.',
        f'''{HOST_NAME}: Упорство обычно вознаграждается.
              Но мы тут боремся за суперприз.
              В игре "{GAME_TITLE}".
              Название как бы намекает. Понимаешь?''',
        f'{HOST_NAME}: Ладно, если сделаешь 800 попыток - приму. Шутка.',
    )
    not_five_chars_counter = 0
    not_in_list = (
        f'{HOST_NAME}: Такого слова нет в словаре. Попробуй другое.',
        f'{HOST_NAME}: И этого тоже нет, прости.',
        f'''{HOST_NAME}: Окей, давай сделаем свой словарь, с вот этими.
              Но в следующий раз, ладно?''',
        f'{HOST_NAME}: Уф-ф, ты сможешь, я в тебя верю!',
    )
    not_in_list_counter = 0
    words = []
    with open('5_char_words.csv', newline='', encoding='cp1251') as file:
        for row in csv.reader(file):
            words.append(row[0].lower())
    while True:
        the_word = input(f'{gamer_name}: ').lower()
        if len(the_word) != 5:
            if not_five_chars_counter > 3:
                continue
            print(not_five_chars[not_five_chars_counter])
            not_five_chars_counter += 1
        elif the_word not in words:
            if not_in_list_counter > 3:
                continue
            print(not_in_list[not_in_list_counter])
            not_in_list_counter += 1
        elif the_word == 'питон':
            logo = (
                '          .?77777777777777$.            ',
                '          777..777777777777$+           ',
                '         .77    7777777777$$$           ',
                '         .777 .7777777777$$$$           ',
                '         .7777777777777$$$$$$           ',
                '         ..........:77$$$$$$$           ',
                '  .77777777777777777$$$$$$$$$.=======.  ',
                ' 777777777777777777$$$$$$$$$$.========  ',
                '7777777777777777$$$$$$$$$$$$$.========= ',
                '77777777777777$$$$$$$$$$$$$$$.========= ',
                '777777777777$$$$$$$$$$$$$$$$ :========+.',
                '77777777777$$$$$$$$$$$$$$+..=========++~',
                '777777777$$..~=====================+++++',
                '77777777$~.~~~~=~=================+++++.',
                '777777$$$.~~~===================+++++++.',
                '77777$$$$.~~==================++++++++: ',
                ' 7$$$$$$$.==================++++++++++. ',
                ' .,$$$$$$.================++++++++++~.  ',
                '         .=========~.........           ',
                '         .=============++++++           ',
                '         .===========+++..+++           ',
                '         .==========+++.  .++           ',
                '          ,=======++++++,,++,           ',
                '          ..=====+++++++++=.            ',
                '                ..~+=...                '
            )
            for row in logo:
                print(' ' * 2 + row)
            return the_word
        else:
            # print('Есть такое слово')
            return the_word


# Определятор времени суток со здоровалкой.
def user_time_hello() -> str:
    current_hour = datetime.time(datetime.now())
    six_morning = time(hour=6, minute=0, second=0)
    noon = time(hour=12, minute=0, second=0)
    six_evening = time(hour=18, minute=0, second=0)
    eleven_evening = time(hour=23, minute=0, second=0)
    if current_hour < time(hour=6, minute=0, second=0):
        return 'Доброй ночи'
    elif six_morning <= current_hour < noon:
        return 'Доброе утро'
    elif noon <= current_hour < six_evening:
        return 'Добрый день'
    elif six_evening <= current_hour < eleven_evening:
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'


# Составление пустой игровой доски.
def new_empty_board() -> list:
    # Ширина игрового поля == 15
    # Индексы букв в строке:
    # [_][_][_][_][_]
    #  1  4  7  10 13
    # Индексы игровых строк - [2:8]
    # Индекс первой строки "Буквотилизатора" - 9
    new_board = ['[_]' * 5 for _ in range(6)]
    new_board[0] += ' <'
    new_board.insert(0, '[ 5   Б У К В ]')
    new_board.insert(1, '===============')
    new_board.append('БУКВОТИЛИЗАТОР:')
    new_board.append('[' + '_' * 13 + ']')
    for row in new_board:
        print(' ' * 14 + row)
    return new_board


# Добавление полностью совпадающих букв.
def upper_case_add(row: str, char: str, char_index: int) -> str:
    row_list = list(row)
    row_list[char_index] = char.upper()
    return ''.join(row_list)


# Добавление частичных совпадений.
def lower_case_add(row: str, char: str, char_index: int) -> str:
    row_list = list(row)
    row_list[char_index] = char.lower()
    return ''.join(row_list)


# Буквотилизатор
def utilize(utilizer: str, char: str) -> str:
    util_list = list(utilizer)
    # Утилизировать буквы будем через одну позицию:
    # с первой до последней позиций внутри скобок.
    # В строку умещается 7 букв с индексами: 1, 3, 5, 7, 9, 11, 13
    for position in range(1, len(util_list), 2):
        current_char = util_list[position]
        if current_char == '_':
            util_list.insert(position, char)
            util_list.pop(position + 1)
            new_utilizer = ''.join(util_list)
            return new_utilizer


# Составление доски победителя.
def winner_board(winner_board: list, the_word: str, the_try: int) -> list:
    winner_addition = [
        '',
        '[    Э Т О    ]',
        '[П О Б Е Д А !]',
        ''
    ]

    word_list = list(the_word)
    char_board_index = 1
    winner_row = winner_board[the_try + 1]

    for char in word_list:
        winner_row = upper_case_add(winner_row, char, char_board_index)
        char_board_index += 3
    winner_row += ' < < <'
    # print(winner_row)
    winner_board[the_try + 1] = winner_row
    winner_board.extend(winner_addition)
    # for row in winner_board:
    #     print(row)
    return winner_board


# Чтобы запустить игру:
start()
