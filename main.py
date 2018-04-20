import discord
import asyncio
import requests
import time
import string
import random
import copy

DISCORD_BOT_TOKEN = 'token'

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

client = discord.Client()
#http = discord.http

save_channel = 0
admin_list = ['265474107666202634', '282660110545846272']
bonus_list = ['265474107666202634', '282660110545846272', '175571075931963393']
admin_channel_list = ['434056729362169857', '433267590937444364', '43568779755939430']

prefix = '>'
stops = 0
#lock = 0

event_list = []
is_event = 0

quiz_channel = 0
quiz = 0
quiz_number = -1
quiz_numbers = -1
set_answer = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

question = ['1) https://sun9-6.userapi.com/c840724/v840724591/74499/x8hB5rkgIkU.jpg',
			'2) https://pp.userapi.com/c846320/v846320591/23582/SClHqmmWE0Y.jpg',
			'3) https://pp.userapi.com/c834100/v834100591/116733/OuwBfc0GKwc.jpg',
			'4) https://pp.userapi.com/c841639/v841639591/7ee08/UC7dluXRGgI.jpg',
			'5) https://pp.userapi.com/c834202/v834202591/d6b84/AnYJtA--lE0.jpg',
			'6) https://pp.userapi.com/c824411/v824411591/1164c1/5mZIEYsbHAI.jpg',
			'7) https://pp.userapi.com/c846017/v846017591/24701/Bh25snWBCl8.jpg',
			'8) https://pp.userapi.com/c846219/v846219591/23a84/EV5tVSseGj4.jpg',
			'9) https://pp.userapi.com/c847020/v847020591/2557b/K21NUu_G_ec.jpg',
			'10) https://pp.userapi.com/c834203/v834203591/117502/4NYjkoSAtnU.jpg',
			'11) https://pp.userapi.com/c831508/v831508591/d3c68/qtlwIGrbvwc.jpg',
			'12) https://pp.userapi.com/c830609/v830609591/cf56e/NIfBShi_EGM.jpg',
			'13) https://pp.userapi.com/c834104/v834104533/112c65/A2mmg_mLiK4.jpg',
			'14) https://pp.userapi.com/c845019/v845019533/2c064/t6Z4_1yxetE.jpg',
			'15) https://pp.userapi.com/c844720/v844720523/28eed/Im1kZS1WoKI.jpg',
			'16) https://pp.userapi.com/c834100/v834100897/114102/qeXr4eut2oU.jpg',
			'17) https://pp.userapi.com/c847123/v847123209/2630f/QZKvAWreGN4.jpg',
			'18) https://pp.userapi.com/c830108/v830108944/d1c82/ZnnQbYyVA-g.jpg',
			'19) https://pp.userapi.com/c841221/v841221058/74759/2qj4ClVx0GQ.jpg',
			'20) https://pp.userapi.com/c831309/v831309589/ca39f/_2ATdwnWZVE.jpg',
			'21) http://animeru.tv/assets/images/resources/1575/1791ca9d6eb0fa2c28e5f15000d518258641d54a.jpg',
			'22) https://scontent-arn2-1.cdninstagram.com/vp/ae79ff0ec82053fc68d40dae663466c8/5B2FD62C/t51.2885-15/e35/23164144_587504724707054_4524634221112721408_n.jpg',
			'23) https://awesomereviews.ru/wp-content/uploads/2017/09/%D0%91%D0%BB%D0%B8%D1%82%D1%86-%D0%A2%D0%BE%D0%BB%D0%BA%D0%B5%D1%80.jpg',
			'24) http://i.imgur.com/QYr2C7c.jpg',
			'25) https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYVb09iGL5Fe63aMQx8hXnsECcuqpxupUciSbXnHf2j10Ue_4dTg',
			'26) https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIuyzrQBascnms3B1vOeTJF6NHfQYIw4HlJZMdt9KsHtKVe64Jfw',
			'27) http://nisamerica.com/lovelive/images/screenshots/9.jpg',
			'28) https://pbs.twimg.com/media/C9xjyVFXkAIiyhs.jpg']

