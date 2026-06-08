from Handler import Logger

class ErrorHandler(Logger):
    def write(self,message):
        print(f"you are getting error {message}")

