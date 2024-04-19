import random


logo = [
    '''logo1''',
    '''logo2''',
    '''logo3'''
]









def random_logo():
    random_s = random.choice(logo)
    print(random_s)


# Black: \033[30mHello\033[0m
# Red: \033[31mHello\033[0m
# Green: \033[32mHello\033[0m
# Yellow: \033[33mHello\033[0m
# Blue: \033[34mHello\033[0m
# Magenta: \033[35mHello\033[0m
# Cyan: \033[36mHello\033[0m
# White: \033[37mHello\033[0m