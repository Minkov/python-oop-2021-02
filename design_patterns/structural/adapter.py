from abc import abstractmethod, ABC
from pyfiglet import figlet_format


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)


class PyfigletLogger(Logger):
    def __init__(self):
        self.logger = StdoutLogger()

    def log(self, obj):
        return self.logger.log(figlet_format(obj))


PyfigletLogger().log('It works!')
