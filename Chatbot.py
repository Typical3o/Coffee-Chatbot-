#the purpose of this program is to create simple and fun code to covey an understanding of functions, implementing the input tool, and making a coherent conversation through codee. In addition, through logger and logging, should be able to implement code free of redundant prints, and to log any error faced in the process

import sys
import logging

#logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(filename='filehandler.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s]')
filehandler = logging.FileHandler('filehandler.log')
logger.addHandler(filehandler)
streamhandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamhandler)

order = {}

drink_option = []

milk = []


def coffee_chatbot():
  start = greeting()
  



def mistake():
  logger.error('I\'m sorry, I do not understand, can we try that again?')


def greeting():
  res = input('Welcome to the shop! What can I get you today, something cold or hot? \n[a] Cold \n[b] Hot \n> ')
  if res == 'a':
    return cold_drink()
  elif res == 'b':
    return hot_drink()
  else:
    mistake()
    return greeting()


def milk_option():
  res = input('For your drink, what kind of milk would you like? We have Whole Milk, Half-And-Half, Almond Milk, and Oat Milk. \n[a] Whole Milk \n[b] Half-And-Half \n[c] Almond Milk \n[d] Oat Milk \n[e] No Milk \n > ')
  if res == 'a':
    logger.info('Got it, Whole Milk')
    milk.append('Whole Milk')
    return read_back_order()
  elif res == 'b':
    logger.info('Alright, Half-And-Half... got it!')
    milk.append('Half-And-Half')
    return read_back_order()
  elif res == 'c':
    logger.info(' Almond Milk, You\'ve got it.')
    milk.append('Almond Milk')
    return read_back_order()
  elif res == 'd':
    logger.info('Great Choice! Oat milk it is.')
    milk.append('Oat Milk')
    return read_back_order()
  elif res == 'e':
    logger.info('No problem, no milk it is.')
    milk.append('No Milk')
    return read_back_order()
  else:
    return mistake()
  
  

def cold_drink():
  res = input('For our cold drinks we have a Latte, Cold Brew, Cold Shaken Espresso, and our seasonal Caramel Macchiato. Which would you like? \n[a] Latte \n[b] Cold Brew \n[c] Cold Shaken Espresso \n[d] Caramel Macchiato \n >' )
  if res == 'a':
    logger.info('Great, one cold latte.')
    drink_option.append('Cold Latte')
    order['Cold Latte'] = None
    return milk_option()
  elif res == 'b':
    logger.info('Got it, one Cold Brew.')
    drink_option.append('Cold Brew')
    return read_back_order()
  elif res == 'c':
    logger.info('Alright, one Cold Shaken-Espresso.')
    drink_option.append('Cold Shaken-Espresso')
    return milk_option()
  elif res == 'd':
    logger.info('Great choice, one Caramel Macchiato.')
    drink_option.append('Caramel Macchiato')
    return milk_option()
  else:
    return mistake()




def hot_drink():
  res = input('Our hot drinks include a Latte, Hot Coffee, Cappucino, London Fog, and our seasonal Hot Chocolate. Which can I get you today? \n[a] Hot Latte \n[b] Hot Coffee \n[c] Cappucino \n[d] London Fog \n[e] Seasonal Hot Chocolate \n >')
  if res == 'a':
    logger.info('Got it, a Hot Latte.')
    drink_option.append('Hot Latte')
    return milk_option()
  elif res == 'b':
    logger.info('One Hot Coffee coming right up!')
    drink_option.append('Hot Coffee')
    return milk_option()
  elif res == 'c':
    logger.info('That\'s my favorite; one cappucino!')
    drink_option.append('Cappucino')
    return milk_option()
  elif res == 'd':
    logger.info('Great choice! One London Fog coming up.')
    drink_option.append('London Fog')
    return milk_option()
  elif res == 'e':
    logger.info('Great Choice! The Hot Chocolate is great; coming right up!')
    drink_option.append('Hot Chocolate')
    return read_back_order()
  else:
    return mistake()

    

def additional_drink():
  res = input('Will that other drink be hot or cold? \n[a] Hot \n[b] Cold \n >')
  if res == 'a':
    return hot_drink()
  elif res == 'b':
    return cold_drink()
  else:
    return mistake()


def read_back_order():
  if len(drink_option) <= 1:
    order_back = dict(drink=drink_option, milk_choice=milk)
    print('Alright, so I have here {drink} with {milk_choice}.'.format(**order_back))
    res = input('Can I get you anything else today? \n[a] Yes \n[b] No \n >')
    if res == 'a':
      return additional_drink()
    else:
      name = input('Great! I\'ll get started with your drink right away! Can I get a name for when your drink is ready? ')
      logger.info('Great name! I\'ll call you when it is ready, ' + str(name) +'!')
  elif len(drink_option) > 1:
    big_order_back = dict(drink1 = drink_option[0], drink2 = drink_option[1], milk_choice1 = milk[0], milk_choice2 = milk[1])
    print('Alright, so I have here {drink1} with {milk_choice1} and a {drink2} with {milk_choice2}'.format(**big_order_back))
    res = input('Can I get a name for the order? ')
    logger.info('Great name! I\'ll call you when it\'s ready!')


coffee_chatbot()


git remote add origin https://github.com/Typical3o/Coffee-Chatbot-.git
git branch -M main
git push -u origin main