# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password_generator():
    """Welcome to the PyPassword Generator!"""
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    list_of_letters = random.choices(letters, k=nr_letters)
    list_of_numbers = random.choices(numbers, k=nr_numbers)
    list_of_symbols = []
    for i in range(nr_symbols):
        list_of_symbols.append(random.choice(symbols))
    lv1password_list = list_of_letters + list_of_symbols + list_of_numbers
    random.shuffle(lv1password_list)
    lv2password = "".join(lv1password_list)
    return lv2password
