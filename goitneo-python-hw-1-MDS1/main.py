'''
This is a console bot-assitant.
The bot works with following commands:

"hello":                    Replies to the console with the message "How can I help you?"
"add username phone":       User enters 'add' command, username and phone number (necessarily with a space) and the bot saves a new contact in memory. 
"change username phone":    User enters 'change' command username and NEW phone number (necessarily with a space) and the bot stores in memory the new
                            telephone number phone for the username contact, which already exists in the notebook.
"phone username":           User enters 'phone' command and username and the bot displays the phone number for the specified username contact in the console.
"all":                      With this command, the bot outputs all saved contacts with phone numbers to the console.
"close", "exit":            For any of these commands, the bot ends its work after outputting the message "Good bye!" to the console and completes its execution.

'''



#parser for entered command
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


#the function adds a new contact to the dictionary
def add_contact(args, contacts):
    try:
        name, phone = args 
        if name in contacts:
            return "The contact already exists. Please choose another name."
        contacts[name] = phone
    except ValueError:
        return "The command 'add' shoud have 2 arguments - 'Name'(1 word) and 'Phone'(1 phone number)"
    return "Contact added."


#the function changes a phone number for existing contact
def change_contact(args, contacts):
    try:
        name = args[0]
        new_phone = args[1]
    except IndexError:
        return "The command 'change' shoud have 2 arguments - 'Name'(1 word) and 'Phone'(1 new phone number)"
    phone = contacts.get(name)
    if phone == None:
        phone = 'User is not found'
        return (phone)
    contacts[name] = new_phone
    return "Contact updated."


#the function returns the phone number of an existing contact
def user_phone(args, contacts):
    try:
        name = args[0]   
        phone = contacts.get(name)
    except IndexError:
        return "Invalid command. The command 'phone' should have one argument - 'Name'." 
    if len(args) > 1:
        return "Invalid command. The command 'phone' should have one argument - 'Name'." 
    if phone == None:
        phone = "User is not found"
    return (phone)


#the function returns all contacts with their phone numbers
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

