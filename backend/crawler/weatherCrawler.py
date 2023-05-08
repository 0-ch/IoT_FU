from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = 'C:/Users/0524e/OneDrive/桌面/anaconda/chromedriver'

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=10017')
rain = driver.find_element(By.CLASS_NAME, "rain")
rainText = rain.get_attribute("outerHTML")
rainNum = rainText[-10:-8]
print(rainNum)
fo = open("test.txt", "a")
currentDateAndTime = datetime.now()
seq = [str(currentDateAndTime)+"  :  ", rainNum+"\n"]
fo.writelines( seq )


fo.close()
driver.close

