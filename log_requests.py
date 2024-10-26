from src.request_capturer import RequestCapturer
from src.request_logger import RequestLogger
from seleniumwire import webdriver
import time


def callback(driver: webdriver.Firefox) -> None:
    driver.get('https://viamao.govbr.cloud/pronimtb/index.asp?acao=4&item=2')
    driver.find_element(by='xpath', value='//*[@id="confirma"]').click()
    time.sleep(20)


logger = RequestLogger()
requestCapturer = RequestCapturer(logger)
requestCapturer.execute({'callback': callback})
