from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import re
from bs4 import BeautifulSoup
import os
import time
options = Options()
#options.add_argument( "--headless" )
# options.add_argument( "--screenshot test.jpg http://google.com/" )
#options.add_argument("--width=600")
#options.add_argument("--height=800")


with open('keywords.txt') as file:
    keywords = [line.rstrip('\n') for line in file]
with open('processedKeywords.txt') as processedfile:
    processedkeywords = [line.rstrip('\n') for line in processedfile]
print(processedkeywords)
unscrapedKeywords = list(set(keywords)-set(processedkeywords))
print(unscrapedKeywords)
driver = webdriver.Firefox( firefox_options=options )
#time.sleep(10)
for keyword in unscrapedKeywords:
    url = 'https://www.google.com/search?client=firefox-b-d&q='+ re.sub("[ ]", "+", keyword)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    pages = soup.findAll('a', id=re.compile("^vplap\d+"))
        #findAll("div", {"class": "mnr-c pla-unit"})
    print(pages)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'keywords', re.sub("[ ]", "-", keyword))
    if not os.path.exists(path):
        os.makedirs(path)

    driver.save_screenshot(path + '.png')
    for idx,page in enumerate(pages):
        if idx == 5:
            break
        #print(page)
        driver.get(page['href'])

        location = os.path.join(path, page['href'].split('//')[-1].split('/')[0] + str(idx) +'.png')
     #   location = '"\"' + + '"\"' + page['href'].split('//')[-1].split('/')[0] + str(idx) +'.png'
      #  location1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', 'screenie.png'))
        print(location)
        time.sleep(1.7)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.4)
        driver.save_screenshot(location)
    print (driver.title)
    print (driver.current_url)
    with open('processedKeywords.txt', "a") as processedfile:
        processedfile.write(keyword + '\n')
driver.quit()
sys.exit()