from selenium import webdriver
import random
import time as t
from datetime import datetime
from colorama import Fore,init
import pyfiglet
import base64
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.mixer.init()
init(autoreset=True,convert=True)
sound=pygame.mixer.Sound('er.wav')
copyright=base64.b64decode('YXppeg==').decode('utf-8')
result = pyfiglet.figlet_format(copyright, font = "slant" )
print(result.center(50))

print('do not close browser window when it opens up\nit will be automatically minimized after finishing\nif you do the session will end and the program will quit')
initialize=base64.b64decode('aW5pdGlhbGl6aW5nLi4u').decode('utf-8')
sesion=base64.b64decode('c2Vzc2lvbiBzdGFydGVk').decode('utf-8')
work=base64.b64decode('d29ya2luZy4uLi4=').decode('utf-8')
print(Fore.RED+sesion)
t.sleep(2)
print(Fore.RED+initialize)
for i in range(5):
    print('.')
    t.sleep(1)
print(Fore.GREEN+work)


while True:


    time=datetime.now()
    now =time.strftime("%H:%M:%S")
    if (now=="11:00:20" or now=="14:20:03" ) :
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()
        PATH = "chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        url = "https://docs.google.com/forms/d/e/1FAIpQLSe61r6TNx4JvRg2gVu3Eu8-KYKCvd1dJCAmYJFnNw4EU9llMw/viewform"
        driver.get(url)
        def sleep():
            t.sleep(10)



        i=0
        while i<4:
            i+=1

            driver.refresh()

            driver.implicitly_wait(5)
            element = ".quantumWizMenuPaperselectOption.appsMaterialWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isSelected.isPlaceholder"

            dropdown = driver.find_element_by_css_selector(element)
            dropdown.click()

            name = "DHAOUI MED AZIZ" #your name here
            list_element = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[text()='"+name+"']"

            dropdown_element = driver.find_element_by_xpath(list_element)
            dropdown_element.click()

        t.sleep(2)

        choices=['//*[@id="i18"]/div[3]','//*[@id="i21"]/div[3]']
        choice=random.choice(choices)
        with open('log.txt','a') as file:
            if choice==choices[0]:
                file.write(f'survey done at {now} choosed 4\n')
            else:
                file.write(f'survey done at {now} choosed 5\n')

        j=0
        while j<3:
            j+=1
            try:


                cli=driver.find_element_by_xpath(choice)
                cli.click()
                confrim= driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div > div > div')
                confrim.click()

            except Exception as e:
                break

        t.sleep(1)
        driver.minimize_window()
