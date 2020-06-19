from discord.ext import commands
import discord, tokens, markovify

async def markovChannel(message):
    async with message.channel.typing():
        fullstr = ""
        async for post in message.channel.history(limit=None):
            fullstr += post.content + ". "
            print(post.content)
        model = markovify.Text(fullstr)
        markovStrings = ""
        for i in range(3):
            markovStrings += str(model.make_sentence()) + " "
    await message.channel.send(markovStrings)



Client = discord.Client()
client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

@client.event
async def on_message(message):
    if message.content.lower().startswith('$simulate'):
        print("Beginning Markovify")
        command = message.content.split(" ")
        await markovChannel(message)

client.run(tokens.discord)