quiz_answer = [['врата штейна', 'врата штайнера'],
		  ['сегодняшний ужин для эмии', 'сегодняшнее меню для эмии'],
		  ['проект воспитания девочек-волшебниц'],
		  ['кейон!', 'кейон', 'легкая музыка!', 'легкая музыка', 'клуб легкой музыки'],
		  ['созданный в бездне'],
		  ['невероятные приключения джоджо', 'джоджо', 'жожо'],
		  ['девочка-волшебница мадока магика', 'девочка-волшебница мадока', 'девочка волшебница мадока'],
		  ['загадочная история коноханы', 'сказания о конохане', 'история коноханы'],
		  ['садистская смесь'],
		  ['любовь и тьма неприятностей'],
		  ['судный день', 'день гнева'],
		  ['ведьмина магия в деле', 'ведьма за работой'],
		  ['бтууум!', 'взрыв', 'взрыв!', 'бтууум'],
		  ['сердцу хочеться кричать', 'сердцу хочеться петь'],
		  ['шарлотта'],
		  ['связанные'],
		  ['город, в котором меня нет', 'город в котором меня нет', 'город, в котором пропал лишь я', 'город в котором пропал лишь я'],
		  ['слуга вампир', 'сервамп'],
		  ['проклятие мультивыбора превратило мою жизнь в ад', 'проклятие мультивыбора', 'проклятье мультивыбора превратило мою жизнь в ад', 'проклятье мультивыбора'],
		  ['полулюди', 'получеловек', 'аджин'],
		  ['скучный мир в котором не существует понятия грязные шуточки', 'скучный мир, в котором не существует понятия грязные шуточки', 'скучный мир, в котором не существует самой концепции похабных шуток', 'скучный мир в котором не существует самой идеи похабных шуток', 'трусонюх'],
		  ['повар-боец сома: в поисках божественного рецепта', 'повар боец сома', 'боевой повар сома', 'в поисках божественного рецепта', 'повар-боец сома'],
		  ['возрождающие'],
		  ['притворная любовь'],
		  ['кейджо', 'кэйджо!!!!!!!!', 'кейджо!!!!!!!!', 'кэйджо'],
		  ['баскетбол куроко'],
		  ['живая любовь'],
		  ['эроманга-сенсей', 'эроманга сенсей']]

mat_list = []

kusi_list = ['https://media.discordapp.net/attachments/243749885294280704/436607652349607946/1366009488_kus.gif', 'https://media.discordapp.net/attachments/243749885294280704/436608940290211860/1514641844_1510391300_1483900263_demichanwakataritai-episode1-omake-3.gif']
stroke_list = ['https://pa1.narvii.com/6564/b84e81eb41fdcb8f4d09580010d0129f844ef2e1_hq.gif',
            'https://pa1.narvii.com/6409/09635809b718249a519f67ebe6767e838136c4e9_hq.gif',
            'https://i.imgur.com/nCp9C6y.gif']
crazy_list = ['https://49.media.tumblr.com/c0a3938a185e4edbc5b6fa4df344b5e1/tumblr_n7otvic0AI1qckkfko1_r2_500.gif']
fs_list = ['https://i.pinimg.com/originals/47/55/39/475539cfe4876c876c91ffbc0a962d4a.gif',
            'http://i0.kym-cdn.com/photos/images/original/000/448/492/bfa.gif',
            'http://cs.pikabu.ru/images/big_size_comm/2012-12_2/13549741925392.gif',
            'http://i0.kym-cdn.com/photos/images/original/000/448/521/e2c.gif',
            'http://i0.kym-cdn.com/photos/images/newsfeed/000/809/458/237.gif',
            'https://media.giphy.com/media/BFUcrw8V2WnyU/giphy.gif']
#------------------------------------------------------------------------------------------------------------------------------
#         Economics
#------------------------------------------------------------------------------------------------------------------------------
daily_id = []
names = []
cookie = []
waifu_list_own = []
waifu_list_id = []
waifu_list_cost = []


report = 0

