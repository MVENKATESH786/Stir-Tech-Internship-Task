from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pymongo
from pymongo import MongoClient
import uuid
import requests

# ProxyMesh settings
proxymesh_username = 'vicky_i06'
proxymesh_password = 'Venky@06$'     
proxymesh_proxy = '45.32.86.6:31280' # e.g., '123.45.67.89:8080' 


# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['stir_internship']
collection = db['trending_topics']


def get_proxy():
    # Configure ProxyMesh proxy
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxymesh_proxy,
        'ftpProxy': proxymesh_proxy,
        'sslProxy': proxymesh_proxy,
        'noProxy': '',
        'autodetect': False
    })
    return proxy


def scrape_trends():
    # Set up Chrome options with Proxy
    chrome_options = Options()
    proxy = get_proxy()
    chrome_options.proxy = proxy

    # Set up WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://twitter.com/login')

    # Twitter login (replace with actual credentials)
    username = 'Vicky_i007'
    password = 'Vicky@06$'

    # Enter username
    username_field = driver.find_element(By.XPATH, '//input[@name="text"]')
    username_field.send_keys(username)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()

    # Enter password
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys(password)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()

    # Wait for homepage to load
    driver.implicitly_wait(10)

    # Navigate to homepage and find trends
    driver.get('https://twitter.com/home')
    trends_section = driver.find_element(
        By.XPATH, '//section[@data-testid="Trending"]')
    trends = trends_section.find_elements(
        By.XPATH, './/div[@data-testid="trend"]/div/div/a/div/div/span')

    top_5_trends = [trend.text for trend in trends[:5]]

    # Get the IP address used
    ip_response = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_response.json()['ip']

    # Generate unique ID
    unique_id = str(uuid.uuid4())

    # Current date and time
    from datetime import datetime
    datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Data to store
    data = {
        'unique_id': unique_id,
        'name_of_trend1': top_5_trends[0],
        'name_of_trend2': top_5_trends[1],
        'name_of_trend3': top_5_trends[2],
        'name_of_trend4': top_5_trends[3],
        'name_of_trend5': top_5_trends[4],
        'date_time': datetime_str,
        'ip_address': ip_address
    }

    # Insert data into MongoDB
    collection.insert_one(data)

    driver.quit()
    return data
