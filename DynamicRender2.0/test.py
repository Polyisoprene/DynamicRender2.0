import asyncio
import matplotlib.pyplot as plt
import time
import json

# card = {"code":0,"message":"0","ttl":1,"data":{"item":{"basic":{"comment_id_str":"640417892069802054","comment_type":17,"like_icon":{"action_url":"","end_url":"","id":0,"start_url":""},"rid_str":"640417891998420315"},"id_str":"640417892069802054","modules":{"module_author":{"decorate":{"card_url":"http://i0.hdslb.com/bfs/garb/item/bef87ecfbdbf46020f1800d8c098771b1f7c56b7.png","fan":{"color":"","is_fan":false,"num_str":"","number":0},"id":5021,"jump_url":"https://live.bilibili.com/blackboard/activity-lVEr9rQGw2.html","name":"舰长","type":1},"face":"http://i1.hdslb.com/bfs/face/b796fc234e84db55d37f48562004a070705c2258.jpg","face_nft":false,"following":null,"jump_url":"//space.bilibili.com/37815472/dynamic","label":"","mid":37815472,"name":"_DMC_","official_verify":{"desc":"","type":-1},"pendant":{"expire":0,"image":"http://i1.hdslb.com/bfs/garb/item/1b7684c1de7dfc5aa0c43c55edb247432b0cbe64.png","image_enhance":"http://i1.hdslb.com/bfs/garb/item/1b7684c1de7dfc5aa0c43c55edb247432b0cbe64.png","image_enhance_frame":"","name":"大航海_舰长","pid":1010},"pub_action":"","pub_time":"2022-03-22 19:08","pub_ts":1647947310,"type":"AUTHOR_TYPE_NORMAL","vip":{"avatar_subscript":0,"avatar_subscript_url":"","due_date":1647446400000,"label":{"bg_color":"","bg_style":0,"border_color":"","label_theme":"","path":"","text":"","text_color":""},"nickname_color":"","status":0,"theme_type":0,"type":1}},"module_dynamic":{"additional":null,"desc":{"rich_text_nodes":[{"orig_text":"这条动态包含了话题 ","text":"这条动态包含了话题 ","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"//search.bilibili.com/all?keyword=%23%E6%A1%83%E6%A1%83%E7%9A%84%E6%89%8B%E8%B4%A6%23","orig_text":"#桃桃的手账#","text":"#桃桃的手账#","type":"RICH_TEXT_NODE_TYPE_TOPIC"},{"orig_text":"  ","text":"  ","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"//search.bilibili.com/all?keyword=%23%E5%A4%8F%E5%8D%9C%E5%8D%9C%23","orig_text":"#夏卜卜#","text":"#夏卜卜#","type":"RICH_TEXT_NODE_TYPE_TOPIC"},{"orig_text":"，","text":"，","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"emoji":{"icon_url":"http://i0.hdslb.com/bfs/emote/362bded07ea5434886271d23fa25f5d85d8af06c.png","size":1,"text":"[哦呼]","type":1},"orig_text":"[哦呼]","text":"[哦呼]","type":"RICH_TEXT_NODE_TYPE_EMOJI"},{"orig_text":"以及emoji 😃😀 ，","text":"以及emoji 😃😀 ，","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"//search.bilibili.com/all?keyword=%23%E5%92%8C%E6%88%91%E4%B8%80%E8%B5%B7%E5%94%B1%E6%AD%8C%E5%90%A7%23","orig_text":"#和我一起唱歌吧#","text":"#和我一起唱歌吧#","type":"RICH_TEXT_NODE_TYPE_TOPIC"},{"orig_text":"，以及可能还有富文本","text":"，以及可能还有富文本","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"//www.bilibili.com/video/BV1EP4y1T7am","orig_text":"BV1EP4y1T7am","text":"【直播回放】白色情人节晚年歌回 2022年3月19日19点场","type":"RICH_TEXT_NODE_TYPE_BV"},{"orig_text":" ，可能还富含其他东西 ","text":" ，可能还富含其他东西 ","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"orig_text":"@心机卜 ","rid":"490040351","text":"@心机卜 ","type":"RICH_TEXT_NODE_TYPE_AT"},{"orig_text":"为什么会这样呢？是特性吗","text":"为什么会这样呢？是特性吗","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"//www.bilibili.com/video/BV1au411q7LN","orig_text":"BV1au411q7LN","text":"【python真·实战】Ctrl+C不好用了？Windows多线程的坑你踩过嘛？","type":"RICH_TEXT_NODE_TYPE_BV"},{"orig_text":"？？","text":"？？","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"https://www.bilibili.com/read/cv3001502","orig_text":"https://www.bilibili.com/read/cv3001502","text":"网页链接","type":"RICH_TEXT_NODE_TYPE_WEB"},{"orig_text":" ","text":" ","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"jump_url":"https://t.bilibili.com/640247201475330055","orig_text":"https://t.bilibili.com/640247201475330055","text":"网页链接","type":"RICH_TEXT_NODE_TYPE_WEB"},{"orig_text":" ，以及B","text":" ，以及B","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"emoji":{"icon_url":"http://i0.hdslb.com/bfs/emote/70330154c2589c92bd29fb7bcd0503b621f8d0c9.png","size":1,"text":"[雪容融]","type":1},"orig_text":"[雪容融]","text":"[雪容融]","type":"RICH_TEXT_NODE_TYPE_EMOJI"},{"emoji":{"icon_url":"http://i0.hdslb.com/bfs/emote/b4cb77159d58614a9b787b91b1cd22a81f383535.png","size":1,"text":"[妙啊]","type":1},"orig_text":"[妙啊]","text":"[妙啊]","type":"RICH_TEXT_NODE_TYPE_EMOJI"},{"orig_text":"站自带的表情","text":"站自带的表情","type":"RICH_TEXT_NODE_TYPE_TEXT"},{"emoji":{"icon_url":"http://i0.hdslb.com/bfs/emote/3087d273a78ccaff4bb1e9972e2ba2a7583c9f11.png","size":1,"text":"[doge]","type":1},"orig_text":"[doge]","text":"[doge]","type":"RICH_TEXT_NODE_TYPE_EMOJI"},{"emoji":{"icon_url":"http://i0.hdslb.com/bfs/emote/3087d273a78ccaff4bb1e9972e2ba2a7583c9f11.png","size":1,"text":"[doge]","type":1},"orig_text":"[doge]","text":"[doge]","type":"RICH_TEXT_NODE_TYPE_EMOJI"},{"orig_text":"以及at某个人","text":"以及at某个人","type":"RICH_TEXT_NODE_TYPE_TEXT"}],"text":"这条动态包含了话题 #桃桃的手账#  #夏卜卜#，[哦呼]以及emoji 😃😀 ，#和我一起唱歌吧#，以及可能还有富文本BV1EP4y1T7am ，可能还富含其他东西 @心机卜 为什么会这样呢？是特性吗https://b23.tv/BV1au411q7LN？？https://www.bilibili.com/read/cv3001502 https://t.bilibili.com/640247201475330055 ，以及B[雪容融][妙啊]站自带的表情[doge][doge]以及at某个人"},"major":null,"topic":null},"module_more":{"three_point_items":[{"label":"删除","modal":{"cancel":"我点错了","confirm":"删除","content":"确定要删除此条动态吗？","title":"删除动态"},"type":"THREE_POINT_DELETE"}]},"module_stat":{"comment":{"count":0,"forbidden":false,"text":"0"},"forward":{"count":1,"forbidden":false,"text":"1"},"like":{"count":6,"forbidden":false,"status":true,"text":"6"}}},"type":"DYNAMIC_TYPE_WORD","visible":true}}}
#
# card = json.loads(card)

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
        # global card
        url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id=640417892069802054"
        resp = httpx.get(url)
        data = resp.json()

        item = data["data"]["item"]
        dynamic = Item(**item)
        start = time.time()
        re = await BiliRender(dynamic=dynamic).word_dynamic()
        print(time.time()-start)
        if re:
            img_show(re)
    asyncio.run(run())
# a = {"1","2"}
#
# print("1" in a)