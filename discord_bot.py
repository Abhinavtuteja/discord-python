import os

import discord
from dotenv import load_dotenv
import requests
import json
import copy

client = discord.Client()
# print(client)
def search_links(keyword):
	links = []
	data = "https://www.googleapis.com/customsearch/v1?key=AIzaSyA0hYMZMC1HiGQm11NK-HxxMORoIlc8c2w&cx=017576662512468239146:omuauf_lfve&q="+keyword+'"'
	ap = requests.get(data)
	ap = ap.json()['items']
	links = [i['link'] for i in ap]
	return links[:5]

def read_data():
	with open('data.json') as json_data:
	    d = json.load(json_data)
	    return d

def write_data(a):
	with open('data.json', 'w', encoding='utf-8') as f:
	    json.dump(a, f, ensure_ascii=False, indent=4)
	    return a


load_dotenv()
token = "NjQ1MTk0OTM5NzQ3MDA4NTEy.XdEnqA.Aae21KoCJ_AhMx_iT7P7YieV368"



@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)


lis = []
@client.event
async def on_message(message):
	if str(message.author) != str('Abhinav_bot#0436'):
		if message.content != '!recent game':
			lis.append(message.content)
			readed = read_data()
			# print("readed",readed)
			# print('1---',lis)
			lis_data = lis.copy()
			# print("after copy",lis_data)
			readed.append(lis_data[-1])
			print("written---",readed)
			write_data(readed)
			# print("3----",readed)

	elif message.author == client.user:
		return

	if message.content == 'hi' or message.content == 'Hi':
		response = "Hi"
		await message.channel.send(response)
	elif message.content == '!recent game':
		# res = lis[-2]+" "+lis[-3]
		data = read_data()
		await message.channel.send(data[-1])
		await message.channel.send(data[-2])

	elif '!google' in message.content:
		keyword = message.content.replace('!google','').strip()
		links = search_links(keyword)
		for i in links:
			await message.channel.send(i)



client.run(token)
print(lis)


