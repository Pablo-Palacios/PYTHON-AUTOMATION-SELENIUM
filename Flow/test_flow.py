from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
from Flow.FlowLogin import conexion_exitosa
import requests

def test_can_conexion():

      htpp = conexion_exitosa()
      assert htpp.status_code == 200



def test_Inicio():
      
      ruta = r"c:\Program Files (x86)\chromedriver.exe"
      os.environ["webdriver.chrome.driver"] = ruta

      driver = webdriver.Chrome()
      driver.get("https://web.app.flow.com.ar")

      button = driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div/div/main/div/button[1]")
      button.click()
      time.sleep(5)




def test_can_login_good():

# conector al webdrive

      ruta = r"c:\Program Files (x86)\chromedriver.exe"
      os.environ["webdriver.chrome.driver"] = ruta

      driver = webdriver.Chrome()
      driver.get("https://web.app.flow.com.ar/perfiles")


      usuario = "chelopalacios@hotmail."
      contraseña = "******"

# se ingresan los datos del usuario 

      username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='username']" )))
      password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
      username.clear()
      password.clear()
      username.send_keys(usuario)
      password.send_keys(contraseña)
      
# selecciona el boton ingresar 

      ingresar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='enterButton']")))
      ingresar.click()

# selecciona el avatar del usuario 


      avatar_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='testAvatar']")))
      avatar_button.click()


      time.sleep(10)
      driver.close()


################################################################################

def conexion_exitosa():

      http = "https://web.app.flow.com.ar"
      return requests.get(http)
