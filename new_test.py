from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
import asyncio
import nest_asyncio
from database_util import *

# Initialize the database (assuming create_db, insert_number, number_exists are defined)
db_name = 'dnews.db'

create_db(db_name)

# Discord Bot setup
nest_asyncio.apply()
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)

# Function to send a message via Discord
async def send_discord_message(message):
    await client.wait_until_ready()  # Wait until the client is ready
    channel = client.get_channel(1107305947921125452)  # Replace with your channel ID
    if channel:
        await channel.send(message)
    else:
        print("Channel not found or bot does not have access.")

# Selenium part to extract numbers
async def extract_numbers():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get("https://www.dnews.co.kr/uhtml/view.jsp?idxno=202312281142039440785")

    # Execute the JavaScript function
    driver.execute_script("gojournalF('박연오','koss9911')")

    try : 
        while True : 
            elements = driver.find_elements(By.CLASS_NAME, 'lineUse')
            for element in elements:
                a_tags = element.find_elements(By.TAG_NAME, 'a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    number_part = href.split('idxno=')[1]
                    if not number_exists(number_part,db_name):
                        insert_number(number_part,db_name)
                        await send_discord_message(f'{href}')
            
            await asyncio.sleep(5)
            driver.refresh()

    except KeyboardInterrupt : 
        driver.quit()

# Run the Discord bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await extract_numbers()  # Run the Selenium script after logging in
    await client.close()

client.run('MTE4OTk1OTc5MDg1MjU3MTIxNw.GnhxkJ.tn1GY86zR8C-nwD13jTitOU8o4RN3_yFeXB1zo')  # Replace 'YOUR_BOT_TOKEN' with your bot's token
