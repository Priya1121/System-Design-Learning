from SimpleNotification import SimpleNotification
from Media.ImageMedia import ImageMedia
from Device.MobileDevice import MobileDevice
from Device.Subject import Subject

if __name__ == "__main__":
    msg = SimpleNotification("Hello Priya!!")
    image = ImageMedia(msg)
    res = image.addMedia("order.png")

    mob = MobileDevice()

    service = Subject("Hello Lahari")
    service.addObserver(mob)

    service.set_text(res)

         









