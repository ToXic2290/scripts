
# Sagarius лох

import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os

app = Client('admin', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')
app.start()
app.stop()
if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

print('''
🐔арова заебал!
Чекай скрипт давай, понравится - красава.
Не понравится - гей.

''')

print("После ввода задержки напишите в любой телеграм чат команду -help для просмотра команд!")
print("\n Если ты чет не то сделаешь то иди нахуй, мне похуй на твои проблемы.")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
print("Напишите в любой чат телеграмма -help (В закрытых чатах команда не работает)")

global number
number = 0

while cool == 0:
	print("Слишком быстро!")
	cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool == 1:
	print("Слишком быстро!")
	cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool == 2:
	print("Слишком быстро!")
	cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool > 10:
	print("Слишком медленно!")
	cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool < 0:
	print("ОЧЕНЬ БЫСТРО........")
	cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))





@app.on_message(filters.command("help", prefixes="-") & filters.me)
def valentine(app, message):
	app.send_message(message.chat.id,f'''
📙<b> Команды:</b> \n<b> -help - вывести список команд</b> \n<b> .like - арт "лайк"</b> \n<b> .dislike - арт дизлайк</b> \n<b>     Текста песен:</b> \n<b> .showdown</b> \n<b> .twitch</b> \n<b> .battle - (гавно, залупа, пенис и тд.)</b> \n<b> .zoo</b> \n<b> .landisi</b> \n<b> .kaif</b> \n<b> .shadowfield</b> \n <b> .astralstep</b>



''', disable_web_page_preview=True)




