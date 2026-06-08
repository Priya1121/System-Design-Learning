
from Handler import Logger

class InfoHandler(Logger):
    def write(self, message):
        return print(f"you are getting the info {message}")