contacts = {}

def hello():
    print("How can I help you?")

def add(name, phone):
    phone_number = phone.replace(" ", "") # видаляємо всі пробіли з номеру телефону
    name_parts = name.split(' ')
    if len(name_parts) == 1: # якщо ввід містить тільки ім'я
        name = name.strip() # видаляємо зайві пробіли
        contacts[name] = phone_number[-10:] # додати контакт до словника
        print(f"{name}'s phone number ({phone_number[-10:]}) has been added to contacts.")
    else: # якщо ввід містить ім'я та прізвище
        first_name = name_parts[0].strip()
        last_name = ' '.join(name_parts[1:]).strip()
        contacts[f"{first_name} {last_name}"] = phone_number[-10:] # додати контакт до словника
        print(f"{first_name} {last_name}'s phone number ({phone_number[-10:]}) has been added to contacts.")

def change(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"{name}'s phone number has been updated to {phone}.")
    else:
        print(f"{name} is not in contacts.")

def phone(name):
    matching_contacts = [contact for contact in contacts if name in contact]
    if matching_contacts:
        for contact in matching_contacts:
            print(f"{contact}: {contacts[contact]}")
    else:
        print(f"{name} is not in contacts.")

def show_all():
    if contacts:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts to show.")

def exit():
    print("Good bye!")
    quit()

def parse_command(command):
    parts = command.split(' ')
    if parts[0].lower() == 'hello':
        hello()
    elif parts[0].lower() == 'add':
        if len(parts) == 3:
            add(parts[1], parts[2])
        else:
            print("Invalid name or phone number format.  Please enter your first name and, if desired, your last name with a space, and your phone number without spaces.")
    elif parts[0].lower() == 'change':
        change(parts[1], parts[2])
    elif parts[0].lower() == 'phone':
        phone(parts[1])
    elif parts[0].lower() == 'show':
        show_all()
    elif any(word in parts for word in ['good', 'bye', 'close', 'exit']):
        exit()
    else:
        print(f"Invalid command: {command}")

def main():
    while True:
        command = input("Enter command: ")
        parse_command(command)

if __name__ == '__main__':
    main()