'''
This is a console bot-assitant.
The bot works with following commands:

Тож наш бот повинен підтримувати наступний список команд:

1) add [ім'я] [телефон]:                    Додати новий контакт з іменем та телефонним номером.
2) change [ім'я] [новий телефон]:           Змінити телефонний номер для вказаного контакту.
3) phone [ім'я]:                            Показати телефонний номер для вказаного контакту.
4) all:                                     Показати всі контакти в адресній книзі.
5) add-birthday [ім'я] [дата народження]:   Додати дату народження для вказаного контакту.
6) show-birthday [ім'я]:                    Показати дату народження для вказаного контакту.
7) birthdays:                               Показати дні народження, які відбудуться протягом наступного тижня.
8) hello:                                   Отримати вітання від бота.
9) close або exit:                          Закрити програму.

'''
from classes import AddressBook, Record



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args 
    rec = Record(name)
    rec.add_phone(phone)
    contacts.add_record(rec)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    new_phone = args[1]
    old_phone = str(rec.find_old_phone())
    rec.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def user_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    return (phone)

def all_contacts(contacts):
   for name, record in contacts.data.items():
       print(record)

@input_error
def add_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    birthday = args[1]
    rec.add_birthday(birthday)
    return "Birthday added."

def show_birthday(args, contacts):
    name = args[0]
    rec = contacts.find(name)
    return((rec.show_birthday()))

def birthdays(contacts):
    birthdays_dict = dict(contacts.week_birthdays(contacts))
    return(birthdays_dict)

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input == '':
            continue
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
            all_contacts(contacts)
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

