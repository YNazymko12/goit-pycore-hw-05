from decorators import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"The name {name} is already exists on your contacts list."
    else:
        contacts[name] = phone
        return "Contact added." 

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"The name {name} is not on your contacts list yet."       

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
        return f"The name {name} is not on your contacts list yet."       

@input_error   
def show_all(contacts):
    res = ""  

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            res += f"{name}: {phone} \n"
        return res.rstrip("\n")  