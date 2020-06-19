from discord.ext import commands
import discord, tokens, markovify

async def markovChannel(message):
    async with message.channel.typing():
        fullstr = ""
        x = 0
        async for post in message.channel.history(limit=None):
            postText = post.content
            if not postText.endswith(".") and not postText.endswith("!") and not postText.endswith("?"):
                postText += ". "
            fullstr += postText
            x+=1
        print("Markoving from", x, "entries.")
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

