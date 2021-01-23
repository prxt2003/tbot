import discord
import os

client = discord.Client()


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f'Hi {member.name}, in this server, I take executive decisions')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='you L'))


@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

    if message.author == client.user:
        return

    # if 'lol no' in message.content.lower():
    #     await message.channel.send('LOL NO')

    # for i in message.content.lower():
    #     LC, NC = 0, 0
    #     if i == 'lol':
    #         LC = LC + 1
    #     if i == 'no':
    #         NC = NC + 1
    #     if LC >= 2 and NC >=2:
    #         await message.channel.send('Shut the fuck up')

    # if 'executive' in message.content.lower() or 'decision' in message.content.lower():
    #     await message.author.create_dm()
    #     await message.author.dm_channel.send(f'{message.author.name} am sorry but this has to stop')
    #     await message.channel.send('Screw you only I take executive decisions')

    # if message.author.name == 'Tarun Shankar':
    #     await message.channel.send('Am sorry but this has to stop tarun')
    # elif message.author.name in ['Stryker101', 'Madhav Lodha']:
    #     await message.channel.send('Stop eating fatass')

    # if message.author.name == 'cerealkiller2527':
    #     await message.delete()
    #     await message.channel.send('<@!445879318388670464> L')

    if 'parts' in message.content.lower():
        await message.channel.send('We need new BALL BEARINGS')


client.run(os.environ['TOKEN'])