channel_list = []
f = open('channel_list', 'r')
line1 = f.readline()
line2 = f.readline()
c = 0
while line1:
	channel_list.append(line1)
	channel_list.append(line2)
	line1 = f.readline()
	line2 = str(f.readline())
	print(str((c // 2) + 1) + ')' + channel_list[c][:-1] + ' ' + channel_list[c + 1][:-1])
	c = c + 2
f.close()

print('------')

f = open('daily', 'r')
line1 = f.readline()
c = 0
while line1:
	daily_id.append(line1[:-1])
	line1 = f.readline()
	print(str(c + 1) + ')' + daily_id[c])
	c = c + 1
f.close()

f = open('cookie', 'r')
line1 = f.readline()
line2 = f.readline()
while line1:
	names.append(line1[:-1])
	cookie.append(line2[:-1])
	line1 = f.readline()
	line2 = f.readline()
f.close()

f = open('mat', 'r')
line1 = f.readline()
while line1:
	mat_list.append(line1[:-1])
	line1 = f.readline()
print('mat_list is ready.')
f.close()

f = open('waifu', 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
c = 0
while line1:
	waifu_list_own.append(line1[:-1])
	waifu_list_id.append(line2[:-1])
	waifu_list_cost.append(line3[:-1])
	line1 = f.readline()
	line2 = f.readline()
	line3 = f.readline()
	c = c + 3
f.close()

print('------')

random.seed()


async def daily_cookie():
	global daily_id
	await client.wait_until_ready()
	while not client.is_closed:
		daily_id = []
		f = open('daily', 'w')
		for s in daily_id:
			f.write(s + "\n")
		f.close()
		print('---------[command]:daily_cookie')
		await asyncio.sleep(3600)

client.loop.create_task(daily_cookie())

#async def presences():
#	await client.wait_until_ready()
#	while not client.is_closed:
#		await client.change_presence(game=discord.Game(name='Здесь'))
#		await asyncio.sleep(1)
#		await client.change_presence(game=discord.Game(name='могла быть'))
#		await asyncio.sleep(1)
#		await client.change_presence(game=discord.Game(name='ваша реклама!'))
#		await asyncio.sleep(1)
#
#client.loop.create_task(presences())

@client.event
async def on_member_join(member):
	print('---------[command]:' + str(member) + ' join')
	role = discord.utils.get(member.server.roles, id='423111586832580608')
	await client.add_roles(member, role)
	c = random.randint(1, 2)
	if c == 1:
		await client.send_message(client.get_channel('432948785216225281'), 'Добро пожаловать, ' + member.mention + ', мы тебя очень ждали! :kannabear:')
	if c == 2:
		await client.send_message(client.get_channel('432948785216225281'), 'Приветствую ' + member.mention + ', мой дорогой друг. Располагайся по-уютнее. ╰(´︶`)╯♡')

@client.event
async def on_member_remove(member):
	print('---------[command]:' + str(member) + ' leave')
	c = random.randint(1, 2)
	if c == 1:
		await client.send_message(client.get_channel('432948785216225281'), 'Прощай, ' + member.mention + ', будем ждать тебя в гости снова! :BibleRem:')
	if c == 2:
		await client.send_message(client.get_channel('432948785216225281'), member.mention + ', ушёл красиво, по-английски.')

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name='самого крутого бота'))

@client.event
async def on_message(message):

	#server = discord.Server()

	#print('<' + message.channel.name + '>' + '[' + message.author.name + '|' + message.author.id + ']' + message.content)
	print('<' + message.server.id + '>' + '[' + message.author.name + '|' + message.author.id + ']' + message.content)

	global stops
	global save_channel
	global question
	global quiz_channel
	global quiz
	global quiz_number
	global quiz_numbers
	global set_answer
	global quiz_answer
	global daily_id
	global mat_list
	global cookie
	global names
	global report
	global is_event
	global bonus_list
	global kusi_list
	global waifu_list_own
	global waifu_list_id
	global waifu_list_cost

	if message.content.startswith(prefix + 'btcprice'):
		print('---------[command]: btcprice ')
		f = open('config', 'w')
		f.write(message.author)
		f.close()
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]: btcprice\n```')
		btc_price_usd, btc_price_rub = get_btc_price()
		await client.send_message(message.channel, 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub))
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'login') and message.author.id == '282660110545846272':
		print('---------[command]:!login')
		report = message.author
		await client.delete_message(message)

	#if '<@282660110545846272>' in message.content and message.author.id != '282660110545846272' and message.author.id != '434785638840008738':
	#    print('---------[command]:mention cookie')
	#    #await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:mention cookie\n```')
	#    await client.send_message(message.channel, 'Хватит ддосить моего Создателя!!!')
	#    await client.delete_message(message)

	#if '<@175571075931963393>' in message.content:
	#    print('---------[command]:mention soya')
	#    #await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:mention soya\n```')
	#    await client.send_message(message.channel, ':sparkles::regional_indicator_s: :regional_indicator_o: :regional_indicator_y: :regional_indicator_a:      :regional_indicator_j: :regional_indicator_o: :regional_indicator_n: :regional_indicator_e: :regional_indicator_s::sparkles:')
	#    #await client.delete_message(message)

	if message.content.startswith(prefix + 'ddos') and message.author.id in admin_list:
		if message.author.id in admin_list:
			print('---------[command]:!ddos ' + message.content[6:])
			#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!ddos ' + message.content[6:] + '\n```')
			i = 0
			stops = 0
			while i < 30:
				i = i + 1
				if(stops == 1):
					break
				await client.send_message(message.channel, message.content[6:])
				time.sleep(0.5)
			stops = 0
		await client.delete_message(message)

	if (await strcmp(message.content, prefix + 'stop') == 1):
		print('---------[command]:!stop')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!stop\n```')
		stops = 1
		await client.delete_message(message)

	if await strcmp(message.content.lower(), 'печенюха') or await strcmp(message.content.lower(), 'печенька'):
		print('---------[command]:!cookie')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!cookie\n```')
		await client.send_message(message.channel, "О, я тоже хочу, поделитесь?:cookie:")

	if await strcmp(message.content, prefix + 'ping'):
		print('---------[command]:!ping')
		await client.send_message(message.channel, ':sparkles:Туточки:sparkles:')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'hi'):
		print('---------[command]:!hi')
	   #await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!hi')
		await client.send_message(message.channel, ':sparkles:' + message.author.name + ' приветствует всех:sparkles:\n')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'pic'):
		print('---------[command]:!pic')
		await client.send_message(message.channel, 'Держи арт!')
		await client.send_file(message.channel, 'pic/konachan.jpg')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'gm'):
		print('---------[command]:!gm')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!gm\n```')
		await client.send_message(message.channel, ':hugging:С добрым утречком:hugging:')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'help'):
		print('---------[command]:!help')
		await client.send_message(message.channel, '```css\n' +
												   '[Pineapple Cookie help]\n\n' +
												   '<Cookie>\n' +
												   prefix + 'daily - Получить часовую порцию печенюх.\n' +
												   prefix + 'cookie / ' + prefix +'me - Узнать свой баланс печенюх.\n' +
												   prefix + 'roll <ставка> - Поставить печенюхи на рулетке.\n' +
												   prefix + 'give <кому> <сколько> - Поделиться печенюхами с другом.\n' +
												   prefix + 'rank - Посмотреть на обжор.\n\n' +
												   '<Events>\n' +
												   prefix + 'reg - Регистрация для участия в ивентах. Выдает соответствующую роль.\n\n' +												   
												   '<Waifu>\n' +
												   prefix + 'get2d <кто> <цена> - Приобрести или выкупить вайфу.\n' +
												   prefix + '2d - Список вайфу.\n\n' +
												   '<Fun>\n' +
												   #'Печенюха/печенька - Попросит вкуснях. Это две команды. Буквы могут быть любого размера.\nПишется без префикса.\n' +
												   #'Меншн Сони выдаст интересный набор смайликов))). Но не стоит слишком часто юзать эту функцию.\nГрозит перманентным баном по айди на доступ к этой команде.\n' +
												   prefix + 'say <текст> - Напишет ваше сообщение.\n' +
												   prefix + 'stroke <кого> - Погладить кого-то. [20 печенюх]\n' +
												   prefix + 'fs - Покрутить пальчиками. [15 печенюх]\n' +
												   prefix + 'hi - Поприветствует всех от вашего имени.\n' +
												   prefix + 'gm - Охайё, т.е доброе утро)).\n\n' +
												   '<Help>\n' +
												   prefix + 'help - Вызов этой справки.\n' +
												   prefix + 'ping - Сомневаешься в том, что он жив???\n' +
												   prefix + 'report <текст> - Отправить сообщение разработчику. Баги, пожелания, предложения руки и сердца кидать сюда-ня.\n' +
												   '```')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'oldhelp') == 1 and message.author.id in admin_list:
		print('---------[command]:!oldhelp')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!help\n```')
		await client.send_message(message.channel, '```css\n' +
												   '[cookie help]\n\n' +
												   'Печенюха/печенька - Попросит вкуснях. Это две команды. Буквы могут быть любого размера.\nПишется без префикса.\n\n' +
												   'Меншн Сони выдаст интересный набор смайликов))). Но не стоит слишком часто юзать эту функцию.\nГрозит перманентным баном по айди на доступ к этой команде.\n\n' +
												   prefix + 'say <текст> - Напишет ваше сообщение.\n\n' +
												   prefix + 'hi - Поприветствует всех от вашего имени.\n\n' +
												   prefix + 'gm - Охайё, т.е доброе утро)).\n\n' +
												   prefix + 'help - Вызов этой справки.' +
												   '```')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'save') == 1 and message.author.id in admin_list:
		print('---------[command]:!save')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!save```')
		save_channel = message.channel
		f = open('channel_list', 'a')
		f.write(save_channel.name + '\n' + save_channel.id)
		f.close
		await client.delete_message(message)

	if message.content.startswith(prefix + 'say '):
		print('---------[command]:!say')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!say```')
		await client.send_message(message.channel, message.content[5:])
		await client.delete_message(message)

	if message.content.startswith(prefix + 'says ') and message.author.id in admin_list:
		print('---------[command]:!say')
		em = discord.Embed(description=message.content[6:], colour=0xC5934B)
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)

	if message.content.startswith(prefix + 'report '):
		print('---------[command]:!report')
		await client.send_message(discord.utils.get(message.server.members, id='282660110545846272'), '<' + message.author.name + '|' + message.author.id+ '>'+ ' ' + message.content[8:])
		await client.delete_message(message)

	if message.content.startswith(prefix + 'sayhim') and message.author.id in admin_list:
		print('---------[command]:!sayhim')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!sayhim```')
		await client.send_message(client.get_channel(channel_list[int(message.content[8]) * 2 - 1][:-1]), message.content[10:])
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'start quiz') == 1 and message.author.id in admin_list:
		print('---------[command]:!start quiz')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!start quiz\n```')
		quiz_channel = message.channel
		quiz = 1
		await client.send_message(message.channel, 'Викторина началась!')
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'stop quiz') == 1 and message.author.id in admin_list:
		print('---------[command]:!stop quiz')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!stop quiz\n```')
		quiz_channel = 0
		quiz = 0
		await client.send_message(message.channel, 'Викторина окончена))\n\nОгромное спасибо спонсорам сегодняшней викторины - Rumata и <@265474107666202634>')
		await client.delete_message(message)

	if message.content.startswith(prefix + 'quiz ')  and message.author.id in admin_list and quiz == 1 and message.channel != quiz_channel:
		quiz_number = int(message.content[6:]) - 1
		quiz_numbers = quiz_number
		print('---------[command]:!quiz ' + str(quiz_number))
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quiz ' + str(quiz_number) + '\n```')
		await client.send_message(quiz_channel, question[quiz_number])
		await client.delete_message(message)

	if message.content.startswith(prefix + 'quizans') and message.author.id in admin_list:
		print('---------[command]:!quizans ' + message.content[9:])
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quizans ' + message.content[9:] + '\n```')
		if quiz_number == -1:
			await client.send_message(quiz_channel, 'А что же произошло? Грац, вы нашли недоработку с нашей стороны, а раз так, то победил челик ниже:')
		set_answer[quiz_numbers] = str(quiz_numbers + 1) + ')' + message.content[9:]
		await client.send_message(quiz_channel, message.content[9:] + ', верно!')
		await client.delete_message(message)

	if message.channel == quiz_channel and quiz:
		print('---------[command]:!quiz answer - ' + message.content)
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quiz answer - ' + message.content + '\n```')
		if quiz_number != -1:
			if message.content.lower() in quiz_answer[quiz_number]:
				if quiz_number != -1:
					quiz_number = -1
					set_answer[quiz_number] = str(quiz_number + 1) + ')' + message.author.id + ' ' + message.author.name
					await client.send_message(quiz_channel, '<@' + message.author.id+ '>'+ ', верно!')

	if await strcmp(message.content, prefix + 'quizstat') == 1 and message.author.id in admin_list:
		print('---------[command]:!quiz stat')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quiz stat\n```')
		ret = '```css'
		for s in set_answer:
			ret = ret + '\n' + s
		ret = ret + '\n```'
		await client.send_message(message.channel, ret)
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'quizquestions') == 1 and message.author.id in admin_list:
		print('---------[command]:!quizquestions')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quizquestions\n```')
		ret = '```css'
		for s in question:
			ret = ret + '\n' + s
		ret = ret + '\n```'
		await client.send_message(message.channel, ret)
		await client.delete_message(message)

	if await strcmp(message.content, prefix + 'quizanswers') == 1 and message.author.id in admin_list:
		print('---------[command]:!quizanswers')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!quizanswers\n```')
		ret = '```css'
		for s in quiz_answer:
			ret = ret + '\n' + s
		ret = ret + '\n```'
		await client.send_message(message.channel, ret)
		await client.delete_message(message)

	if await strcmp(message.content.lower(), 'соня'):
		print('---------[command]:!sonya')
		#await client.send_message(client.get_channel('43569861995842766'), '```css\n[command]:!sonya\n```')
		await client.send_message(message.channel, 'Соня лучшая!!!')
		await client.delete_message(message)


	if message.content.lower() in mat_list:
		print('---------[command]:!sukablyat')
		await client.send_message(message.author, 'Не матерись, пожалуйста)) ')
		await client.delete_message(message)


