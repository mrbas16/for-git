from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

my_driver = webdriver.Chrome(service=Service("E:/Downloads/tip_calc/chromedriver.exe"))
my_driver.get("E:/Downloads/tip_calc/index.html")
my_driver.find_element(By.ID, 'billamt').send_keys("100")
my_driver.find_element(By.XPATH, '//*[@id="serviceQual"]').send_keys(3)
my_driver.find_element(By.ID, 'peopleamt').send_keys(4)
my_driver.find_element(By.ID, 'calculate').click()

result = my_driver.find_element(By.ID, 'tip').text
print(f' The resolt was: [{result}]')


# if result == "7.50":
#     print('That is OK')
# else:
#     print('There is a BUG!!')

# assert result == "7.40"

input()

# //*[@id="billamt"]
# /html/body/div/div[1]/form/p[2]/input
#//*[@id="serviceQual"]
#//*[@id="serviceQual"]/option[3]
# //*[@id="peopleamt"]`