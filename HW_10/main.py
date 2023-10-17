from collections import UserDict


class Field:                                # +++
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    

class Name(Field):                          # +?
    ...


class Phone(Field):                         # +++
        
    def __init__(self, phone: str) -> None:
        new_phone = phone.strip()
        for c in '+( )-.':
            new_phone = new_phone.replace(c, "")
        if len(new_phone) == 10 and new_phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError(f"{phone} - incorrect phone number")
            
    def __str__(self):
        return self.value


class Record:                               # +++
    
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
        
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return 
        raise ValueError(f"Number {old_phone} not found")  

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):            # +++
    
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
