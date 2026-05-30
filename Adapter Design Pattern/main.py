from Middleware import Middleware
from Adapter import Adapter
class main:
    if __name__ == "__main__":
        mid = Middleware()
        adapter = Adapter(mid)

        print(adapter.deliver())


