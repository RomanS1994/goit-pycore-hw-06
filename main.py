from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def check_phone(self):
        try:
            if len(self.value) == 10 and self.value.isdigit():
                return self.value 
        except ValueError:
            print("Phone number must be exactly 10 numerals")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
    
    def remove_phone(self, phone_number):
        try: 
            self.phones.remove(phone_number)
        except ValueError as e:
            print(e)


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone == old_phone:
                self.phones[index] = Phone(new_phone)
                print(f"Phone {old_phone} changed to {new_phone}")
                return
            else:
                print(f"Phone {old_phone} not found")
    
    def find_phone(self, phone_number):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone.value
        except ValueError as e:
            print(e)

        


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f'Contact {record.name} added' )
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f'Contact with name "{name}" not found')
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f'Contact with name "{name}" not found')





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
