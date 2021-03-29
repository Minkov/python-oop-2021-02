from abc import ABC, abstractmethod
import os


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, obj):
        with open(self.file_path, 'a') as file:
            file.write(obj)
            file.write('\n')


class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)


class LoggerFactory(ABC):
    @abstractmethod
    def get(self):
        pass


class ProductionLoggersFactory(LoggerFactory):
    def __init__(self, logs_file_path):
        self.logs_file_path = logs_file_path
        self.logger = FileLogger(self.logs_file_path)

    def get(self):
        return self.logger


class DevelopmentLoggersFactory(LoggerFactory):
    def __init__(self):
        self.logger = StdoutLogger()

    def get(self):
        return self.logger


def get_loggers_factory():
    environment = os.environ.get('ENVIRONMENT', 'dev')
    logs_file_path = os.environ.get('LOGS_FILE_PATH', None)
    if environment == 'prod':
        return ProductionLoggersFactory(logs_file_path)
    else:
        return DevelopmentLoggersFactory()
