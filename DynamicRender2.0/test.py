import asyncio
import httpx
from dynamicrender.DynamicChecker import Item
from dynamicrender.Renderer import BiliRender
import matplotlib.pyplot as plt
import time

def img_show(img):

    plt.imshow(img)
    plt.show()



async def main():
    url = "https://app.bilibili.com/x/topic/web/details/cards?topic_id=28484&sort_by=3&offset=&page_size=20&source=Web"
    response = httpx.get(url)
    data = response.json()
    # print(data)
    items = data["data"]["topic_card_list"]["items"]
    tasks = []

    for item in items:
        dynamic = item["dynamic_card_item"]
        card = Item(**dynamic)
        # start = time.time()
        img = await BiliRender(card).render()
        end = time.time()
        # print(end - start)
        img_show(img)

asyncio.run(main())
