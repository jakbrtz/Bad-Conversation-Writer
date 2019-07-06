# Bad-Conversation-Writer
Mimics a discord text channel

## Setup
You will need these libraries:

`pip install discord`

`pip install gpt-2-simple`

`pip install tensorflow`

## Commands
 `!scrape #channel` This copies all the text from a channel. Specify the channel you want to scrape by using a # so it becomes a hyperlink.
 
 `!train steps` Trains the model. This will take a long time. By default, steps is set to 100.
 
 `!generate` Generate text based on the data in the channel.

## Remarks
I wanted to submit this to [Discord's Hack Week](https://blog.discordapp.com/discord-community-hack-week-build-and-create-alongside-us-6b2a7b7bba33), but I decided against it because it takes too long to run.

It might be faster if you use the tensorflow that uses your GPU. I don't actually understand what's going on.