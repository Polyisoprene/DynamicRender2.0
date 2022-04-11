import asyncio
import json
import traceback

from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment, Message

from ..BliApi import Api
from ..DataManager import DataManage
from ..MessageManager import MessageSender


class PushLive:
    def __init__(self, cookie, all_sub_info):
        self.cookie = cookie
        self.all_sub_info = all_sub_info

    async def pusher(self):
        uid_list = []
        info_dict = {}
        for i in self.all_sub_info:
            uid = i[0]
            uid_list.append(uid)
            info_dict[str(uid)] = {"live_status": i[2], "sub_info": i[3]}
        live_room_info = await Api().get_room_info(uid_list)
        tasks = []
        if live_room_info:
            for k, v in live_room_info.items():
                tasks.append(self.compare_live_status(k, v, info_dict))
            await asyncio.gather(*tasks)

    async def compare_live_status(self, uid, single_room_info, info_dict):
        new_status = single_room_info["live_status"]
        if new_status == 1 and info_dict[str(uid)]["live_status"] != new_status:
            with DataManage() as update:
                await update.modify_live_status(uid, new_status)
            sub_info = json.loads(info_dict[str(uid)]["sub_info"])
            live_room_link = "https://live.bilibili.com/" + str(single_room_info["room_id"])
            cover = single_room_info["cover_from_user"] if single_room_info["cover_from_user"] else single_room_info[
                "keyframe"]
            message = f"【{single_room_info['uname']}】开播啦!!!\n\n标题:{single_room_info['title']}\n\n传送门:{live_room_link}\n" + MessageSegment.image(
                cover)
            for k, v in sub_info.items():
                await self.__send_checker(message, k, v)
        else:
            with DataManage() as update:
                await update.modify_live_status(uid, new_status)

    async def __send_checker(self, message: Message, position, group_sub_info):
        tasks = []
        for k, v in group_sub_info.items():
            tasks.append(self.__message_sender(message, position, k, v))
        await asyncio.gather(*tasks)

    async def __message_sender(self, message: Message, position, bot_id, sub_info):
        """发送消息"""
        # 查看bot开关状态
        try:
            bot_status = await self.__check_bot_status(position, bot_id)
            if bot_status:
                if sub_info["DynamicOn"] == 1:
                    if position.isdigit():
                        await MessageSender(message=message, bot_id=bot_id).send_to("group", position)
                    else:
                        position_dic = json.loads(position)
                        await MessageSender(message=message, bot_id=bot_id).send_to("guild",
                                                                                    guild_id=position_dic["guild_id"],
                                                                                    channel_id=position_dic[
                                                                                        "channel_id"])
        except Exception as e:
            logger.error(traceback.print_exc())

    async def __check_bot_status(self, position, bot_id) -> bool:
        """检查开关状态函数"""
        # 查看这个群是否开启了开关
        bot_id = int(bot_id)
        with DataManage() as switch_getter:
            switch = await switch_getter.acquire_SwitchStatus(position, bot_id)
        # 如果没找到开关就新添一个开关
        if not switch:
            with DataManage() as switch_setter:
                await switch_setter.store_SwitchStatus(position, bot_id)
            return True
        else:
            if switch[0] == 1:
                return True
            else:
                return False
