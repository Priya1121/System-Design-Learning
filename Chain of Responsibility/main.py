from DebugHandler import DebugHandler
from ErrorHandler import ErrorHandler
from InfoHandler import InfoHandler



class main:

    if __name__=='__main__':
        DEBUG = 1
        INFO = 2
        ERROR = 3

        debug = DebugHandler(DEBUG)
        error = ErrorHandler(ERROR)
        info = InfoHandler(INFO)

        debug.setNextLogger(info)
        info.setNextLogger(error)
        error.setNextLogger(None)

        debug.log(INFO,"Debug ho rha he")





