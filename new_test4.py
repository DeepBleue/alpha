from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
import asyncio
import nest_asyncio
from database_util import *
import winsound
from playsound import playsound

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Initialize the database (assuming create_db, insert_number, number_exists are defined)
db_name = 'dnews.db'

create_db(db_name)

# Discord Bot setup
nest_asyncio.apply()
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)


async def ring():
    # winsound.Beep(1000, 100)
    playsound('./sound/voice.mp3')
    
    
    
# Selenium part to extract numbers
async def extract_numbers():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get("https://www.dnews.co.kr")

    js_code = "document.querySelector('.search_box').classList.add('open');"
    driver.execute_script(js_code)

    WebDriverWait(driver, 3)
    
    
    # try:
    #     # Wait for the element to be available
    #     input_element = WebDriverWait(driver, 3).until(
    #         EC.presence_of_element_located((By.ID, "query"))
    #     )
    #     input_element.send_keys("특징주")

    #     search_button = driver.find_element(By.CLASS_NAME, "searching")
    #     search_button.click()
    # except Exception as e:
    #     print(e)
    # finally:
    #     driver.quit()
    # # button.click()
    # try : 
    #     while True : 
    #         elements = driver.find_elements(By.CLASS_NAME, 'lineUse')
    #         for element in elements:
    #             a_tags = element.find_elements(By.TAG_NAME, 'a')
    #             for a_tag in a_tags:
    #                 href = a_tag.get_attribute('href')
    #                 number_part = href.split('idxno=')[1]
    #                 if not number_exists(number_part,db_name):
    #                     insert_number(number_part,db_name)
    #                     await ring()
            
            
    #         # id_to_delete = get_id_to_delete(db_name)  # Function to determine which ID to delete
    #         # if id_to_delete is not None:
    #         #     delete_id(db_name, id_to_delete)
    #         await asyncio.sleep(5)
    #         driver.refresh()

    # except KeyboardInterrupt : 
    #     driver.quit()




# Run the Discord bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await extract_numbers()  # Run the Selenium script after logging in
    await client.close()


client.run('MTE4OTk1OTc5MDg1MjU3MTIxNw.GnhxkJ.tn1GY86zR8C-nwD13jTitOU8o4RN3_yFeXB1zo')  # Replace 'YOUR_BOT_TOKEN' with your bot's token
