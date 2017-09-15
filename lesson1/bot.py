
import datetime

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

import logging, ephem
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater("389750746:AAFXpEl5WcZAQsFL3M1u5hrgRcsaZPvZF0w")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_current, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # add photo handler
    updater.start_polling()
    updater.idle()
       

def greet_user(bot, update):
    text = 'Вызван /start'
    #print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    #print(user_text)
    update.message.reply_text(user_text)   

def planet_current(bot, update, args):
    if len(args) == 0:
        update.message.reply_text("Пришли название планеты, нехороший человек!")
    else:
        first_arg = args[0].lower()

        if first_arg.startswith("mar") or first_arg.startswith("мар"):
            pl = ephem.Mars()
        elif first_arg.startswith("ven"):
            pl = ephem.Venus()
        elif first_arg.startswith("jup"):
            pl = ephem.Jupiter()
        else:
            update.message.reply_text("Unknown planet '%s', assuming Uranus. YOUR ANUS" % first_arg)
            pl = ephem.Uranus()

        pl.compute("%s" % datetime.date.today())
        short_constellation_name, full_constellation_name = ephem.constellation(pl)

        response = "The planet %s is now in %s constellation" % (pl.name, full_constellation_name)

        update.message.reply_text(response)



if __name__ == "__main__":
    main()