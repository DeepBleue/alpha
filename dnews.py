# Function to send a message via Discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
import nest_asyncio
from database_util import create_db,insert_number,number_exists
from discord_function import send_discord_message
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio


db_name = 'dnews.db'
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

async def Dnews(client,CHANNEL_ID):
    
    create_db(db_name)
    
    def selenium_task():
    
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open the webpage
        driver.get("https://www.dnews.co.kr/uhtml/view.jsp?idxno=202312281142039440785")

        # Execute the JavaScript function
        driver.execute_script("gojournalF('박연오','koss9911')")
        

        
        try:
            while True:
                
                elements = driver.find_elements(By.CLASS_NAME, 'lineUse')
                for element in elements:
                    a_tags = element.find_elements(By.TAG_NAME, 'a')
                    message = element.text
                    for a_tag in a_tags:
                        href = a_tag.get_attribute('href')
                        number_part = href.split('idxno=')[1]
                        if not number_exists(number_part,db_name):
                            insert_number(number_part,db_name)
                            try:
                                asyncio.run_coroutine_threadsafe(
                                    send_discord_message(message, href, client, CHANNEL_ID),
                                    asyncio.get_event_loop()
                                )
                            except Exception as e:
                                print(f"Error sending message: {e}")
                time.sleep(5)
                driver.refresh()

        except Exception as e:
            print(f"Error in Selenium task: {e}")
            driver.quit()
    
    executor = ThreadPoolExecutor()
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, selenium_task)
    