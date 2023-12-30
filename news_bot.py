from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
import asyncio
import nest_asyncio
from database_util import create_db,insert_number,number_exists
from discord_config import CHANNEL_ID,TOKEN
from dnews import Dnews


nest_asyncio.apply()
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)



# Run the Discord bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await Dnews(client,CHANNEL_ID)  # Run the Selenium script after logging in
    await client.close()

client.run(TOKEN)  # Replace 'YOUR_BOT_TOKEN' with your bot's token