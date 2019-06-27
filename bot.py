import discord
import string

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
		
		# split the message into it's words
		words = message.content.split()
		if len(words) < 1:
			return
		
		# if you need to scrape the channel:
		if words[0] == '!scrape':
			# select the channel that you want to scrape
			channel = message.channel
			if len(words) > 1:
				channel = channel.guild.get_channel(int(words[1][2: len(words[1])-1]))
			includeMessage = True
			scrapeOutput = ""
			async for msg in channel.history(limit = 10000):
				includeMessage = True
				if msg.content[:1] in string.punctuation:
					includeMessage = False
				if msg.content.strip() == '':
					includeMessage = False
				if includeMessage:
					scrapeOutput = msg.author.name + ": " + msg.content + "\n" + scrapeOutput
			open("scrape.txt","w+", encoding="utf-8").write(scrapeOutput)
			print("done!")

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)