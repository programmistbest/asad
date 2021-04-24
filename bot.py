import config 
import telebot 
import requests
from telebot import types

bot = telebot.TeleBot(config.token)
#Декодировать json, функцией json()
reponse = requests.get(config.url).json()

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=true, row_width=2)
	itembtn1 = types.KeyboardButton('USD')
	itembtn2 = types.KeyboardButton('EUR')
	itembtn3 = types.KeyboardButton('RUB')
	itembtn4 = types.KeyboardButton('BTC')
	itembtn5 = types.KeyboardButton('AUD')
	itembtn6 = types.KeyboardButton('AUH')
	itembtn7 = types.KeyboardButton('CAD')
	itembtn8 = types.KeyboardButton('CHF')
	itembtn9 = types.KeyboardButton('CYN')
	itembtn10 = types.KeyboardButton('GBP')
	markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)
	msg = bot.send_message(message.chat.id,
		"Узнать наличый курс  Привет Банк (в отделениях)", replay_markup=markup)
	bot.register_next_step_handler(msg, process_coin_step)

	def process coin step(message):
		try:
			markup = types.ReplyKeyboardRemove(selective=False)

			for coin in reponse:
				if (message.text == coin['ccy']):
					bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']),
						replay_markup=markup, parse_mode="Markdown")

				except exception as e:
					bot.reply_to(message, 'ooops!')

					def printCoin(buy, sale):
						'''Вывод курса пользователю'''
						return " *Курс покупка:*" +str(buy) + "\n *Курс продажи:*" +str(sale)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step  handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING it will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
	bot.polling(none_stop=True)
	