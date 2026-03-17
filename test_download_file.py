import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False,
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

def test_text_in_downloaded_file():

    # browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.open("https://practice.expandtesting.com/download")
    # browser.element("[data-testid='download-raw-button']").click()
    download_url = browser.element("[data-testid='1773699745156_DNDAgentFile.txt']").get(query.attribute("href"))

    content = requests.get(url=download_url).content
    with open("tmp/sample2.txt", "wb") as file:
        file.write(content)

    with open("tmp/sample2.txt", "r") as file:
        a = file.read()
        assert "test" in a

    time.sleep(5)