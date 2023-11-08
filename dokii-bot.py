#Dokii-Bot v1 2023 by Duki

#SUBPROGRAMS
import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

intents.messages = True
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected.')

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send("Pong!")

    elif message.content.startswith("!test"):
        await message.channel.send("Test was a success!")

    elif message.content.startswith("!help"):
        await message.channel.send(
            "***Help Commands***\n"
            "!ping - checks if the bot is online.\n"
            "!test - a temporary command for development purposes.\n"
            "!help -a list of all commands and features and how to use them."
        )

    elif message.content.startswith("!announce"):
        if len(message.content.split(" ")) < 3:
            await message.channel.send("You need to specify a title and a message. Correct usage: `!announce Hello Hello everyone!`")
            return

        msg = message.content.split(" ", 2)
        title = msg[1]
        content = msg[2]

        await message.channel.send("**{}**\n{}".format(title, content))


client.run("input token here")
