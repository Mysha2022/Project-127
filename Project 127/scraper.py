from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        # beautiful soup object
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul" , attrs = {"class" , "exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a"))
                
                else:
                    try:
                        temp_list.append(li_tag)
                    except:
                        temp_list.append("")

        # Find all elements on the page and click to move to the next page
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


        
# Calling Method    
scrape()

# Define Header
headers = ["star_name", "distance", "mass", "radius", "luminosity"]

# Define pandas DataFrame   
df = pd.DataFrame(stars_data, columns = headers)

# Convert to CSV
df.to_csv("stars.csv", index = True, index_lable  = "id")
    


