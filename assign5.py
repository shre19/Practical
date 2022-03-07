from hashlib import new


name = "Sales Bot"
mood = "good"

products = {
    "mouse": 500,
    "keyboard": 400,
    "laptop": 60000,
    "gaming laptop": 75000,
    "pc": 80000,
    "cpu": 40000,
    "gaming chair": 15000,
    "earphones": 500,
    "headphones": 1000
}

responses = {
    "what is your name?": 
    "My name is {0}.".format(name),
    "how are you?": 
        "I am feeling {0}.".format(mood),
    "bye":
        "Bye bye have a lovely day :)",
    "default": 
        "Sorry I have no information about this please call out customer care number 1800-900-800."
}

def give_price(product):
    for k, v in products.items():
        if k == product:
            print(v)
    else:
        print("Sorry entered product information is not available.")


def match(curr_text):
    if "name" in curr_text:
        new_text = "what is your name?"
    elif "how are" in curr_text:
        new_text = "how are you?"
    elif "price" in curr_text:
        s = curr_text.split("price of")[1]
        give_price(s)
        return
    elif "bye" in curr_text:
        new_text = "bye"
    else:
        new_text = "default"
    return new_text

def res(message):
    if message in responses:
        new_message = responses[message]
    else:
        new_message = responses["default"]
    return new_message

while 1:
    user_input = input()
    user_input = user_input.lower()
    related_input = match(user_input)
    op_message = res(related_input)
    print(op_message)
    if("bye" in op_message):
        break

