from Subject import Subject
from TvObserver import TVObserver
from MobileObserver import MobileObserver
class main:

   if __name__ == "__main__": 
    sub = Subject()
    tv = TVObserver()
    mob = MobileObserver()
    sub.addObserver(tv)
    sub.addObserver(mob)


    sub.set_temp(45)

