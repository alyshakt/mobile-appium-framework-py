import random
import string


def random_number(range=10):
    amount = random.randrange(range)
    if amount < 1:
        amount = amount + 1
    return amount


def random_string(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength)).lower()


def random_item_for_note():
    items = list()
    items.append('T-shirt')
    items.append('Cafe Latte')
    items.append('Shipping')
    items.append('Service Cancellation')
    items.append('3rd night free')
    items.append('Manager\'s gift')
    num = random_number(len(items))
    return items.__getitem__(num)
