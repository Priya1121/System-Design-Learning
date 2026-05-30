
from Media.IMedia import IMedia
class ImageMedia(IMedia):

    def addMedia(self,image_url):
        return self.baseText.notify()+ " " + image_url