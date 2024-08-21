from ninja import Functions

class Ninja:
    class Sync:
        class Add:
            def __init__(self, ar: int = None, k: str = None, co: str = None, hl: str = "en", v: str = None, size: str = "invisible", cb: str = None, url: str = None, proxy=None, user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Avast/126.0.0.0') -> None:
                self.ar = ar
                self.k = k
                self.co = co
                self.hl = hl
                self.v = v
                self.size = size
                self.cb = cb
                self.url = url
                self.proxy = proxy
                self.user_agent = user_agent

                if url:
                    self._url(url)

            def _url(self, url):
                parsed_url = Functions._url_ext(url)
                self.ar = parsed_url.get("ar", self.ar)
                self.k = parsed_url.get("k", self.k)
                self.co = parsed_url.get("co", self.co)
                self.hl = parsed_url.get("hl", self.hl)
                self.v = parsed_url.get("v", self.v)
                self.size = parsed_url.get("size", self.size)
                self.cb = parsed_url.get("cb", self.cb)
        @staticmethod
        def run(add_instance: 'Ninja.Sync.Add'):
            instance = Functions.SyncV3(
                ar=add_instance.ar,
                k=add_instance.k,
                co=add_instance.co,
                hl=add_instance.hl,
                v=add_instance.v,
                size=add_instance.size,
                cb=add_instance.cb,
                proxy=add_instance.proxy,
                user_agent=add_instance.user_agent
            )
            return instance._get_token()

    class Async:
        class Add:
            def __init__(self, ar: int = None, k: str = None, co: str = None, hl: str = "en", v: str = None, size: str = "invisible", cb: str = None, url: str = None, proxy=None, user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Avast/126.0.0.0') -> None:
                self.ar = ar
                self.k = k
                self.co = co
                self.hl = hl
                self.v = v
                self.size = size
                self.cb = cb
                self.url = url
                self.proxy = proxy
                self.user_agent = user_agent

                if url:
                    self._url(url)

            def _url(self, url):
                parsed_url = Functions._url_ext(url)
                self.ar = parsed_url.get("ar", self.ar)
                self.k = parsed_url.get("k", self.k)
                self.co = parsed_url.get("co", self.co)
                self.hl = parsed_url.get("hl", self.hl)
                self.v = parsed_url.get("v", self.v)
                self.size = parsed_url.get("size", self.size)
                self.cb = parsed_url.get("cb", self.cb)


        @staticmethod
        async def run(add_instance: 'Ninja.Async.Add'):
            instance = Functions.AsyncV3(
                ar=add_instance.ar,
                k=add_instance.k,
                co=add_instance.co,
                hl=add_instance.hl,
                v=add_instance.v,
                size=add_instance.size,
                cb=add_instance.cb,
                proxy=add_instance.proxy,
                user_agent=add_instance.user_agent
            )
            return await instance._get_token()

async def examples():
    add_instance = Ninja.Sync()
    dt = add_instance.Add(url="https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LethqgZAAAAAEZwXwfi_iP0dceTTwTKFX7moBuH&co=aHR0cHM6Ly93d3cubGlkbC5lczo0NDM.&hl=en&v=hfUfsXWZFeg83qqxrK27GB8P&size=invisible&cb=coegqdmdebk5")
    token = add_instance.run(dt)
    print(token)

    add_instance = Ninja.Async()
    dt = add_instance.Add(url="https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LethqgZAAAAAEZwXwfi_iP0dceTTwTKFX7moBuH&co=aHR0cHM6Ly93d3cubGlkbC5lczo0NDM.&hl=en&v=hfUfsXWZFeg83qqxrK27GB8P&size=invisible&cb=coegqdmdebk5")
    token = await add_instance.run(dt)
    print(token)
import asyncio
asyncio.run(examples())