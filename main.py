import requests
from bs4 import BeautifulSoup
import telegram
import time
bot_token = '<6590224590:AAGLU31ZpSN6d72lriZJUJFHaaINr74T6-g>'
bot_chat_id = '<727731187>'
bot = telegram.Bot(token=bot_token)
def send_message_to_telegram_channel():
     url = 'https://www.bbc.com/amharic/topics/cdr56g2x71dt'
response = requests.get(url)
s = BeautifulSoup(response.text, 'html.parser')
target_a_tag = s.find_all("a", class_="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0")
def send_message_to_telegram_channel():
    url = 'https://www.bbc.com/amharic/topics/cdr56g2x71dt'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    
    target_a_tag = s.find_all("a", class_="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0")
    
    if target_a_tag:
        for i in range(2):
            if target_a_tag[2] == i:
                print("No news found")
            else:
                href_value = target_a_tag[i].get("href")
                res = requests.get(href_value)
                sou = BeautifulSoup(res.text, 'html.parser')
                news = sou.find_all(class_='bbc-19j92fr ebmt73l0')
                
                image = sou.find(class_='e3vrtyk0 bbc-rb7xa0 e1mo64ex0')
                image_url = ""
                if image:
                    image_url = image.get("src")
                    url = f"http://t.me/Pogar_bot{bot_token}/sendMessage?chat_id={bot_chat_id}&text={image_url}"
                    response = requests.get(url)
                else:
                    print('Image not found!')
                
                message = ""
                for i in range(len(news)):
                    message += news[i].text + '\n'
                
                url = f"http://t.me/Pogar_bot{bot_token}/sendMessage?chat_id={bot_chat_id}&text={message}"
                response = requests.get(url)
                
                time.sleep(10)  # Add a delay to avoid spamming the channel
            
    else:
        print("Target <a> tag not found.")


send_message_to_telegram_channel()