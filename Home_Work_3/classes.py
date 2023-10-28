from collections import UserDict, defaultdict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Birthday:
    def __init__(self, value: str):
        if not datetime.strptime(value, '%d.%m.%Y'):
            raise ValueError("The birthday date must be in format DD.MM.YYYY")
        #перевірка на правильність введеня даних в форматі DD.MM.YYYY
        self.value = value

     
    


class Phone(Field):
    def __init__(self, value: str):
        if not all([len(value) == 10, value.isdigit()]):
            raise ValueError("The phone number must consist of 10 digits")
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)
        
    def remove_phone(self, del_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == del_phone:
                phone = self.phones[i]
                self.phones.remove(phone)
    
    def find_old_phone(self):
        old_phone = str(self.phones[0])
        return(old_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            
    def add_birthday(self, birthday):
        birthday = Birthday(birthday)
        self.birthday = birthday
        return(self.birthday)
                        
    def show_birthday(self):
        birthday = str(self.birthday.value)
        return (birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        return(self.data.get(value))

    def delete(self, name):
        del self.data[name]

    def week_birthdays(self,contacts):
        list_of_birthday = defaultdict(list)
        today = datetime.today().date()
        tomorrow = today + timedelta(days=1)
        for user in contacts:
            name = user["name"]
            birthday = user["birthday"].date()  
            birthday_this_year = birthday.replace(year=tomorrow.year)
            if birthday_this_year < tomorrow:
                birthday_this_year = birthday_this_year.replace(year = (tomorrow.year + 1))
            delta_days = (birthday_this_year - tomorrow).days
            if delta_days < 7:
                day_of_week = birthday_this_year.weekday()
                if day_of_week == 0:
                    list_of_birthday["Monday"].append(name)
                elif day_of_week == 1:
                    list_of_birthday["Tusday"].append(name)
                elif day_of_week == 2:
                    list_of_birthday["Wenesday"].append(name)
                elif day_of_week == 3:
                    list_of_birthday["Thursday"].append(name)
                elif day_of_week == 4:
                    list_of_birthday["Friday"].append(name)
                elif day_of_week == 5 and today.weekday() != 5 and today.weekday() != 6:
                    list_of_birthday["Monday"].append(name)
                elif day_of_week == 6 and today.weekday() != 6:
                    list_of_birthday["Monday"].append(name)
        return(list_of_birthday)

if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")


    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
