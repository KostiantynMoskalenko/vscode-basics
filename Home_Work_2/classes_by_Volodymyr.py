from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


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
        print(list(self.phones))
        #phone_index = self.phones.index(old_phone) # щоб так зробити, old_phone має 
            # бути екземпляром Phone, також в класі Phone потрібно реалізувати магічний метод __eq__
        for i, p in enumerate(self.phones):
            p.value = old_phone
            self.phones[i] = Phone(new_phone)
            print(i)
        # self.phones[phone_index] = new_phone
        print (self.phones)
        
    def delete_phone(self, name):
        pass
    
    def change_phone(self, name):
        pass
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        # key_name = str(name)
        # key_name = key_name.split()[2]
        # key_name = key_name[:-1]
        # self.data[key_name] = name
    def find(self, value):
        return(self.data.get(value))
    def delete(self, name):
        del self.data[name]

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