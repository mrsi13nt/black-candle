import random
import os


logo = [
    '''logo1''',
    '''logo2''',
    '''logo3'''
]


logo_menu = '''
   .               .    
 .´  ·  .     .  ·  `.  Black Candle 2.0.1
 :  :  :  (\033[31m¯\033[0m)  :  :  :  web scanning tool for devolopers
 `.  ·  ` /¯\ ´  ·  .´  More info at: https://yourwebsite.com
   `     /¯¯¯\     ´  
 
'''


examples_help = '''examples:
black_candle -u www.google.com -sql'''



def random_logo():
#for clean the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# for printing random logo
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