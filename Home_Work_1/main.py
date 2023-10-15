
'''
Завдання 2
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

БОТ ПОМІЧНИК ПОВИНЕН СТАТИ ДЛЯ НАС ПРОТОТИПОМ ЗАСТОСУНКУ-АСИСТЕНТА ЯКИЙ МИ РОЗРОБИМО В НАСТУПНИХ ДОМАШНІХ ЗАВДАННЯХ. ЗАСТОСУНОК-АСИСТЕНТ В ПЕРШОМУ 
НАБЛИЖЕННІ ПОВИНЕН ВМІТИ ПРАЦЮВАТИ З КНИГОЮ КОНТАКТІВ ТА КАЛЕНДАРЕМ.
У цій домашній роботі зосередимося на інтерфейсі самого бота.  Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний 
застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, 
виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача 
як ключ і номер телефону як значення.

Рекомендації для виконання
По перше, нам треба систематизувати опис форматів наших команд для консольного бота-помічника. Це допоможе зрозуміти які функції треба зробити для кожної 
команди. Зробімо це:

Команда "hello", тут можна обійтись поки без функції та використати звичайний print:
Введення: "hello"
Вивід: "How can I help you?"
Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:
Введення: "add John 1234567890"
Вивід: "Contact added."
Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:
Введення: "change John 0987654321"
Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:
Введення: "phone John"
Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
Команда "all". Для цієї команди зробимо функцію show_all:
Введення: "all"
Вивід: усі збережені контакти з номерами телефонів
Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:
Введення: будь-яке з цих слів
Вивід: "Good bye!" та завершення роботи бота
Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, і бот буде виводити повідомлення "Invalid command."

Почнемо з простого варіанту CLI-бота:

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

Коли програма запускається, вона виводить повідомлення "Welcome to the assistant bot!" і входить в нескінчений цикл, де вона очікує введення команди від 
користувача while True.

Якщо користувач вводить "good bye", "close" або "exit", програма виводить "Good bye!" та завершує роботу. За це відповідає блок коду:

if command in ["close", "exit"]:
            print("Good bye!")
            break

Якщо користувач вводить "hello", програма виводить "How can I help you?". Якщо ж введена команда не відповідає жодному з цих варіантів, програма 
виводить "Invalid command.".

Welcome to the assistant bot!
Enter a command: test
Invalid command.
Enter a command: hello
How can I help you?
Enter a command: exit
Good bye!

Цей код створює простий інтерактивний командний рядок, який реагує на обмежений набір команд. Ми реалізували цикл запит-відповідь який буде служити 
відмінною основою для додавання додаткової функціональності нашого домашнього завдання.

Тепер додамо парсер команд. Перепишемо наш код наступним чином

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

Ми додали функцію parse_input(user_input) яка приймає рядок вводу користувача user_input і розбиває його на слова за допомогою методу split(). 
Вона повертає перше слово як команду cmd та решту як список аргументів *args. Рядок коду cmd, *args = user_input.split() розділяє рядок на слова. 
Перше слово зберігається у змінній cmd, а решта зберігається у списку args завдяки оператору розпакування *. Далі рядок коду cmd = cmd.strip().
lower() видаляє зайві пробіли навколо команди та перетворює її на нижній регістр. ``

НАВІЩО ПРИВОДИТИ КОМАНДУ ДО НИЖНЬОГО РЕГІСТРУ?
Припустимо, користувач вводить команду як "HELLO", "Hello" або "hello". Якщо не привести ці варіанти до спільного регістру, вони будуть розглядатися 
як різні команди, і вам доведеться обробляти кожний варіант окремо.

Приведення команди до нижнього регістру дозволяє уникнути цього, перетворюючи всі варіанти на одну та ту ж форму. Таким чином, ви можете легко 
порівнювати введену команду з попередньо визначеними командами без зважання на те, як користувач ввів її.

Це забезпечує кращий досвід користувача, оскільки програма стає менш чутливою до конкретного способу введення команд.

Отриманий результат в функції main ми отримаємо після виконання рядка коду command, *args = parse_input(user_input) .

Функція parse_input розбиває введений рядок на слова, використовуючи пробіл як розділювач. Змінна command отримує перше значення та вважається 
командою, а змінна args стає списком з усіх інших значень.

Наприклад якщо ми введемо команду "add John 123456" то змінна command стане рядком "add" а змінна args стане списком ["John", "123456"] . Якщо ж ми 
введемо команду "hello" то command стане рядком "hello", а args буде пустим списком []

Маю надію ви вже зрозуміли тепер принцип парсера, настав час додати команду add.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

Ми додали словник з контактами contacts = {} в середину функції main та функцію обробник команди add_contact.

Функція add_contact призначена для додавання нового контакту до словника контактів. Вона приймає два аргументи: args, який є списком і містить 
ім'я та телефонний номер, та contacts, який є словником, де зберігаються контакти.

Всередині функції, два елементи зі списку args розпаковуються в змінні name та phone. Функція далі додає пару "ключ: значення" до словника контактів, 
використовуючи ім'я як ключ і телефонний номер як значення contacts[name] = phone.

ТРЕБА ЗАУВАЖИТИ, ЩО ЯКЩО КОНТАКТ З ТАКИМ ІМ'ЯМ ВЖЕ ІСНУЄ, ЙОГО ДАНІ БУДУТЬ ПЕРЕЗАПИСАНІ БЕЗ БУДЬ-ЯКИХ ПОПЕРЕДЖЕНЬ. ТУТ ВИ ВЖЕ МОЖЕТЕ ДІЯТИ НА СВІЙ 
РОЗСУД, ХОЧЕТЕ ЧИ НІ ВИ ОБРОБЛЯТИ КОЛІЗІЮ, В НАШОМУ ВАРІАНТІ МИ ПЕРЕЗАПИСУЄМО КОНТАКТ.
Функція add_contact повертає рядок, що підтверджує успішне додавання контакту: "Contact added.".

Необхідно зауважити, що ця функція не має вбудованих перевірок на помилки введення. Наприклад, якщо args не містить двох елементів, ця функція 
викличе помилку ValueError.

ValueError: not enough values to unpack (expected 2, got 0)

Обробку помилок в цьому домашньому завданні залиште на свій розсуд, бо в наступному домашньому завданні ми додамо обробку помилок через декоратори.

Критерії оцінювання:
Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.

Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".

Бот не чутливий до регістру введених команд.

Бот приймає команди:

"hello", та відповідає у консоль повідомленням "How can I help you?"

"add username phone". За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. Користувач вводить ім'я username та номер 
телефону phone, обов'язково через пробіл.

"change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.  

"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.

"all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.

"close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.

Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.

Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.
'''
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name = args[0]
    new_phone = args[1]
    phone = contacts.get(name)
    if phone == None:
        phone = 'User is not found'
        return (phone)
    contacts[name] = new_phone
    return "Contact updated."

def user_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if len(args) > 1:
        phone = "Invalid command. Command 'phone' should has one argument only - 'Name'." 
    if phone == None:
        phone = "User is not found"
    return (phone)

def all_contacts(contacts):
    list = contacts
    return (list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(user_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

