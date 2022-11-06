#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.WARNING,
                    filename='info.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    )

def main(adress):

    try:
        options = webdriver.ChromeOptions()
        # 设置下载目录
        prefs = {"download.default_directory":"/Users/mac/Desktop/test"}
        options.add_experimental_option("prefs", prefs)
        # 不自动关闭浏览器
        options.add_experimental_option("detach", True)
        # # 无界面浏览器
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # # 无痕浏览器 对抗部分反爬手段
        # options.add_argument("--incognito")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get('https://smart-contract-downloader.vercel.app/')
        time.sleep(1)
        search_box = driver.find_element("name","contractAddress")
        search_box.send_keys(adress)
        search_box.submit()
        time.sleep(2)
        download_box = driver.find_element("xpath", '/html/body/div/div/main/div[4]/button')
        download_box.click()
        print(adress + 'successed')
        logging.warning(f'{adress}')
    except Exception:
        print(adress + 'failed')
        logging.error(f'{adress}')

    time.sleep(1.5)
    driver.quit()

if __name__ == '__main__':
    for adress in open("/Users/mac/Desktop/newest_contract_1.txt"):
        main(adress)
