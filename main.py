welcome_txt = "Привет! Благодарю за подписку. Держи чек-лист “Как набрать высокий балл по SAT и поступить в ВУЗ мечты?" # /start дегенды басканда
every_1_hour_txt = "Дальше в этом боте я буду делиться уникальной инфой по SAT.\n\nХочешь набрать хороший балл, поступить в топовый ВУЗ и получить востребованную профессию? Тебе повезло!\n\nСкоро расскажу об ошибках, из-за которых сотни тысяч старшеклассников проваливают SAT..\n\nИ расскажу, как ты можешь эти ошибки избежать👌" # ар быр сагат сайын жыберылетын сообщениенын тексты
document_name = "file.txt" # жыберу керек документтын аты
keyword = "жибер" # ключевое слово кандай болады соны жазасын
keyword_txt = "ПРОГРЕВАЮЩИЙ ВИДОС" # ключевое слово жазганнан кейын пользовательдерге кандай сообщение жыберыледы соны жазасын
secret = "хочу поступить"
secrett = "Хочу поступить"
token = "1427672563:AAGlQjeqiXu4HsXgWj2IoNuSgYw9YOf0IIQ"
checklist = "https://drive.google.com/drive/u/1/my-drive"
secrettxt = "Ты прочитал предыдущий чек-лист до конца, молодец! Значит, ты решительно настроен обучаться за границей. Я это уважаю! Держи обещанный подарок:"
secrettxt2 = "https://drive.google.com/file/d/1Xu8_wrPfbHuP6Z6sF-yv3kaZtEQYF6uz/view?usp=sharing"
hour24 = "Большинство сдdcdcdающих SAT жалеют об одном:\n\n“ПОЧЕМУ Я НЕ НАЧАЛ(А) ГОТОВИТЬСЯ РАНЬШЕ?”\n\n“НА ЧТО Я ТРАТИЛ СВОЕ ВРЕМЯ?”\n\nЗапомни: каким бы умным ты ни был, подготовка к SAT требует времени. От 2 до 18 месяцев. Чем раньше начнешь - тем выше наберешь.\n\nКонечно, есть факторы, которые могут ускорить подготовку, например, хороший учитель. Но даже лучший учитель не сделает из тебя вундеркинда за ночь.\n\nГрант в ВУЗе мечты - это путешествия, лучшие знания, востребованная профессия. Готов ли ты рискнуть всем этим из-за сериала? Гулянок? Инстаграма?" + "Я бы дал себе такой совет в 10-11 классе:\nРасставь приоритеты. Что для тебя сейчас важнее: “покайфовать” в моменте, или поднапрячься и обеспечить себе будущее?\n\nЧасики тикают. Лишняя минута подготовки может дать тебе дополнительный балл на экзамене. И этот балл может решить твою судьбу." + "Но есть и обратная сторона.."
hour48 = "НЕ УЧИСЬ МНОГО! Секрет эффективного обучения\n\nДа, картинка красивая: кофе, книжки, наушники со спокойной музыкой, и учеба 10 часов подряд. Но 10 часов подготовки, и даже 5, могут привести к ВЫГОРАНИЮ.\n\nЯ раньше так и делал. В начале все было круто, но уже через неделю я не мог смотреть на учебники без отвращения. Заставить себя учиться тоже не мог. Хотел только лежать и кушать печеньки.\n\nЭто обратная сторона усердной подготовки: мозг устает от долгой рутины.\nОтсюда и секрет эффективности - УМЕРЕННОСТЬ.\n3 часа в день - это хорошо. Только здесь главное - учиться без пропусков, по четкому графику. А то и забросить недалеко.\n\nНапример, я ставлю своим ученикам такое расписание: 1-день - writing, 2-й день - математика. Так они не устают от тонны текстов, еще и постоянно улучшают свой score.\n\n**Поэтому, учись не много, а с умом!**\n\nТолько не думай, что учиться с умом - это лишь про умеренность. Есть еще куча секретов! Чтобы узнать один, я потратил ЦЕЛЫЙ ГОД, а второй секрет бустнул мой прогресс в 5 раз НА РОВНОМ МЕСТЕ."
import time
import telebot
from telebot import types
import threading
from telebot import types

bot = telebot.TeleBot(token)
users = []
userss = []

def send_every_1_hour():
	one_hour = 7200
	while True:
		for i, user in enumerate(users):
			Time = time.time()

			if Time - user[1] > one_hour and user[2] == 0:
				bot.send_message(user[0], every_1_hour_txt)
				user[2] += 1
				time.sleep(1)

			if Time - user[1] > 86400 + one_hour and user[2] != 0:
				if user[2] == 1:
					bot.send_photo(user[0], 'https://drive.google.com/file/d/1NzGgMTUkhjClXKlUskCq1B5MOuG8ih_U/view?usp=sharing')
					bot.send_message(user[0], hour24)
					user[1] = Time
					user[2] += 1
					one_hour = 0
				else:
					bot.send_photo(user[0], 'https://drive.google.com/file/d/1NuAnFf0mXIKiFIUPv4RYSUKPvFORFf6I/view?usp=sharing')
					bot.send_message(user[0], hour48)
					del users[i]

				time.sleep(1)
				



@bot.message_handler(commands=['start'])
def welcome(message):
	
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='⚡Читать чек-лист', url='https://drive.google.com/file/d/15Ai8_sq6ngSbeQAR2p9IvzV-UgENOVrJ/view?usp=drivesdk')
	markup.add(btn_my_site)
	bot.send_message(message.chat.id, welcome_txt, reply_markup = markup)
	if message.chat.id not in userss:
		userss.append(message.chat.id)
	if message.chat.id not in users:
		users.append([message.chat.id, time.time(), 0])

@bot.message_handler(content_types=['text'])
def handle_keyword(message):
	if message.text == secret or message.text == secrett:
		markup = types.InlineKeyboardMarkup()
		btn_my_site= types.InlineKeyboardButton(text='⚡Читать второй чек-лист', url='https://drive.google.com/file/d/1Xu8_wrPfbHuP6Z6sF-yv3kaZtEQYF6uz/view?usp=sharing')
		markup.add(btn_my_site)
		bot.send_message(message.chat.id, secrettxt, reply_markup = markup)
	if message.chat.id not in userss:
		userss.append(message.chat.id)

@bot.message_handler(content_types=['text'])
def handle_keyword(message):
	if message.text == keyword:
		bot.send_message(message.chat.id, "I got it")
		for user in userss:
			bot.send_message(user, keyword_txt)
			time.sleep(1)



if __name__ == "__main__":
	thread = threading.Thread(target=send_every_1_hour, daemon=True)
	thread.start()
	bot.polling(none_stop=True)
