import coloredlogs
import logging as log

class Logging:
    def __init__(self):
        coloredlogs.install()
        self.log = log
        self.log.getLogger().setLevel(log.INFO)

    def info(self, message):
        self.log.info(message)
    
    def warn(self, message):
        self.log.warn(message)

    def error(self, message):
        self.log.error(message)

    def set_level(self, level):
        self.log.getLogger().setLevel(level)