import discord

# Everything that the bot does is inside this class:
class MyClient(discord.Client):

	# When you're ready, log in
	async def on_ready(self):
		print('Logged on as', self.user)
		
	# When you recieve a message, respond to it
	async def on_message(self, message):
		# if the author of the message was a bot don't respond
		if message.author.bot:
			return
		
		words = message.content.split()
		# only respond if the first word of the message was `!doit`
		if words[0] == '!doit':		
			await message.channel.send("ditto")

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)