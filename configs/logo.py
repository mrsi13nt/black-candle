import random
import os


logo = [
    '''


 ███████████  ████                     █████           █████████                           █████ ████          
░░███░░░░░███░░███                    ░░███           ███░░░░░███                         ░░███ ░░███          
 ░███    ░███ ░███   ██████    ██████  ░███ █████    ███     ░░░   ██████   ████████    ███████  ░███   ██████ 
 ░██████████  ░███  ░░░░░███  ███░░███ ░███░░███    ░███          ░░░░░███ ░░███░░███  ███░░███  ░███  ███░░███
 ░███░░░░░███ ░███   ███████ ░███ ░░░  ░██████░     ░███           ███████  ░███ ░███ ░███ ░███  ░███ ░███████ 
 ░███    ░███ ░███  ███░░███ ░███  ███ ░███░░███    ░░███     ███ ███░░███  ░███ ░███ ░███ ░███  ░███ ░███░░░  
 ███████████  █████░░████████░░██████  ████ █████    ░░█████████ ░░████████ ████ █████░░████████ █████░░██████ 
░░░░░░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░      ░░░░░░░░░   ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░  ░░░░░░  


                                                                   
''',
    '''                                                            
                                                            
                    @AAXXsXAXXsXXXsXXXsA5                   
                5sssXssXXAX22AAA222AXXXssssr@               
              XXssrs3M5hH3hh5555MM3h3352AXsXXX5             
            XXsXXX3hS##SSMMh55353M333hhh3332AXXss           
          XXXAhh3hhhhhGSGGHh33h35Mh3HGHHhHMMh5Xrsss         
        5XXX53MGSGSGHhHh3353hMhh3533hMHHHSGHhh522ssr        
       ssXA52553MMH35hGG#9&&BBB&&BB#SGM5hMM3h35552rrs       
      ArrA35333335hGB&&                  h33335552rrss      
     rss23hhh35hH9&&                99B&   SM53Mhh52irs     
    5Xrr5HMHhHBB&    rs      @G     ss;29&   BSMMHh5XrsX    
    ssr253GB&&&   rA25@      @@&      52AX,   &&B#h35XsX    
    Xsr3H#&&   A5352A       @@@@&      555352   &&BSM5XXA   
    srXMHB   3525hM5         &B@         MM352hs   9MhssX   
    ssAh3  33323M#B#       &&B2&&&       B&HM33355  h3ssX   
    XsA2A555253hH9&9      B@@@@@@&@     @B&SHh335AAAA2sXs   
    AAA3M35255X5G9&B9     B@@@@&BGM     B&&SM55h553hh2XA5   
    AXsAMh3h3h35MS9&B9    B&&&&99hh   #B&&9H35hhhh3M3rsX    
     AssA33h33h333HSB&&&B 9#S9@GA: 9&&&&#GM33333hh35rsA     
      AXX535h33h3333G#&&&&BBBB9B9&&&&&BGh533333h335AXss     
       AXX53533hMMMH3hG9B&@@&@@@&&&B9SM3hMhhh33535AXXX      
        sXXA3523S#GHhMhh3MHMHHHHHMhhhhHMhhhh3A252XXX5       
         5sXXA533hhHMHhHhHM33hh33hHHMHSGhhh3h52AXXA         
           rXssA555hMMHh35Gh53h35HHhh##Shh552XXA2           
             AXsXXA253333355A55253hhhM332AXXXXA             
                XAXXAXXAA222AA2A2222AXXXXXXXs               
                   5AAXXXAXAXXXXsXXXsssAX                   
                         5X2A@ AsX5                         
                                                            
''',
    '''
   .               .    
 .´  ·  .     .  ·  `.  Black Candle 2.0.1
 :  :  :  (\033[31m¯\033[0m)  :  :  :  web scanning tool for devolopers
 `.  ·  ` /¯\ ´  ·  .´  devoloped by : Abd ElRahman Mounir
   `     /¯¯¯\     ´  
 
'''
]



logo_menu = '''
*******************************************************************
*     ____  _            _     ____                _ _            *
*    | __ )| | __ _  ___| | __/ ___|__ _ _ __   __| | | ___       *
*    |  _ \| |/ _` |/ __| |/ / |   / _` | '_ \ / _` | |/ _ \\      *
*    | |_) | | (_| | (__|   <| |__| (_| | | | | (_| | |  __/      *
*    |____/|_|\__,_|\___|_|\_\\____\__,_|_| |_|\__,_|_|\___|       *
*                                                                 *
*                                                                 *
* Black Candle 1.2                                                *
* Coded by Abd El Rahman Mounir                                   *
* Red Teamer and cybersecurity student                            *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************
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