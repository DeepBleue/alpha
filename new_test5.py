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
import time



db_name = 'dnews.db'
create_db(db_name)


def ring():
    # winsound.Beep(1000, 100)
    playsound('./sound/voice.mp3')
    
    

driver = webdriver.Chrome()


driver.get("https://www.dnews.co.kr")

driver.switch_to.frame('startmain')

driver.execute_script("document.querySelector('.btn_search').click();")
driver.execute_script("document.getElementById('query').value = '특징주';")
driver.execute_script("document.querySelector('.searching').click();")




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
                    ring()

        # id_to_delete = get_id_to_delete(db_name)  # Function to determine which ID to delete
        # if id_to_delete is not None:
        #     delete_id(db_name, id_to_delete)
        time.sleep(1)
        driver.execute_script("document.querySelector('a img[alt=\"검색\"]').parentNode.click();")
        time.sleep(1)

        # driver.refresh()

except KeyboardInterrupt : 
    driver.quit()