from Handler import Logger

class DebugHandler(Logger):
    def write(self,message):
        print(f"you are getting debug {message}")