#------------------------------------------------------------------------------------------------------------------------------
#         Economics
#------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'daily reset') == 1 and message.author.id in admin_list and message.channel.id in admin_channel_list:
		print('---------[command]:!daily reset')
		daily_id = []
		f = open('daily', 'w')
		for s in daily_id:
			f.write(s + "\n")
		f.close()
		await client.send_message(message.channel, 'Ежедневка сброшена.')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'daily'):
		print('---------[command]:!daily')
		if message.author.id in daily_id:
			await client.send_message(message.channel, '<@' + message.author.id+ '>'+ ', вы уже получили печенюхи)')
		else:
			daily_id.append(str(message.author.id))
			f = open('daily', 'w')
			c = 0
			for s in daily_id:
				f.write(s + "\n")
				c = c + 1
			f.close()
			cookie_count = 100
			if message.author.id in names:
				c = 0
				while(names[c] != message.author.id):
					c = c + 1
				cookie[c] = str(int(cookie[c]) + cookie_count)
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
			else:
				names.append(message.author.id)
				cookie.append(str(cookie_count))
			await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', держи ' + str(cookie_count) + ':cookie:!')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if (await strcmp(message.content.lower(), prefix + 'cookie') == 1 or await strcmp(message.content.lower(), prefix + 'me') == 1):
		print('---------[command]:!cookie')
		if message.author.id in names:
			c = 0
			while(names[c] != message.author.id):
				c = c + 1
			await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя ' + cookie[c] + ':cookie:!')
		else:
			await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя нет :cookie: :(')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if message.content.startswith(prefix + 'roll '):
		print('---------[command]:!roll')
		if not message.content[6:].isdigit():
			await client.send_message(message.channel, '```css\nError!!! Введенное значение не является числом\nExample: ' + prefix + 'roll 20\n```')
		elif message.author.id in names:
			c = 0
			while(names[c] != message.author.id):
				c = c + 1
			if (int(message.content[6:]) > int(cookie[c])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя нет столько:cookie: :(')
			else:
				bonus = 0
				if message.author.id in bonus_list:
					bonus = 30
				if (random.randint(0, 100) + bonus) > 50:
				#if (random.random() == 1):
					cookie[c] = str(int(cookie[c]) + int(message.content[6:]))
					f = open('cookie', 'w')
					c = 0
					for s in cookie:
						f.write(names[c] + '\n' + s + "\n")
						c = c + 1
					f.close()
					await client.send_message(message.channel, '<@' + message.author.id+ '>, ты выиграл ' + str(int(message.content[6:])) + ':cookie:')
				else:
					cookie[c] = str(int(cookie[c]) - int(message.content[6:]))
					f = open('cookie', 'w')
					c = 0
					for s in cookie:
						f.write(names[c] + '\n' + s + "\n")
						c = c + 1
					f.close()
					await client.send_message(message.channel, '<@' + message.author.id+ '>, ты проиграл ' + (message.content[6:]) + ':cookie:')
		else:
			await client.send_message(message.channel, '<@' + message.author.id+ '>, у тебя нет :cookie: :(')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'update'):
		print('---------[command]:!update')
		updates()
		await client.send_message(message.channel, 'Обновлено из файлов.')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if message.content.startswith(prefix + 'give '):
		print('---------[command]:!give')
		params = message.content.lower().split(' ')
		if not message.author.id in names:
			await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя нет :cookie: :(')
		elif params[1][2:-1] in names:
			c = 0
			while(names[c] != params[1][2:-1]):
				c = c + 1
			k = 0
			while(names[k] != message.author.id):
				k = k + 1
			if not params[2].isdigit():
				await client.send_message(message.channel, '```css\nError!!! Введенное значение не является числом\nExample: ' + prefix + 'give <someone> 500\n```')
			elif (int(params[2]) > int(cookie[k])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>, у тебя нет столько:cookie: :(')
			else:
				cookie[c] = str(int(cookie[c]) + int(params[2]))
				cookie[k] = str(int(cookie[k]) - int(params[2]))
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
				await client.send_message(message.channel, '<@' + message.author.id+ '>, подарил ' + params[1] + ' ' + params[2] + ':cookie:')
		else:
			await client.send_message(message.channel, 'Нет такого пользователя :(')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if message.content.startswith(prefix + 'get2d '):
		print('---------[command]:!get2d')
		comm = message.content.split(' ')
		if not comm[2].isdigit():
			await client.send_message(message.channel, '```css\nError!!! Введенное значение не является числом\nExample: ' + prefix + 'get2d <@someone> 1000\n```')
		elif not comm[1][2:-1].isdigit() or not comm[1][:2] == '<@' or not comm[1][-1:] == '>':
			await client.send_message(message.channel, '```css\nError!!! Введенное значение не является ссылкой на пользователя\nExample: ' + prefix + 'get2d <@someone> 1000\n```')
		elif comm[1][2:-1] in waifu_list_id:
			c = 0
			while(waifu_list_own[c] != message.author.id):
				c = c + 1
			k = 0
			while(names[k] != message.author.id):
				k = k + 1
			if (int(comm[2]) > int(waifu_list_cost[c])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', недостаточно :cookie: для покупки :(')
			if (int(comm[2]) > int(cookie[k])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя недостаточно:cookie: :(')
			else:
				cookie[k] = str(int(cookie[k]) - int(comm[2]))
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
				waifu_list_own[c] = message.author.id
				waifu_list_cost[c] = comm[2]
				f = open('waifu', 'w')
				c = 0
				for s in waifu_list_cost:
					f.write(waifu_list_own[c] + '\n' + waifu_list_id[c] + '\n' + s + '\n')
					c = c + 1
				f.close()
				await client.send_message(message.channel, message.author.mention + ' выкупил ' + comm[1] + ' за ' + comm[2])
		else:
			k = 0
			while(names[k] != message.author.id):
				k = k + 1
			if (int(comm[2]) > int(cookie[k])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя недостаточно:cookie: :(')
			else:
				cookie[k] = str(int(cookie[k]) - int(comm[2]))
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
				waifu_list_own.append(message.author.id)
				waifu_list_id.append(comm[1])
				waifu_list_cost.append(comm[2])
				f = open('waifu', 'w')
				c = 0
				for s in waifu_list_cost:
					f.write(waifu_list_own[c] + '\n' + waifu_list_id[c] + '\n' + s + '\n')
					c = c + 1
				f.close()
				await client.send_message(message.channel, message.author.mention + ' купил ' + comm[1] + ' за ' + comm[2])
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content, prefix + '2d'):
		print('---------[command]:!2d')
		ret = '\n'
		c = 0
		for s in waifu_list_id:
			ret = ret + s + ' принадлежит <@' + waifu_list_own[c] + '>. Цена - ' + waifu_list_cost[c] + ':cookie:\n'
			c = c + 1
		em = discord.Embed(title='Список вайфу:', description=ret, colour=0xC5934B)
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'rank'):
		print('---------[command]:!rank')
		f = open('cookie', 'r')
		line1 = f.readline()
		line2 = f.readline()
		nam = []
		coo = []
		while line1:
			nam.append(line1[:-1])
			coo.append(line2[:-1])
			line1 = f.readline()
			line2 = f.readline()
		f.close()
		c = 0
		p = 0
		ret = '\n'	
		while c < 10:
			if len(nam) > 0:
				p = await max(coo)
				ret = ret + str(c + 1) + ') <@' + nam[p] + '> - ' + coo[p] + ':cookie:\n'
				nam.pop(p)
				coo.pop(p)
			else:
				break
			c = c + 1
		nam = []
		coo = []
		em = discord.Embed(title='Leaderboards:', description=ret, colour=0xC5934B)
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'event')  and message.author.id in admin_list:
		print('---------[command]:!event')
		is_event = 1
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'reg') and is_event and message.server.id == '243749885294280704':
		print('---------[command]:!reg')
		role = discord.utils.get(message.server.roles, name='Участвует в ивенте')
		await client.add_roles(message.author, role)
		await client.send_message(message.channel, '<@' + message.author.id + '>, зарегистрирован.')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'unreg')  and message.author.id in admin_list:
		print('---------[command]:!unreg')
		is_event = 0
		role = discord.utils.get(message.server.roles, name='Участвует в ивенте')
		for s in message.server.members:
			if role in s.roles:
				await client.remove_roles(s, role)
		await client.send_message(message.channel, 'Роли изъяты.')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'embed')  and message.author.id in admin_list:
		em = discord.Embed(title='Крутим пальчиками.', colour=0xC5934B)
		em.set_image(url='http://i0.kym-cdn.com/photos/images/original/000/448/492/bfa.gif')
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content.lower(), prefix + 'rules')  and message.author.id in admin_list:
		f = open('rules','r')
		ret = 0
		line = f.readline()
		ret = line
		while line:
			line = f.readline()
			ret = ret + line
		f.close()
		em = discord.Embed(description=ret, colour=0xC5934B)
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if (message.content.startswith('кусь ') or message.content.startswith('Кусь '))  and message.author.id == '344359878153994241':
		em = discord.Embed(description=message.author.name + ' делает кусь ' + message.content[5:], colour=0xC5934B)	
		em.set_image(url=random.choice(kusi_list))
		await client.send_message(message.channel, embed=em)
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if message.content.startswith(prefix + 'stroke '):
		print('---------[command]:!stroke')
		if message.author.id in names:
			c = 0
			while(names[c] != message.author.id):
				c = c + 1
			if (20 > int(cookie[c])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя недостаточно:cookie: :(')
			else:
				em = discord.Embed(description=message.author.name + ' гладит ' + message.content[8:], colour=0xC5934B)
				em.set_image(url=random.choice(stroke_list))
				await client.send_message(message.channel, embed=em)
				cookie[c] = str(int(cookie[c]) - 20)
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
		else:
			await client.send_message(message.channel, '<@' + message.author.id+ '>, у тебя нет :cookie: :(')
		await client.delete_message(message)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
	if await strcmp(message.content, prefix + 'fs'):
		print('---------[command]:!fs')
		if message.author.id in names:
			c = 0
			while(names[c] != message.author.id):
				c = c + 1
			if (15 > int(cookie[c])):
				await client.send_message(message.channel, '<@' + message.author.id+ '>'+ '' + ', у тебя недостаточно:cookie: :(')
			else:
				em = discord.Embed(description=message.author.name + ' крутит пальчиками!', colour=0xC5934B)
				em.set_image(url=random.choice(fs_list))
				await client.send_message(message.channel, embed=em)
				cookie[c] = str(int(cookie[c]) - 15)
				f = open('cookie', 'w')
				c = 0
				for s in cookie:
					f.write(names[c] + '\n' + s + "\n")
					c = c + 1
				f.close()
		else:
			await client.send_message(message.channel, '<@' + message.author.id+ '>, у тебя нет :cookie: :(')
		await client.delete_message(message)



#if message.content.lower() in mat_list:
#        print('Удаляю мат!')
#        await client.send_message(message.channel, 'Извени но я вырезала твой мат \nhttps://iichan.hk/a/arch/src/1331445120492.gif%27')
#        msg = await client.send_message(message.author, 'Не матерись, пожалуста)) ')
#        await client.edit_message(msg,'Извени но я вырезала твой мат')


async def updates():
	channel_list = []
	f = open('channel_list', 'r')
	line1 = f.readline()
	line2 = f.readline()
	c = 0
	while line1:
		channel_list.append(line1)
		channel_list.append(line2)
		line1 = f.readline()
		line2 = str(f.readline())
		print(str((c // 2) + 1) + ')' + channel_list[c][:-1] + ' ' + channel_list[c + 1][:-1])
		c = c + 2
	f.close()

	print('------')

	f = open('daily', 'r')
	line1 = f.readline()
	c = 0
	while line1:
		daily_id.append(line1[:-1])
		line1 = f.readline()
		print(str(c + 1) + ')' + daily_id[c])
		c = c + 1
	f.close()

	f = open('cookie', 'r')
	line1 = f.readline()
	line2 = f.readline()
	while line1:
		names.append(line1[:-1])
		cookie.append(line2[:-1])
		line1 = f.readline()
		line2 = f.readline()
	f.close()

	f = open('mat', 'r')
	line1 = f.readline()
	while line1:
		mat_list.append(line1[:-1])
		line1 = f.readline()
	print('mat_list is ready.')
	f.close()

	f = open('waifu', 'r')
	line1 = f.readline()
	line2 = f.readline()
	line3 = f.readline()
	c = 0
	while line1:
		waifu_list_own.append(line1[:-1])
		waifu_list_id.append(line2[:-1])
		waifu_list_cost.append(line3[:-1])
		line1 = f.readline()
		line2 = f.readline()
		line3 = f.readline()
		c = c + 3
	f.close()

async def max(list):
    maximum = 0
    p = 0
    for s in range(len(list)):
        if int(list[s]) > maximum:
            maximum = int(list[s])
            p = s
    return p


async def strcmp(s1, s2):
	i1 = 0
	i2 = 0
	s1 = s1 + '\0'
	s2 = s2 + '\0'
	while ((s1[i1] != '\0') & (s2[i2] != '\0')):
		if(s1[i1] != s2[i2]):
			return 0
		i1 = i1 + 1
		i2 = i2 + 1
	if(s1[i1] != s2[i2]):
		return 0
	else:
		return 1


def get_btc_price():
	r = requests.get(BTC_PRICE_URL_coinmarketcap)
	response_json = r.json()
	usd_price = response_json[0]['price_usd']
	rub_rpice = response_json[0]['price_rub']
	return usd_price, rub_rpice

client.run(DISCORD_BOT_TOKEN)