@app.on_message(filters.command("like", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f'''      
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
		sleep(5)
		global number
		number = number + 1
		msg.edit(f'<b> </b>')

@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f'''
🟥''')  # red
		sleep(0.001)
		msg.edit(f'''
🟥🟥''')  # red
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
		sleep(1)
		msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
		sleep(1)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
		sleep(1)
		msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
		sleep(4)
		global number
		number = number + 1
		msg.edit(f'<b> </b>')



@app.on_message(filters.command("showdown", prefixes=".") & filters.me)
def valentine(app, msg):
	msg.edit(f"<b>Начало через: 13s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 12s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 11s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 10s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 9s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 8s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 7s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 6s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 5s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 4s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 3s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 2s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 1s</b>")  # orange
	sleep(0.2)
	msg.edit(f"<b>Бу, блять! Ха-ха</b>") 
	sleep(1.2)
	msg.edit(f"<b>Просыпайтесь нахуй (Let's go!)</b>")  # orange
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Похоронный марш гулей, на часах последний тик</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Моя тати — Бравл Шелли, я несу ей дробовик</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Ваши головы — мишени, я снесу их в один миг</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Никаких резких движений — ваш хилбар на один хит</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Динамайк трипл килл, ха, нервы на пределе</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Voice в моих ушах — я позабыл все дни недели</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Как на лезвии ножа и шквал патрон, летят шрапнели</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Psychokilla — весь мой шарм, вся эта мапа поредели</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>Эй, погоди, мои парни на Стокгольме</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Мой showdown 1x1, и мои демоны все в форме</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Если я зайду к вам в лобби — оно станет вам могилой</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Если ты зайдешь — мне похуй, я не стартану и выйду, а-ха</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>По приказу Генерала Гавса!</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>— Бро, тут вообще сложная ситуация, все границы позакрывали нахуй. Ваще пиздец полный. Ща просто едем ближе ко Львову, но во Львове тоже пиздец начался, поэтому хуй знает</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>— Бля, чуваки, шутки шутками, но не занимайтесь хуйнёй, я вас умоляю. А-а-а!</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Генерал Гавс, ха, вижу вас без гема</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я отдал приказ, и все умрут от реквиема</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Дота-рэп — топ чарт, ха, наебал систему</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Mute all chat, я на лям скупил все гемы, ха-ха</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, бля</b>
	''')

	sleep(0.5)
	global number
	number = number + 1
	app.send_message(message.chat.id, f'''
	 <b> </b>
	 ''')

@app.on_message(filters.command(["Oxxxymiron", "versus", "battle"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Гавно</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Залупа</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Пенис</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Хер</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Давалка</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Хуй</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Блядина</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Галовка</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Шлюха</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Жопа</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Член</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Еблан</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Петух</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Мудила</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Рукаблуд</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Ссанина</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Очко</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Блядун</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Вагина</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Сука</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Ебланище</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Влагалеще</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Пердун</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Дрочила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пидор</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пизда</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Туз</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Малафья</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Гомик</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Мудила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пилотка</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Манда</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Анус</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Вагина</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Путана</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Педрила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Шалава</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Хуила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Мошонка</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Елда</b>
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	<b>Раунд!</b>
	''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("zoo", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мне собачку тр*хнуть утром мало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Надо утром вечером и днем</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У меня вчера змея сосала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А сегодня я е*усь с ежом!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мама принесла вчера котенка</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>На ночь я его к себе забрал</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу во все дыры отъе*ал!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')

	sleep(5)
	global number
	number = number + 1



@app.on_message(filters.command("landisi", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Толстый х*й под самый нос</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Но меня не проебешь</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Х*й на ландыш не похож</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Х*й — большой</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Мех с п*зды, клочек волос</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Но меня не наебешь</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Клок на ландыш не похож</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Клок — большой</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Мы забрались в камыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Нае*ались от души</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Нах*я нам эти ландыши?</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ты и так, б*ядь, хороша</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ну и что</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Что ландыш маленький?</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Теплого мая привет</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Девушка юноше</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Делает м*нет</b>
	''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command(["NeverEnough", "ne", "zxcursed"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>MUPP broken your heart</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, ха-а, а-а</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Крики necromastery и вопли подо мной</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Руки дезоляторы и shadow nevermore</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз в ебало, твоя сука вся течёт</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Она говорит ей мало, но я продолжу ход</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Твоё сердце так пылает, его превращаю в лёд</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Как Лелуш управляю этой сукой — она орёт</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я бегу ща как Соник, попробуй поймай</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Эта сука не знает, как подойти — отступай</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>На мне ща куча дури (А-а) и это не манта</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Вдавил шб и таунт трайни (А-а), один из ста</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Записал тебя в тетрадку и я не Ягами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Zero reasons to talk, ублюдки, это цунами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я, бля, Тобирама — все бастарды за бортами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я неуязвим, моя клятва — это синигами (Ага)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Fear — это страх, а страх — это я</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Под баффом агилы берсерк mode Киллуа</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Sla-Sla-Slayer убийца, Рефреш обновился</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Реквием в сердце — ты болью проникся</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>За спиной нет крыльев, но я лечу</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Butterfly на руке и я его точу (А)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Emotional emptiness — совсем не грущу</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Why do you even try? Заживо сожру</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я-Я не под спидами, просто под хастой</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Су-Су-Супер Сайян, so slow — это штрафной</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Выпал крит, это не Кристалис</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Моб Психо сто, но мы не сыгрались</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Зеницу Агацума — называй меня скорость</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Меня не остановить, тревела на ноги полная готовность</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>See you later на полу следы от ног остались навсегда</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Позади меня нет жара, only холода</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Не оставлю тебе выбора, творя, бля, чудеса</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Never enough даю те полчаса, убив всех enemy, ну да-да</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, продолжай, ха-а (Yeah, ho)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Демоны в башке, рэйзы на тебе</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Кричишь от боли, приклонись судьбе</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Поток Акаши, ты вставший на колени</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Не посмел бы даже думать о замене</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>У меня нет кагуне, просто я ебанутый</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Feel no pain — и я стал культом</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Тысячи гулей узнают по никнейму</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Чекай телеграм, там весь сквад Антейку</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Если у тя бабочка — я не миссую</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Если у тя мкб — ты вовсе не хитуешь</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>W/W — сияю ярче Иллидана (А-а)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Парень ставит паузу и я достаю катану</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Ха-а, ха-а, а-а**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Залетаю с автоматом, ставлю лазер коллиматор</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Твоя тати — моя тати, со мной едет в Maserati</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Фиолетовая shawty, её тело на кровати</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я снёс им всем ебало — это стиль аннигилятор</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Третий глаз как шинигами, в темноте не вижу свет</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Venom orb в моём пресете, замедляю в интернете</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Вооружён зубами, я их отправлю на тот свет</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Они стреляют в моё тело, мой armor бронежилет (Арата)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Мо-Моя катана самехада — поедает этих тварей</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Холодает в моём теле, бью — я будто Гаара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''') 
	sleep(1)
	app.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEENvNiNs_MoD7fFverk1v5wqoX2Fd-tQACxgoAAiu8OUlTcsBdvR5J0iME")

	sleep(0.5)
	global number
	number = number + 1
	app.send_message(message.chat.id, f'''
	 <b> </b>
	 ''')

@app.on_message(filters.command(["kaif", "konfuz"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты в моих мыслях так плотно засела</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А я не был грубым, так, просто манера</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Все подружки в шоке, Gucci, Panamera</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>От голоса моего ты опьянела</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Где девочка манит, там так сильно дурманит</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждую секунду я звоню, но телеф занят</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кайф ты поймала, тебе всегда мало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты не представляешь, как мне тебя не хватало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сильно бьётся сердце, сама не ожидала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Наконец-то твоя совесть тебя наказала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Девочка в предвкушении азарта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Когда встретил тебя, не нашёл пути обратно</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты — моё сокровище, козырная карта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мы дошли до финиша, не дойдя до старта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Что ты забыла у меня на repeat'е?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В твоих глазах я тону — помогите!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')

	app.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEEPJ1iOeGaHrwudfx0VAkPdzcJV7rSsAACLBYAAqlr0EsgtENNn-yMxyME")

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command("shadowfiend", prefixes=".") & filters.me)
def valentine(app, msg):

	app.send_message(msg.chat.id, f'''
	<b>PLVSTIC, ты такой стильный!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– shadowraze?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Нет, блять, Pavshiy</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Mariyaunban?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Нет, блять, Prepodobniy, ха-ха-ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Shadow-Shadow Fiend, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Парень без обид</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твой ugly face уже разбит</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Слышь, ебучий псих, твой playstyle — это стыд, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я, бля, Shadow Fiend, ты — ебучий психокид, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, блядь, кто такой, а? Сука, чё не нравится?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз в ебло и твоё эго, блядь, расплавится</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твоя блядь на пос-пять — она лает и кусается</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я бля perfect player, меня это не касается, сука</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ах-ха-ха, привет, Каспер, помнишь меня?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Как там твой сыночек, безмозглый дегенерат, Стасик,</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>поживает? Никто его ещё не пришиб, как муху ебаную?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А, броу? Как там твоя мать, шлюха гнилозубая, поживает,</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>тоже, рассказывай</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>До встречи на эпицентре, сын шлюхи</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз на шее</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мне не нужно разрешение, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Убрал тебя с мида, в моём лобби стал мишенью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твой Титаник пал, блядь, или сука, потерпел крушение</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты ебучий dead inside интернетных отношений</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Моё лобби ZXC, но я не жду больше минуты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В деле топовый SF, мои коилы – терракоты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мои коилы — ZXC, мои души — громче всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC — ты отлетаешь от раскаста shadowraze</b>
	''')

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command("astralstep", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Разрубаю глефой ноги, я бегу, за спиной Боги (А-а)</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Как на ринге, только в лобби, ты подох, бля (Ха-ха)</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я стреляю — это step, бро, you low</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я быстрее этих lame'ов, you slow, братан</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я use'аю эти spell'ы — это мой lifesteal</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я sip'ую эти step'ы — это жёсткий стиль</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Долбоёб назвал НН-ом, я его простил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я убил их, даже не завейстил сил</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Погасил этих псин, курю бензин, I'm steal</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Показал им старый стиль, добил их всех, а кто спросил?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Astral step поразил долбоёбов и терпил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У меня сотка гулей, посмотри — ты вновь один</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Вот ты прикинь, челы чё-то там на Дота-рэп гонят, да</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>А я за один квартал лям рублей получил, бля</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Лимон за Дота-рэп, ха-ха-ха-ха</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Hunter on ghoul, я убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Уворот от пуль, у меня есть вес</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Нахуй граммовка, у меня есть весы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не злодей, но у меня свои бесы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Много валюты, имею и песо</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Много энергии, я будто Тесла</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю так метко, все пули прям в висок, а</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')

	sleep(0.5)
	global number
	number = number + 1


@app.on_message(filters.command("twitch", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Я настолько асоциальный, что не мылся пару лет</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>И я днями и ночами залипаю на Твиче</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>Все друзья мне говорили "Найди девушку уже"</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>Но друзей не заводил я, ведь они все в голове</b>
	''')
	sleep(1.6)
	app.send_message(msg.chat.id, f'''
	<b>Меня никто, ни за что, никогда не любил</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Но зачем это всё, когда есть виртуальный мир</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Пусть никто, ни за что, никогда не любил</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Мне и так хорошо, со мною виртуальный мир</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Я Б СЕБЯ ЛЮБИЛ, Я БЫ, Я Б СЕБЯ ЛЮБИЛ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>НО МНЕ НЕ ХВАТАЕТ СИЛ, НО-НО НЕ ХВАТАЕТ СИЛ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>И Я ЗАПУСКАЮ СТИМ, ЗА-ЗА ЗАПУСКАЮ СТИМ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>ОТ РЕАЛЬНОСТИ УЙТИ..</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>Я Б СЕБЯ ЛЮБИЛ, Я БЫ, Я Б СЕБЯ ЛЮБИЛ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>НО МНЕ НЕ ХВАТАЕТ СИЛ, НО-НО НЕ ХВАТАЕТ СИЛ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>И Я ЗАПУСКАЮ СТИМ, ЗА-ЗА ЗАПУСКАЮ СТИМ</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>От реальности уйти...</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Просыпаюсь рано утром, я не умер это сон(</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>Снова сраный кот мяучит, а я думал что он сдох...</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>На день строил столько планов, пришло время все менять</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>Захожу в какой-то паблик, чтоб спросить "Жива ли мать?)" </b>
	''')
	sleep(2.5)
	app.send_message(msg.chat.id, f'''
	<b>Пошли нахуй тянки, у меня есть танки</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>Пошла в пизду работа, у меня есть дота</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>Counter-Strike и Hearthstone, Overwatch и Bloodborne</b>
	''')
	sleep(2.3)
	app.send_message(msg.chat.id, f'''
	<b>Вся FIFA и Battlefield, Lineage 2 и Skyrim </b>
	''')
	sleep(5)
	app.send_message(msg.chat.id, f'''
	<b>Меня никто, ни за что, никогда не любил</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Но зачем это всё, когда есть виртуальный мир </b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Пусть никто, ни за что, никогда не любил</b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>Мне и так хорошо, со мною виртуальный мир </b>
	''')
	sleep(2.1)
	app.send_message(msg.chat.id, f'''
	<b>Я Б СЕБЯ ЛЮБИЛ, Я БЫ, Я Б СЕБЯ ЛЮБИЛ</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>НО МНЕ НЕ ХВАТАЕТ СИЛ, НО-НО НЕ ХВАТАЕТ СИЛ!</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>И Я ЗАПУСКАЮ СТИМ, ЗА-ЗА ЗАПУСКАЮ СТИМ</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>ОТ РЕАЛЬНОСТИ УЙТИ</b>
	''')
	sleep(4)
	app.send_message(msg.chat.id, f'''
	<b>Я Б СЕБЯ ЛЮБИЛ, Я БЫ, Я Б СЕБЯ ЛЮБИЛ! </b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>НО МНЕ НЕ ХВАТАЕТ СИЛ, НО-НО НЕ ХВАТАЕТ СИЛ </b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b>И Я ЗАПУСКАЮ СТИМ, ЗА-ЗА ЗАПУСКАЮ СТИМ </b>
	''')
	sleep(1.8)
	app.send_message(msg.chat.id, f'''
	<b> ОТ РЕАЛЬНОСТИ УЙТИ...</b>
	''')
	sleep(5)
	app.send_message(msg.chat.id, f'''
	<b>😔😔😞</b>
	''')
	
	sleep(0.5)
	global number
	number = number + 1




end_message = '<b>  </b>'
app.run()
