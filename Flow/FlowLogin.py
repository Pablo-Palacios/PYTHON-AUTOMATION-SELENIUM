from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import requests


def conexion_exitosa():
        
        
        http = "https://web.app.flow.com.ar/perfiles"

        return requests.get(http)









