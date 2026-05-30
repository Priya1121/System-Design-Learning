
from Media.IMedia import IMedia
class GIFMedia(IMedia):

    def addMedia(self, GIF_url):
        return self.baseText.notify()+" "+GIF_url