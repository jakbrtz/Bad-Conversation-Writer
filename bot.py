import discord
import gpt_2_simple as gpt2
import string

# Start the gpt session
model_name = "117M"
gpt2.download_gpt2(model_name=model_name)
sess = gpt2.start_tf_sess()

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
			scrapeOutput = ""
			await client.change_presence(activity=discord.Game("scrape " + channel.name))
			async for msg in channel.history(limit = 10000):
				if msg.content[:1] in string.punctuation:
					continue
				if msg.content.strip() == '':
					continue
				if "http" in msg.content: 
					continue
				if message.author.bot:
					continue
				scrapeOutput = msg.author.name + ": " + msg.content + "\n" + scrapeOutput
			open("scrape.txt","w+", encoding="utf-8").write(scrapeOutput)
			await message.channel.send("Done! Type `!train` to create a model. This will take a long time.")
			await client.change_presence(activity=None)
			print("done!")
			
		# once you have the data, train the model
		if words[0] == "!train":
			steps=100
			if len(words) > 1:
				steps=int(words[1])
			
			await client.change_presence(activity=discord.Game("with a neural net"))
			
			gpt2.finetune(sess,
				'scrape.txt', 
				model_name=model_name,
				steps=steps)
			
			await client.change_presence(activity=None)
			await message.channel.send("Done! Type `!generate` to get some text")
			print("done!")
			
		# generate new textgen
		if words[0] == "!generate":
			await client.change_presence(activity=discord.Game("Microsoft Word"))
			output = gpt2.generate(sess, return_as_list=True)[0]
			await client.change_presence(activity=None)
			await message.channel.send("```\n" + output[:1990] + "\n```")
			print("done")

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)