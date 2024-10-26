from src.abstract.response import Response
from src.abstract.request import Request
from typing import TypedDict
import time
import os


class RequestLoggerInput(TypedDict):
    request: Request
    response: Response


class RequestLogger:

    def __init__(self):
        self.__folderPath = 'tmp/logs'
        os.makedirs(self.__folderPath, exist_ok=True)
        self.__clearLogs()

    def execute(self, input: RequestLoggerInput) -> None:
        miliseconds = int(round(time.time() * 1000))
        fileName = f'{miliseconds}.txt'

        with open(f"{self.__folderPath}/{fileName}", 'wb') as file:
            file.write("Request:\n".encode('utf-8'))
            file.write(str(input['request']).encode('utf-8'))
            file.write("\n\nResponse:\n".encode('utf-8'))
            file.write(str(input['response']).encode('utf-8'))

    def __clearLogs(self) -> None:
        for file in os.listdir(self.__folderPath):
            os.remove(os.path.join(self.__folderPath, file))
