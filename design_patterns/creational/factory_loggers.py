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


class LoggersFactory:
    def __init__(self):
        self.environment = os.environ.get('ENVIRONMENT', 'dev')
        self.logs_file_path = os.environ.get('LOGS_FILE_PATH', None)
        self.__init_logger()

    def get(self) -> Logger:
        return self.logger

    def __init_logger(self):
        if self.environment == 'prod':
            self.logger = FileLogger(self.logs_file_path)
        else:
            self.logger = StdoutLogger()


loggers_factory = LoggersFactory()

print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
logger = loggers_factory.get()
logger.log('It works')
