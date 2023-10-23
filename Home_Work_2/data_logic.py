from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass


      #  return(Owner.info(self.owner))        
    # реалізація класу

class Phone(Field):
    pass
    #def check_number(self, phone):
     #   if phone.isdigit() and len(phone) == 10:
      #      return str(phone)
       # else:
        #    return None
    
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
    def delete_phone(self, name):
        pass
    def change_phone(self, name):
        pass
    def search_phone(self, name):
        pass

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.dict = {}
    def add_record(self, name):
        self.dict[Name(name)] = Phone(phone)
    def search_record(self, value):
        pass
    def delete_record(self, value):
        pass

   

    # реалізація класу

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("123456789")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)
print(john_record)
print(book)

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
