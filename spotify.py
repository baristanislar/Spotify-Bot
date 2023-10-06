from re import split
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import requests
import webbrowser
import random
import pytz
import time
import os
import keyboard
from colorama import Fore
from pystyle import Center, Colors, Colorate
import time
                            
def main():
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
   
  ▄█   ▄█▄  ▄█   ▄██████▄     ▄███████▄     ███        ▄████████  ▄█  ▀████    ▐████▀ 
  ███ ▄███▀ ███  ███    ███   ███    ███ ▀█████████▄   ███    ███ ███    ███▌   ████▀  
  ███▐██▀   ███▌ ███    ███   ███    ███    ▀███▀▀██   ███    ███ ███▌    ███  ▐███    
 ▄█████▀    ███▌ ███    ███   ███    ███     ███   ▀  ▄███▄▄▄▄██▀ ███▌    ▀███▄███▀    
▀▀█████▄    ███▌ ███    ███ ▀█████████▀      ███     ▀▀███▀▀▀▀▀   ███▌    ████▀██▄     
  ███▐██▄   ███  ███    ███   ███            ███     ▀███████████ ███    ▐███  ▀███    
  ███ ▀███▄ ███  ███    ███   ███            ███       ███    ███ ███   ▄███     ███▄  
  ███   ▀█▀ █▀    ▀██████▀   ▄████▀         ▄████▀     ███    ███ █▀   ████       ███▄ 
  ▀                                                    ███    ███                      
                      
   ▄████████    ▄███████▄  ▄██████▄      ███      ▄█     ▄████████ ▄██   ▄        ▀█████████▄   ▄██████▄      ███     
  ███    ███   ███    ███ ███    ███ ▀█████████▄ ███    ███    ███ ███   ██▄        ███    ███ ███    ███ ▀█████████▄ 
  ███    █▀    ███    ███ ███    ███    ▀███▀▀██ ███▌   ███    █▀  ███▄▄▄███        ███    ███ ███    ███    ▀███▀▀██ 
  ███          ███    ███ ███    ███     ███   ▀ ███▌  ▄███▄▄▄     ▀▀▀▀▀▀███       ▄███▄▄▄██▀  ███    ███     ███   ▀ 
▀███████████ ▀█████████▀  ███    ███     ███     ███▌ ▀▀███▀▀▀     ▄██   ███      ▀▀███▀▀▀██▄  ███    ███     ███     
         ███   ███        ███    ███     ███     ███    ███        ███   ███        ███    ██▄ ███    ███     ███     
   ▄█    ███   ███        ███    ███     ███     ███    ███        ███   ███        ███    ███ ███    ███     ███     
 ▄████████▀   ▄████▀       ▀██████▀     ▄████▀   █▀     ███         ▀█████▀       ▄█████████▀   ▀██████▀     ▄████▀                                                                                                                                                                       
 """)))

    print("")
    print(Colors.red, Center.XCenter("ONLY FOR EDUCATİONAL PURPOSES"))
    print("")

    user_agents = [
    # Chrome (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Chrome (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Firefox (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Firefox (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Safari (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",

    # Opera (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61"
    ]
    
    supported_languages = [
    "en-US", "en-GB", "en-CA", "en-AU", "en-NZ", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-LU",
    "de-DE", "de-AT", "de-CH", "de-LU", "es-ES", "es-MX", "es-AR", "es-CL", "es-CO", "es-PE",
    "it-IT", "it-CH", "ja-JP", "ko-KR", "pt-BR", "pt-PT", "ru-RU", "tr-TR", "nl-NL", "nl-BE",
    "sv-SE", "da-DK", "no-NO"
    ]

    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    random_user_agent = random.choice(user_agents)
    
    with open('acc.txt', 'r') as file:
        acc = file.readlines()

        spotify_song = input(Colorate.Vertical(Colors.green_to_blue, "Enter the Spotify song URL (e.g https://open.spotify.com/track/6L2dWnompVTiSWajrBobMT?si=1357b44115ac4af0):"))

    drivers = []

    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)

                        
    for account in acc:      
                                          
            random_language = random.choice(supported_languages)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
            chrome_options.add_argument('--disable-logging')
            chrome_options.add_argument('--log-level=3')
            chrome_options.add_argument('--disable-infobars')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument("--window-size=1366,768")
            chrome_options.add_argument("--lang=en-US,en;q=0.9")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument(f"--user-agent={random_user_agent}")
            chrome_options.add_argument(f"--lang={random_language}")
            chrome_options.add_argument("--mute-audio")
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_experimental_option('prefs', {
                'profile.default_content_setting_values.notifications': 2
            })

            driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

            username, password = account.strip().split(':')
                    
            try:           
                driver.get("https://www.spotify.com/us/login/")
                username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
                password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")

                username_input.send_keys(username)
                password_input.send_keys(password)

                driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()
                                        
                time.sleep(delay)
                                        
                driver.get(spotify_song)

                driver.maximize_window()

                keyboard.press_and_release('esc')        

                time.sleep(10)

                try:
                    cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
                    cookie.click()
                except NoSuchElementException:
                        try:
                                button = driver.find_element(By.XPATH, "//button[contains(@class,'onetrust-close-btn-handler onetrust-close-btn-ui')]")
                                button.click()
                        except NoSuchElementException:
                                    time.sleep(delay2)
                                    
                playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
                playmusic = driver.find_element(By.XPATH, playmusic_xpath)
                playmusic.click()
                                        
                time.sleep(1)

                volumedown_xpath = "(//*[@id='main']/div/div[2]/div[3]/footer/div/div[3]/div/div[3]/button)" 
                volumedown = driver.find_element(By.XPATH, volumedown_xpath)
                volumedown.click()

                time.sleep(1)
                print(Colors.green, "Username: {} - Listening process has started.".format(username))

            except Exception as e:
                        print(Colors.red, "An error occurred in the bot system:", str(e))

    
    print(Colors.blue, "Stream operations are completed. You can stop all transactions by closing the program.")

    while True:
        pass

if __name__ == "__main__":
    main()
