from src.request_logger import RequestLogger
from seleniumwire import webdriver
from typing import TypedDict


class RequestLoggerInput(TypedDict):
    callback: callable


class RequestCapturer:
    def __init__(self, logger: RequestLogger):
        self.__driver = webdriver.Firefox()
        self.__logger = logger

    def execute(self, input: RequestLoggerInput) -> None:
        input['callback'](self.__driver)

        for request in self.__driver.requests:
            if 'firefox' not in request.url and request.response:
                self.__logger.execute({
                    'request': {
                        'url': request.url,
                        'method': request.method,
                        'headers': request.headers,
                        'params': request.params,
                        'body': request.body,
                    },
                    'response': {
                        'status_code': request.response.status_code,
                        'headers': request.response.headers,
                        'body': request.response.body,
                    }
                })

        self.__driver.close()
