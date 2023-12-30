import discord
import nest_asyncio

nest_asyncio.apply()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(1107305947921125452)  # Replace with the actual channel ID
    print(channel)
    if channel is not None:
        await channel.send('Hello, Discord!')
    else:
        print("Channel not found. Check if the bot has access to the channel.")
    await client.close()


client.run('MTE4OTk1OTc5MDg1MjU3MTIxNw.GnhxkJ.tn1GY86zR8C-nwD13jTitOU8o4RN3_yFeXB1zo')  # Replace 'YOUR_BOT_TOKEN' with your bot's token
