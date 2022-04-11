import httpx
from pydantic import BaseModel

# class FollowData(BaseModel):
#     uid: str
#     cookie: dict

# data = {
#     'uid': 2049968320,
#     'act':1,
#     'cookie': {"DedeUserID": "1223217427", "DedeUserID__ckMd5": "43128c26a99d8d4a", "Expires": "15551000",
#                "SESSDATA": "01623a8e%2C1665124233%2C1f740%2A41", "bili_jct": "d65cebe79a642b544d4497c7053b1e47"}
# }
# url = "https://dmc.lzxder.xyz:2233/follow"
# response = httpx.post(url=url, json=data)
# print(response.json())
# a = (1,2,3,{"a":123})
# print(list(a))
uids = [2049968320,37815472]
uids = {'uids': uids}
url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
response = httpx.post(url, json=uids)
data = response.json()
print(data)