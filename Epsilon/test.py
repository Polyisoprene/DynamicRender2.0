# js = """[CQ:json,data={"app":"com.tencent.structmsg"&#44;"config":{"ctime":1649761654&#44;"forward":true&#44;"token":"603366c15154dae7a8452f091c1eadd3"&#44;"type":"normal"}&#44;"desc":"新闻"&#44;"extra":{"app_type":1&#44;"appid":100951776&#44;"msg_seq":7085672345936374731&#44;"uin":3064615013}&#44;"meta":{"news":{"action":""&#44;"android_pkg_name":""&#44;"app_type":1&#44;"appid":100951776&#44;"ctime":1649761654&#44;"desc":"夏卜卜"&#44;"jumpUrl":"https://b23.tv/CBoe6tU?share_medium=android&amp;share_source=qq&amp;bbid=XYC2CCBCE72C509C6203274F078C65385BA5A&amp;ts=1649761623684"&#44;"preview":"https://pic.ugcimg.cn/91147f3a3eb413bbc24ec7948f33734b/jpg1"&#44;"source_icon":"https://open.gtimg.cn/open/app_icon/00/95/17/76/100951776_100_m.png?t=1649411918"&#44;"source_url":""&#44;"tag":"哔哩哔哩"&#44;"title":" 本周直播预告出现啦！不知道奥日第二部做得怎么样，但是..."&#44;"uin":3064615013}}&#44;"prompt":"&#91;分享&#93;本周直播预告出现啦！不知道奥日第二部做得怎么样， 但是..."&#44;"ver":"0.0.0.1"&#44;"view":"news"}]"""
# bt = re.search("https://b23\.tv/(\w+)",js).group()
# response = httpx.get(bt)
# data = response.headers.get("location")
# result = re.search("https://m.bilibili.com/dynamic/(\d+)", data).group()
# dynamic_id = re.search('(\d+)', result)
# print(dynamic_id.group())
# url = "https://api.bilibili.com/x/web-interface/view?bvid=BV1Ei4y1D741"
#
# res = httpx.get(url)
# print(res.json())
# print(bt)

import json

# uids = [649833]
#
# uids = {'uids': uids}
#
# url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
# response = httpx.post(url, json=uids)
# data = response.json()
# data = data["data"]
# print(data)
# import requests
#
# url = 'https://api.bilibili.com/x/share/click'
# # link = input('输入哔哩哔哩url')
# link = "https://t.bilibili.com/649316433115742217"
# # 请求参数
# data = {'build': '9331', 'buvid': '74fe03588ceace988e365fd982bd0955', 'oid': link, 'platform': 'ios',
#         'share_channel': 'COPY', 'share_id': 'public.webview.0.0.pv', 'share_mode': '3'}
# r = requests.post(url, data)
# reapi = r.json()
# # datalink = reapi.get('data')
# print(reapi)
# input("Press Any Key")
topic_url = "https://www.bilibili.com/v/topic/detail?topic_id=28484"

url = "https://app.bilibili.com/x/topic/web/details/cards?topic_id=28484&sort_by=3&offset=&page_size=20&source=Web"