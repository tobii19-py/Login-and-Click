from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def store(temperature):
  now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
  # assign current datetime to filename
  filename = f"{now}.txt"
  with open(filename, "a") as file:
    file.write(str(temperature) + "\n")
  return filename
  
def main():
  while True:
    driver = get_driver()
  
    # Find and fill in username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
  
    # Click home button and wait 2 seconds
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
  
    # Select temperature element
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    temperature = clean_text(element.text)
    print(temperature)

    store(temperature)
  
  time.sleep(2)

main()