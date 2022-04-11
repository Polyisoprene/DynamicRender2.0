import asyncio
import matplotlib.pyplot as plt
import time
import json

def img_show(img):

    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    import httpx
    from dynamicrender.DynamicChecker import Item
    from dynamicrender.Renderer import BiliRender


    def time_log(func):
        async def wrap(*args, **kwargs):
            start = time.time()
            result = await func(*args, **kwargs)
            print("程序花费时长:"+str(time.time()-start))
            return result
        return wrap

    @time_log
    async def run():
        url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id=647670184872509449"
        resp = httpx.get(url)
        data = resp.json()
        item = data["data"]["item"]
        dynamic = Item(**item)
        start = time.time()
        re = await BiliRender(dynamic=dynamic).render()
        print(time.time() - start)
        if re:
            img_show(re)
    asyncio.run(run())

