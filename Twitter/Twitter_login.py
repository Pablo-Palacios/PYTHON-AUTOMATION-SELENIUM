from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time

def test_login():
    ruta = r"c:\Program Files (x86)\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = ruta

    name = "maxitoto2020"
    contraseña = "********"

    # Abrir pagina 
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/i/flow/login")

    # Iniciar sesion 
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='text']")))
    username.clear()
    username.send_keys(name)
    siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']"))).click()






    time.sleep(10)
